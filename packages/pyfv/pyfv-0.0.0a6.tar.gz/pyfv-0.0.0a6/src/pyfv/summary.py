#!/opt/miniconda3/bin/python
# -----------------------------------------------------------------------------
# PyFV: A modern Python FITS Viewer
# Copyright (c) 2025, Pan S. Chai
# Distributed under the BSD 3-Clause License. See LICENSE file for details.
# -----------------------------------------------------------------------------
#   
#  Python FV Project
#
#      module: summary.py
#
#  Version: Ver 1.0 (beta)
#
#-------------------------------------------------------------------------------
#       
# Modification History: 
#
#   - Pan Chai, October 2025
#     Package migrated 
#           
#-------------------------------------------------------------------------------
#
# Description:
#
#   - open file selection dialog
#   - using AstroPy to gather FITS info
#   - separate the gathered FITS info into different functionalities
#     - Header
#     - Plot/Image
#     - Table 
#   
#-------------------------------------------------------------------------------
#

import os
import io
import re

from astropy.io import fits
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

from pathlib import Path
import sys
import codecs
import os

import time
import traceback, sys
import numpy as np
import subprocess

from header import HeaderLoader, show_header_dialog
from header import HeaderLoader, open_header_editor
# from table import show_table_dialog
from table import open_table_editor
from help import HelpWindow
import pow as pow_view

# Path to THIS file (fv.py)
fv_dir = os.path.dirname(os.path.abspath(__file__))

# Path to pow.py in the same directory
pow_path = os.path.join(fv_dir, "pow.py")

class PlotColumnDialog(QDialog):
    def __init__(self, parent, fits_file, hdu_index, column_names):
        super().__init__(parent)
        self.setWindowTitle("Select Columns to Plot")
        self.fits_file = fits_file
        self.hdu_index = hdu_index

        layout = QVBoxLayout(self)

        layout.addWidget(QLabel("Select X column:"))
        self.x_combo = QComboBox()
        self.x_combo.addItems(column_names)
        layout.addWidget(self.x_combo)

        layout.addWidget(QLabel("Select Y column:"))
        self.y_combo = QComboBox()
        self.y_combo.addItems(column_names)
        layout.addWidget(self.y_combo)

        btn_layout = QHBoxLayout()
        plot_button = QPushButton("Plot")
        plot_button.clicked.connect(self.launch_plot)
        btn_layout.addWidget(plot_button)

        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.reject)
        btn_layout.addWidget(cancel_button)

        layout.addLayout(btn_layout)

    def launch_plot(self):
        from pathlib import Path
        import subprocess

        fits_path = str(Path(self.fits_file).resolve())
        x_col = self.x_combo.currentText()
        y_col = self.y_combo.currentText()
        idx_str = str(self.hdu_index)

        try:
            proc = subprocess.Popen(['python', pow_path, fits_path, idx_str, x_col, y_col, 'plot'])
            self.parent().pow_processes.append(proc)
        except Exception as e:
            print(f"Failed to launch plot: {e}")
        self.accept()

class FitsSummaryDialog(QMainWindow):
    header_ready = pyqtSignal(int, str)

    def closeEvent(self, event):
        try:
            if hasattr(self, "help_window") and self.help_window is not None:
                self.help_window.close()
        except Exception as e:
            print(f"[Summary] Error closing help window: {e}")
        event.accept()

    def __init__(self, fits_file, summary_data=None, parent=None):
        super().__init__(parent)
        self.fits_file = fits_file
        self.summary_data = summary_data
        self.active_button = None

        self.threads = []
        self.header_dialogs = []
        self.pow_processes = []

        displayDirName = os.path.dirname(fits_file) 
        displayFileName = os.path.basename(fits_file) 
        self.setWindowTitle(f"fv: Summary of {displayFileName} in {displayDirName}  ")
        self.initUI()

    def close_all(self):
        # Terminate all launched pow.py processes
        if hasattr(self, "pow_processes"):
            for proc in self.pow_processes:
                try:
                    if proc.poll() is None:
                        proc.terminate()
                except Exception as e:
                    print(f"Error terminating pow.py process: {e}")
            self.pow_processes.clear()

        # Close old-style dialogs (if any)
        for dlg in self.header_dialogs:
            if dlg.isVisible():     
                dlg.close()         
        self.header_dialogs.clear() 
                                    
        # Close the shared tabbed header dialog (if exists)
        if hasattr(self, "header_tab_dialog") and self.header_tab_dialog:
            self.header_tab_dialog.close()
            self.header_tab_dialog = None
    
        self.close()

    def show_image_viewer(self, hdu_index):

        # Build temporary FITS file with only the selected HDU if needed.
        # But for now, just pass the full file.
        try:
            #script_path = os.path.join(os.path.dirname(__file__), "pow.py")
            #subprocess.Popen(["/opt/miniconda3/bin/python", script_path, self.fits_file, hdu_index])
            subprocess.Popen(["python", pow_path, self.fits_file, hdu_index])
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to open pow.py:\n{e}")

    def show_table_viewer(self, hdu_index):
        viewer = TableViewer(self.fits_file, hdu_index, self)
        viewer.exec()

    def load_and_show_header(self, hdu_index: int):
        fits_file = self.fits_file  # or however you store it
    
        # 1) create the worker and a real QThread INSTANCE
        worker = HeaderLoader(fits_file, hdu_index)
        thread = QThread(self)  # <-- instance, not the class

        # 2) move worker to the thread
        worker.moveToThread(thread)

        # 3) connect signals
        thread.started.connect(worker.run)

        def on_finished(idx, header_text):
            # Show with your legacy read-only dialog:
            # show_header_dialog(self, fits_file, idx, header_text)
            # If you'd rather open the NEW editable header tab instead, comment the line above
            # and use the line below:

            open_header_editor(self, fits_file, idx)

            # clean up & allow thread to exit
            thread.quit()

        worker.finished.connect(on_finished)

        # 4) tidy up memory when done
        worker.finished.connect(worker.deleteLater)
        thread.finished.connect(thread.deleteLater)

        # 5) keep refs so they don't get GC'd early
        if not hasattr(self, "_header_threads"): self._header_threads = []
        if not hasattr(self, "_header_workers"): self._header_workers = []
        self._header_threads.append(thread)
        self._header_workers.append(worker)

        # optional: remove refs once thread actually stops
        def _cleanup():
            try:
                self._header_threads.remove(thread)
            except ValueError:
                pass
            try:
                self._header_workers.remove(worker)
            except ValueError:
                pass
        thread.finished.connect(_cleanup)

        # 6) go!
        thread.start()

    def load_and_show_header_X(self, hdu_index):
        # print(f"[Main] Starting thread for HDU {hdu_index}")

        thread = QThread(self)
        worker = HeaderLoader(self.fits_file, hdu_index)
        worker.moveToThread(thread)

        def on_result(index, text):
            # print(f"[Main] Got result for HDU {index}")
            #show_header_dialog(self, os.path.basename(self.fits_file), index, text)
            open_header_editor(self, os.path.basename(self.fits_file), index)

        def cleanup():
            # print(f"[Thread] Finished for HDU {hdu_index}")
            self.threads.remove(thread)
            thread.deleteLater()

        thread.started.connect(lambda: worker.run())
        worker.finished.connect(on_result)
        worker.finished.connect(thread.quit)
        worker.finished.connect(worker.deleteLater)
        thread.finished.connect(cleanup)

        self.threads.append(thread)
        thread.start()

    def initUI(self):

        # For each data row
        def centered_label(text):
            lbl = QLabel(text)
            lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
            return lbl

        central = QWidget()
        layout = QVBoxLayout(central)

        # Style to match other buttons
        menu_button_style = """
            QToolButton {
                padding: 6px 12px;
                border: none;
                border-radius: 0px;
                background-color: #f0f0f0;
                font-size: 14px;
                font-weight: bold;
            }
            QToolButton::menu-indicator {
                image: none;
            }
        """
        menu_dropdown_style = """
            QMenu {
                font-size: 16pt;
                background-color: #ffffff;
                color: #000000;
                border: 1px solid #999999;
            }
            QMenu::item {
                padding: 6px 20px;
            }
            QMenu::item:selected {
                background-color: #e0e0e0;
            }
        """

        menu_row = QHBoxLayout()
        menu_row.setContentsMargins(0, 0, 0, 0)   # Remove outer padding
        menu_row.setSpacing(0)                    # Remove space between buttons
        menu_row.setAlignment(Qt.AlignmentFlag.AlignLeft)  # Align to left

        # Create "File" menu button
        file_button = QToolButton()
        file_button.setText("File")
        file_button.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)
        file_button.setStyleSheet(menu_button_style)

        file_menu = QMenu(file_button)
        open_action = QAction("Open...", self)
        open_action.triggered.connect(lambda: self.parent().selectFile(None))
        file_menu.addAction(open_action)
        file_menu.setStyleSheet(menu_dropdown_style)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close_all)
        file_menu.addAction(exit_action)

        file_button.setMenu(file_menu)
        menu_row.addWidget(file_button)

        # Create "Edit" menu button
        #edit_button = QToolButton()
        #edit_button.setText("Edit")
        #edit_button.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)
        #edit_button.setStyleSheet(menu_button_style)

        #menu_row.addWidget(edit_button)

        # Create "Tool" menu button
        #tool_button = QToolButton()
        #tool_button.setText("Tool")
        #tool_button.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)
        #tool_button.setStyleSheet(menu_button_style)

        #menu_row.addWidget(tool_button)

        # Create "Help" menu button
        help_button = QToolButton()
        help_button.setText("Help")
        help_button.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)
        help_button.setStyleSheet(menu_button_style)

        help_menu = QMenu(help_button)
        help_menu.setStyleSheet(menu_dropdown_style)

        help_topics = [
            "About FV", "Start FV", "Calculator", "Calculator Expressions", "Column Selection",
            "Column Statistics", "Create New FITS File", "Deleting Rows", "Desktop Manager",
            "Display Device", "Column Parameters", "File Summmary", "File Selection",
            "Header Display", "Image Plots", "FV License", "Plot Dialog", "Preferences",
            "Sorting Columns", "Scripting", "SkyView", "Catalog Database", "VizieR",
            "FTOOLs Execution", "Table Display", "Image Tables", "Hisograms", "3D Image Tables",
            "3D Image Display"
        ]

        for topic in help_topics:
            action = QAction(topic, self)
            action.triggered.connect(lambda checked, t=topic: self.show_help_topic(t))
            help_menu.addAction(action)

        help_button.setMenu(help_menu)
        menu_row.addWidget(help_button)

        # Add menu_row to main layout
        menu_container = QWidget()
        menu_container.setLayout(menu_row)

        # Create a horizontal line (QFrame)
        menu_separator = QFrame()
        menu_separator.setFrameShape(QFrame.Shape.HLine)
        menu_separator.setFrameShadow(QFrame.Shadow.Sunken)
        menu_separator.setStyleSheet("margin-top: 2px; margin-bottom: 6px; color: #888888; background-color: #888888;")

        layout.addWidget(menu_container)
        layout.addWidget(menu_separator)

        grid = QGridLayout()

        headers = ["", "Index", "Name", "Type", "Dimensions", "View"]

        for col, header in enumerate(headers):
            label = QLabel(f"<b>{header}</b>")
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            grid.addWidget(label, 0, col)

        # Add horizontal line under header
        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)
        line.setStyleSheet("margin-top: 2px; margin-bottom: 6px; color: #888888; background-color: #888888;")
        #line.setStyleSheet("margin-top: 4px; margin-bottom: 4px;")
        grid.addWidget(line, 1, 0, 1, 6)
 
        row = 2 # start of the row 3

        with fits.open(self.fits_file) as hdulist:
            for idx, hdu in enumerate(hdulist):
                name = hdu.name.strip() or ("PRIMARY" if idx == 0 else f"HDU{idx}")

                # Type
                if isinstance(hdu, (fits.PrimaryHDU, fits.ImageHDU)):
                    hdu_type = "Image"
                elif isinstance(hdu, fits.BinTableHDU):
                    hdu_type = "Binary"
                elif isinstance(hdu, fits.TableHDU):
                    hdu_type = "ASCII"
                else:
                    hdu_type = type(hdu).__name__

                # Dimensions
                if hdu.data is None:
                    dims = "0"
                elif isinstance(hdu, (fits.BinTableHDU, fits.TableHDU)):
                    # dims = f"{len(hdu.data)} x {len(hdu.columns)}"
                    dims = f"{len(hdu.columns)} cols × {len(hdu.data)} rows"
                else:
                    dims = " x ".join(str(x) for x in hdu.data.shape)

                # View Type
                if isinstance(hdu, fits.BinTableHDU):
                    view = "Binary"
                    # view_buttons = ["Header", "Plot", "HIST", "Table"]
                    view_buttons = ["Header", "Plot", "Table"]
                elif isinstance(hdu, (fits.PrimaryHDU, fits.ImageHDU)):
                    view = "Image"
                    view_buttons = ["Header", "Image", "Table"]
                else:
                    view = "Unknown"
                    view_buttons = ["Header"]

                # Add to grid
                row = row +  1

                # grid.addWidget(centered_label(""), row, 0)

                checkbox = QCheckBox()
                checkbox.setObjectName(f"checkbox_{idx}")
                checkbox.setChecked(False)
                checkbox.setStyleSheet("margin-left:10px;")
                checkbox.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
                grid.addWidget(checkbox, row, 0)

                for col, text in enumerate([str(idx), name, hdu_type, dims], start=1):
                    lbl = centered_label(text)
                    lbl.setStyleSheet("font-size: 16pt; margin: 0px; padding: 0px;")
                    lbl.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
                    grid.addWidget(lbl, row, col)

                button_layout = QHBoxLayout()
                button_layout.setContentsMargins(0, 0, 0, 0)
                button_layout.setSpacing(4)  # You can tweak this for tighter button spacing

                for label in view_buttons:
                    btn = QPushButton(label)
                    btn.setObjectName(f"{label.lower()}_btn_{idx}")
                    btn.setCheckable(True)

                    # callback to display Header

                    def make_view_callback(index, label, button):
                        label = label.lower()
                        if label == "header":
                            return lambda: (
                                self.load_and_show_header(index),
                                button.setChecked(False)
                            )
                        elif label == "table":
                            return lambda: (
                                # show_table_dialog(self, self.fits_file, index),
                                open_table_editor(self, self.fits_file, index),
                                button.setChecked(False)
                            )
                        elif label == "image":
                            def launch_image():
                                try:
                                    import pow as pow_view  # local import so you don't need to modify the top of the file
                                    pow_view.open_image_or_animate(self, self.fits_file, index)
                                except Exception as e:
                                    print(f"Failed to open image viewer: {e}")
                                button.setChecked(False)
                            return launch_image
                        elif label == "plot":
                            def plot_handler():
                                try:
                                    with fits.open(self.fits_file) as hdul:
                                        hdu = hdul[index]
                                        if not isinstance(hdu, (fits.BinTableHDU, fits.TableHDU)):
                                            print("Not a table HDU.")
                                            return

                                        column_names = hdu.columns.names
                                except Exception as e:
                                    print(f"Error reading FITS file: {e}")
                                    return

                                dlg = PlotColumnDialog(self, self.fits_file, index, column_names)
                                dlg.exec()
                                button.setChecked(False)

                            return plot_handler
                        else:
                            return lambda: self.on_view_clicked(index, label, button)

                    btn.setAutoExclusive(False)
                    btn.setChecked(False)
                    btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
                    btn.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)

                    label_lower = label.lower()

                    # Check if the button should be disabled due to missing data
                    if label_lower in ["image", "table"]:
                        if hdu.data is None or (
                            label_lower == "image" and not (
                                isinstance(hdu.data, (list, tuple, np.ndarray)) and hasattr(hdu.data, "shape") and len(hdu.data.shape) >= 2
                            )
                        ) or (
                            label_lower == "table" and isinstance(hdu, (fits.BinTableHDU, fits.TableHDU)) and len(hdu.data) == 0
                        ):
                            btn.setEnabled(False)
                            btn.setStyleSheet("background-color: #dddddd; color: #888888; font-size: 16px; font-weight: bold; padding: 8px 6px; margin: 0px;")
                        else:
                            btn.clicked.connect(make_view_callback(idx, label, btn))
                            btn.setStyleSheet("background-color: white; font-size: 16px; font-weight: bold; padding: 8px 6px; margin: 0px;")
                    else:
                        btn.clicked.connect(make_view_callback(idx, label, btn))
                        btn.setStyleSheet("background-color: white; font-size: 16px; font-weight: bold; padding: 8px 6px; margin: 0px;")

                    button_layout.addWidget(btn)

                button_widget = QWidget()
                button_widget.setLayout(button_layout)
                button_widget.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
                grid.addWidget(button_widget, row, 5)

        layout.addLayout(grid)
        central.setLayout(layout)
        self.setCentralWidget(central)

        # Close button
        # close_button = QPushButton("Close")
        # close_button.clicked.connect(self.close)
        # layout.addWidget(close_button)

        # self.setLayout(layout)

    def show_help_topic(self, topic):
        self.help_window = HelpWindow(topic)
        self.help_window.show()

    def on_view_clicked(self, hdu_index, view_type, button):
        print(f"[Clicked] HDU {hdu_index} - View: {view_type}")

        # Unhighlight previous button
        if self.active_button and self.active_button != button:
            self.active_button.setChecked(False)
            self.active_button.setStyleSheet("background-color: white; font-size: 16px; font-weight: bold; padding: 8px 6px; margin: 0px;")

        # Highlight new button
        button.setChecked(True)
        button.setStyleSheet("""
            QPushButton {
                background-color: lightblue;
                font-size: 16px;
                font-weight: bold;
                padding: 8px 6px; 
                margin: 0px;
            }
        """)

        self.active_button = button


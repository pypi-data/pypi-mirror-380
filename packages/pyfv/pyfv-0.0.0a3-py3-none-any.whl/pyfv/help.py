#!/opt/miniconda3/bin/python
# -----------------------------------------------------------------------------
# PyFV: A modern Python FITS Viewer
# Copyright (c) 2025, Pan S. Chai
# Distributed under the BSD 3-Clause License. See LICENSE file for details.
# -----------------------------------------------------------------------------
#
#  Python FV Project
#
#      module: help.py
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
#   Routine to display FV help files
#
#-------------------------------------------------------------------------------
#

from PyQt6.QtWidgets import QApplication, QMainWindow, QTextBrowser, QVBoxLayout, QWidget, QComboBox
from PyQt6.QtCore import QUrl
import sys, os

class HelpWindow(QMainWindow):
    def __init__(self, topic="Start FV"):
        super().__init__()
        self.setWindowTitle("FV Help")
        self.resize(800, 600)

        # Map dropdown items to filenames
        self.help_pages = {
            'About FV': 'aboutFV.html',
            'Start FV': 'startFV.html',
            'Calculator': 'calculator.html',
            'Calculator Expressions': 'expressions.html',
            'Column Selection': 'columnSelection.html',
            'Column Statistics': 'columnStatistics.html',
            'Create New FITS File': 'createNewFITS.html',
            'Deleting Rows': 'deleteRows.html',
            'Desktop Manager': 'deskTopManager.html',
            'Display Device': 'displayDevice.html',
            'Column Parameters': 'displayFormat.html',
            'File Summmary': 'fileSummary.html',
            'File Selection': 'fileSelection.html',
            'Header Display': 'headerDisplay.html',
            'Image Plots': 'imagePlot.html',
            'FV License': 'license.html',
            'Plot Dialog': 'plotDialog.html',
            'Preferences': 'preferences.html',
            'Sorting Columns': 'sortColumn.html',
            'Scripting': 'fv_scripting.html',
            'SkyView': 'SkyView.html',
            'Catalog Database': 'catalog.html',
            'VizieR': 'VizieR.html',
            'FTOOLs Execution': 'ftool.html',
            'Table Display': 'tableDisplay.html',
            'Image Tables': 'imageDisplay.html',
            'Hisograms': '2D-Histogram.html',
            '3D Image Tables': '3D-ImageTable.html',
            '3D Image Display': '3D-ImageDisplay.html'
        }

        layout = QVBoxLayout()

        # Dropdown to select help topic
        self.select_box = QComboBox()
        self.select_box.addItems(self.help_pages.keys())
        self.select_box.currentTextChanged.connect(self.load_topic)
        layout.addWidget(self.select_box)

        # Text viewer
        self.browser = QTextBrowser()
        layout.addWidget(self.browser)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Determine starting topic
        if topic in self.help_pages:
            self.select_box.setCurrentText(topic)
        else:
            self.select_box.setCurrentText("Start FV")  # fallback
        self.load_topic(self.select_box.currentText())

    def load_topic(self, topic_name):
        from pathlib import Path

        fv_file = Path(__file__).resolve()
        current = fv_file.parent

        while current != current.root:
            if (current / "doc").exists():
                help_dir = current / "doc"
                break
            current = current.parent

        filename = self.help_pages.get(topic_name, None)
        if filename:
            # help_dir = os.path.join(os.getcwd(), "doc")
            file_path = os.path.join(help_dir, filename)
            if os.path.exists(file_path):
                self.browser.setSource(QUrl.fromLocalFile(file_path))
            else:
                self.browser.setHtml(f"<h2>Help file not found: {filename}</h2>")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HelpWindow()
    window.show()
    sys.exit(app.exec())


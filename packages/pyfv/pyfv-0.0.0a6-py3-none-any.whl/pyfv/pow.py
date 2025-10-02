#!/opt/miniconda3/bin/python
# -----------------------------------------------------------------------------
# PyFV: A modern Python FITS Viewer
# Copyright (c) 2025, Pan S. Chai
# Distributed under the BSD 3-Clause License. See LICENSE file for details.
# -----------------------------------------------------------------------------
#
#  Python FV Project
#
#      module: pow.py
#
#  Version: Ver 1.0 (beta)
#
#-------------------------------------------------------------------------------
#
# Modification History:
#
#   - Pan Chai, October, 2025
#     Package created and tested.
#
#-------------------------------------------------------------------------------
#
# Usage:
#
#   1. ds9 path is set in environment variable: os.environ['DS9_PATH']
#      and default value is set using MacOS X: "/Applications/SAOImageDS9.app/Contents/MacOS/ds9"
#      if ds9 is going to be used for pow, change the value to where ds9 is installed.
#
#   2. Run by executing this command INSIDE the directory
#
#       for Image FITS file: ./poww.py <fits_file> <hdu_index>
#       for Table FITS file plot:  python pow.py <fits_file> <hdu_index> <col_x> <col_y> plot
#
#-------------------------------------------------------------------------------
#

import os
import PyQt6

# Ensure Qt can find the Cocoa plugin on macOS
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = os.path.join(
    os.path.dirname(PyQt6.__file__), "Qt6", "plugins", "platforms"
)

import sys
import shutil
import warnings
import subprocess
import time
import numpy as np
import re
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import (QFileDialog, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton,
                             QGroupBox,
                             QLabel, QTableView, QWidget, QLineEdit, QSizePolicy,
                             QComboBox, QSlider, QSplitter, QCheckBox)
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import QDialog, QDialogButtonBox, QLabel, QGridLayout, QVBoxLayout, QHBoxLayout, QPushButton, QSpinBox, QMessageBox, QWidget
from PyQt6.QtGui import QImage, QPixmap
import numpy as np
from astropy.io import fits

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib import gridspec
from matplotlib.patches import Rectangle

from astropy.io import fits
from astropy.wcs import WCS, FITSFixedWarning
from typing import Optional

from astropy.visualization.wcsaxes import WCSAxes
from matplotlib.transforms import Affine2D
from astropy.coordinates import Angle

import pandas as pd

is_flipped = False;

os.environ["XPA_METHOD"] = "local"
os.environ["DS9_PATH"] = "/Applications/SAOImageDS9.app/Contents/MacOS/ds9"

class SliceRangeDialogPow(QDialog):
    """
    FV-style slice range picker for 3D/4D cubes.
    Returns (cube_1based, start_1based, end_1based, fps) if accepted.
    For 3D, cube_1based is always 1 and the 'Data Cube' control is hidden.
    """
   # def __init__(self, parent: QWidget, z_len: int, s_len: Optional[int] = None, default_fps: int = 8):
    def __init__(self, parent: QWidget, z_len: int, s_len: Optional[int] = None, default_fps: int = 8):
        super().__init__(parent)
        self.setWindowTitle("fv: Image Selection")
        self._z_len = int(z_len)
        self._s_len = int(s_len) if s_len is not None else None

        vbox = QVBoxLayout(self)

        banner = QLabel(
            f"The 4D image contains {self._s_len} data cube(s), each with {self._z_len} slices"
            if self._s_len is not None else
            f"The 3D image contains {self._z_len} slices"
        )
        vbox.addWidget(banner)

        grid = QGridLayout()
        row = 0
        if self._s_len is not None:
            grid.addWidget(QLabel("Data Cube"), row, 0)
            self.cube_spin = QSpinBox()
            self.cube_spin.setRange(1, max(1, self._s_len))
            self.cube_spin.setValue(1)
            grid.addWidget(self.cube_spin, row, 1)
            row += 1
        else:
            self.cube_spin = None  # not shown

        grid.addWidget(QLabel("Start"), row, 0)
        self.start_spin = QSpinBox()
        self.start_spin.setRange(1, max(1, self._z_len))
        self.start_spin.setValue(1)
        grid.addWidget(self.start_spin, row, 1)

        grid.addWidget(QLabel("End"), row, 2)
        self.end_spin = QSpinBox()
        self.end_spin.setRange(1, max(1, self._z_len))
        self.end_spin.setValue(self._z_len)
        grid.addWidget(self.end_spin, row, 3)
        row += 1

        grid.addWidget(QLabel("FPS"), row, 0)
        self.fps_spin = QSpinBox()
        self.fps_spin.setRange(1, 60)
        self.fps_spin.setValue(default_fps)
        grid.addWidget(self.fps_spin, row, 1)

        vbox.addLayout(grid)

        btns = QDialogButtonBox()
        self.btn_ok = btns.addButton("Animate", QDialogButtonBox.ButtonRole.AcceptRole)
        self.btn_cancel = btns.addButton(QDialogButtonBox.StandardButton.Cancel)
        self.btn_help = QPushButton("Help")
        btns.addButton(self.btn_help, QDialogButtonBox.ButtonRole.HelpRole)
        vbox.addWidget(btns)

        self.btn_ok.clicked.connect(self._accept)
        self.btn_cancel.clicked.connect(self.reject)
        self.btn_help.clicked.connect(self._help)

    def _help(self):
        QMessageBox.information(self, "Help",
            "Select a 1-based slice range (Start..End) to animate through z.\n"
            "If the image is 4D, also pick the Data Cube index (S).\n"
            "FPS controls playback speed.")

    def _accept(self):
        if self.end_spin.value() < self.start_spin.value():
            QMessageBox.critical(self, "Range error", "End must be ≥ Start.")
            return
        self.accept()

    def values(self):
        cube = int(self.cube_spin.value()) if self.cube_spin is not None else 1
        return cube, int(self.start_spin.value()), int(self.end_spin.value()), int(self.fps_spin.value())

class SlicePlayerDialog(QDialog):
    """
    Simple slice player that animates z across a 3D (z,y,x) or 4D (S,z,y,x) array.
    Shows a grayscale view with min-max autoscaling per frame.
    """
    # def __init__(self, parent: QWidget, arr: np.ndarray, cube_1based: int = 1, start_1based: int = 1, end_1based: int | None = None, fps: int = 8, title: str | None = None):
    def __init__(self, parent: QWidget, arr: np.ndarray, cube_1based: int = 1, start_1based: int = 1, end_1based: Optional[int] = None, fps: int = 8, title: Optional[str] = None):

        super().__init__(parent)
        self.setWindowTitle(title or "FV: Image")
        self.arr = np.asarray(arr)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self._step)
        self.setMinimumSize(640, 480)

        # Normalize to (z,y,x)
        if self.arr.ndim == 2:
            self.z_stack = self.arr[np.newaxis, :, :]   # shape (1,y,x)
        elif self.arr.ndim == 3:
            self.z_stack = self.arr                     # shape (z,y,x)
        elif self.arr.ndim == 4:
            s = max(1, cube_1based) - 1
            s = np.clip(s, 0, self.arr.shape[0]-1)
            self.z_stack = self.arr[s]                  # shape (z,y,x)
        else:
            raise ValueError(f"Unsupported ndim={self.arr.ndim}")

        self.z_len = self.z_stack.shape[0]
        self.z0 = np.clip((start_1based - 1), 0, self.z_len - 1)
        if end_1based is None:
            end_1based = self.z_len
        self.z1 = np.clip((end_1based - 1), self.z0, self.z_len - 1)
        self.z = self.z0

        self.ms = max(1, int(1000 / max(1, fps)))

        # UI
        vbox = QVBoxLayout(self)
        top = QHBoxLayout()
        self.status = QLabel(self._status_text())
        top.addWidget(self.status, 1)
        self.btn_play = QPushButton("Play");  self.btn_play.clicked.connect(self.play)
        self.btn_pause = QPushButton("Pause"); self.btn_pause.clicked.connect(self.pause)
        top.addWidget(self.btn_play); top.addWidget(self.btn_pause)
        vbox.addLayout(top)

        self.image_lbl = QLabel(); self.image_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(self.image_lbl, 1)

        self._render_current()

        # keyboard shortcuts
        self.btn_play.setAutoDefault(False)
        self.btn_pause.setAutoDefault(False)
        self.image_lbl.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

    def _status_text(self):
        return f"Slice {self.z+1} of {self.z_len}  (range {self.z0+1}–{self.z1+1})"

    def _normalize_to_uint8(self, plane: np.ndarray) -> np.ndarray:
        a = plane.astype(np.float32)
        mn = np.nanmin(a); mx = np.nanmax(a)
        if not np.isfinite(mn) or not np.isfinite(mx) or mx <= mn:
            return np.zeros_like(a, dtype=np.uint8)
        return ((a - mn) / (mx - mn) * 255.0).astype(np.uint8)

    def _render_current(self):
        plane = self.z_stack[self.z, :, :]
        img8 = self._normalize_to_uint8(plane)
        h, w = img8.shape
        qimg = QImage(img8.data, w, h, w, QImage.Format.Format_Grayscale8)
        self.image_lbl.setPixmap(QPixmap.fromImage(qimg).scaled(
            self.image_lbl.size() if self.image_lbl.size().width() > 0 else qimg.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation))
        self.status.setText(self._status_text())

    def resizeEvent(self, ev):
        super().resizeEvent(ev)
        self._render_current()

    def _step(self):
        self.z += 1
        if self.z > self.z1:
            self.z = self.z0
        self._render_current()

    def play(self):
        self.timer.start(self.ms)

    def pause(self):
        self.timer.stop()


def open_image_or_animate(parent: QWidget, fits_path: str, hdu_index: int = 0):
    """
    Open the file in the full FITSViewer. For 2D, 3D, or 4D images the viewer
    will handle rendering and (for >2D) will enable the embedded slice/animation
    panel. No external dialog windows are used.
    """
    try:
        # We still peek the HDU to set a nicer title suffix, but we don't spawn dialogs.
        with fits.open(fits_path, memmap=True) as hdul:
            hdu = hdul[hdu_index] if (0 <= hdu_index < len(hdul)) else hdul[0]
            data = hdu.data
            title_suffix = ""
            if data is not None:
                arr = np.asarray(data)
                if arr.ndim == 3:
                    title_suffix = " [3D]"
                elif arr.ndim == 4:
                    title_suffix = " [4D]"
                elif arr.ndim == 2:
                    title_suffix = ""
        viewer = FITSViewer(fits_path, "image", hdu_index, None, None)
        if title_suffix:
            viewer.image_title_label.setText(f"Image Viewer: {os.path.basename(fits_path)}{title_suffix}")
        viewer.resize(1000, 800)
        viewer.show()
        return
    except Exception as e:
        QMessageBox.critical(parent, "FV error", str(e))


def _sanitize_header_for_wcs(header: "fits.Header") -> "fits.Header":
    """
    Return a copy of the header with common non-standard WCS quirks fixed so Astropy can parse it.
    - Fixes odd CTYPE tokens like 'DECc-SIN' -> 'DEC--SIN', 'RAc-SIN' -> 'RA---SIN'
    - Upper-cases CTYPEs and strips stray spaces
    - Drops/neutralizes known-problematic keywords (VELREF with invalid values)
    """
    h = header.copy()

    # CTYPE normalization
    for i in (1, 2):
        key = f"CTYPE{i}"
        if key in h:
            val = str(h[key]).upper().strip()
            # If this looks like DEC with an extra char (e.g., 'DECC-SIN' or 'DECc-SIN'), normalize
            if val.startswith("DEC") and "SIN" in val:
                val = "DEC--SIN"
            if val.startswith("RA") and "SIN" in val:
                # RA typically has three dashes before projection code
                val = "RA---SIN"
            # Common TAN fallback
            if val.startswith("DEC") and "TAN" in val and "---" not in val and "--" not in val:
                val = "DEC--TAN"
            if val.startswith("RA") and "TAN" in val and "---" not in val:
                val = "RA---TAN"
            h[key] = val

    # Some files have invalid or legacy velocity reference codes that trip WCS parsing.
    # If present and invalid, drop it.
    for bad_key in ("VELREF", "CTYPE3"):
        if bad_key in h:
            try:
                if bad_key == "VELREF":
                    v = int(h[bad_key])
                    if v not in (0, 1, 2, 3, 4, 256, 257, 258, 259):  # typical valid set
                        del h[bad_key]
                elif bad_key == "CTYPE3" and not str(h[bad_key]).strip():
                    del h[bad_key]
            except Exception:
                # if unparsable, delete
                try:
                    del h[bad_key]
                except Exception:
                    pass
    return h
class FITSViewer(QMainWindow):
    def __init__(self, fits_file, mode="image", hdu_index=0, col_x=None, col_y=None):
        super().__init__()
        self.fits_file = fits_file
        self.mode = mode
        self.hdu_index = hdu_index
        self.col_x = col_x
        self.col_y = col_y

        fits_filename = os.path.abspath(self.fits_file)
        self.current_fits_path = fits_filename

        # Track whether axes are flipped
        self.x_flipped = False
        self.y_flipped = False

        self.current_cmap = 'gray'
        self.show_colorbar = True

        self.setWindowTitle("POW")
        #self.setGeometry(100, 100, 1300, 800)
        #self.resize(1100, 720)
        self.resize(1100, 720)

        self.cmap_reversed = False

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QHBoxLayout(self.central_widget)
        self.splitter = QSplitter(Qt.Orientation.Horizontal)
        self.splitter.setSizes([800, 500])
        self.main_layout.addWidget(self.splitter)

        self.left_widget = QWidget()
        self.right_widget = QWidget()
        self.left_layout = QVBoxLayout(self.left_widget)
        self.right_layout = QVBoxLayout(self.right_widget)
        self.splitter.addWidget(self.left_widget)
        self.splitter.addWidget(self.right_widget)

        open_action = QAction("Open FITS File", self)
        open_action.triggered.connect(self.open_file)
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")
        file_menu.addAction(open_action)

        self.image_figure = Figure(figsize=(9,7))
        self.image_title_label = QLabel()
        self.image_canvas = FigureCanvas(self.image_figure)

        self.gs = gridspec.GridSpec(2, 2, height_ratios=[1, 3], width_ratios=[20, 1])
        if self.mode == "image":
            self.gs = gridspec.GridSpec(2, 2, height_ratios=[1, 3], width_ratios=[20, 1])
            self.hist_ax = self.image_figure.add_subplot(self.gs[0, :])
            self.img_ax = self.image_figure.add_subplot(self.gs[1, 0])
            self.colorbar_ax = self.image_figure.add_subplot(self.gs[1, 1])

        else:  # mode == "plot"
            self.img_ax = self.image_figure.add_subplot(111)

        self.colorbar = None

        policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        self.image_canvas.setSizePolicy(policy)
        self.image_canvas.setMinimumSize(800, 600)
        self.image_canvas.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.image_canvas.setFocus()

        # Create the tracker figure and canvas
        self.zoom_fig = Figure(figsize=(1.5, 1.5))  # Logical size in inches for rendering quality
        self.zoom_canvas = FigureCanvas(self.zoom_fig)
        self.zoom_ax = self.zoom_fig.add_subplot(111)
        self.zoom_ax.set_title("Tracker")
        self.zoom_ax.axis("off")

        # Create a 50x50 black RGB image with a yellow border
        blank_zoom = np.zeros((50, 50, 3))
        blank_zoom[0, :, :] = [1, 1, 0]       # Top border
        blank_zoom[-1, :, :] = [1, 1, 0]      # Bottom border
        blank_zoom[:, 0, :] = [1, 1, 0]       # Left border
        blank_zoom[:, -1, :] = [1, 1, 0]      # Right border

        # Display the initial image
        self.zoom_ax.imshow(blank_zoom, origin='lower')
        self.zoom_fig.tight_layout()
        self.zoom_canvas.draw()

        # Set fixed size and policies for layout control
        self.zoom_canvas.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed))
        self.zoom_canvas.setFixedSize(160, 160)
        self.zoom_canvas.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.zoom_canvas.setFocus()

        self.exit_btn = QPushButton("Exit")
        self.exit_btn.clicked.connect(QtWidgets.QApplication.quit)
        self.exit_btn.setFixedWidth(80)
        self.exit_btn.clicked.connect(sys.exit)
        
        self.exit_btn.setStyleSheet("""
            QPushButton {
                background-color: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1,
                    stop:0 #ff5c5c, stop:1 #cc0000
                );
                color: white;
                font-weight: bold;
                border: 1px solid #a00000;
                border-radius: 10px;
                padding: 6px 14px;
            }
        
            QPushButton:hover {
                background-color: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1,
                    stop:0 #ff7b7b, stop:1 #cc0000
                );
            }
        
            QPushButton:pressed {
                background-color: qlineargradient(
            x1:0, y1:0, x2:0, y2:1,
            stop:0 #cc0000, stop:1 #a00000
        );
        border-style: inset;
    }
""")

        exit_row = QHBoxLayout()
        grid_empty_label = QLabel("    ")
        exit_row.addWidget(grid_empty_label)
        exit_row.addWidget(self.exit_btn)

        exit_row_widget = QWidget()
        exit_row_widget.setLayout(exit_row)
        self.right_layout.addWidget(exit_row_widget)

        self.wcs_checkbox = QCheckBox("Display WCS Coordinates")
        self.wcs_checkbox.setChecked(True)
        self.wcs_checkbox.stateChanged.connect(self.show_image)
        self.right_layout.addWidget(self.wcs_checkbox)

        grid_empty_label = QLabel("    ")
        self.right_layout.addWidget(grid_empty_label)

        self.grid_checkbox = QCheckBox("Show Grid Lines")
        self.grid_checkbox.stateChanged.connect(self.show_image)
        self.grid_checkbox.setChecked(False)
        self.right_layout.addWidget(self.grid_checkbox)

        grid_empty_label = QLabel("    ")
        self.right_layout.addWidget(grid_empty_label)

        self.image_canvas.mpl_connect("motion_notify_event", self.show_pixel_value)
        #self.image_canvas.mpl_connect("button_press_event", self.pan_start)
        #self.image_canvas.mpl_connect("motion_notify_event", self.pan_move)
        self.image_canvas.mpl_connect("motion_notify_event", self.update_zoom)

        self._pan_start_pos = None

        self.pixel_label = QLabel("Pixel: ")

        self.pixel_xy_box = QLineEdit()
        self.pixel_xy_box.setReadOnly(True)
        self.pixel_xy_box.setFixedWidth(100)
        self.pixel_xy_box.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
    
        # WCS labels as QLabel (fixed size)
        self.wcs_x_label = QLabel("    ")
        self.wcs_x_label.setStyleSheet("color: red;")

        self.wcs_y_label = QLabel("    ")
        self.wcs_y_label.setStyleSheet("color: red;")

        self.wcs_space_label = QLabel("    ")
        self.wcs_x_label.setFixedWidth(50)
        self.wcs_x_label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.wcs_y_label.setFixedWidth(50)
        self.wcs_y_label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
    
        # WCS value boxes
        self.wcs_x_value_box = QLineEdit()
        self.wcs_y_value_box = QLineEdit()
        for box in [self.wcs_x_value_box, self.wcs_y_value_box]:
            box.setReadOnly(True)
            box.setFixedWidth(100)
    
        # Pixel value box
        self.pixel_value_box = QLineEdit()
        self.pixel_value_box.setReadOnly(True)
        self.pixel_value_box.setFixedWidth(100)
    
        # Layout
        self.pixel_layout = QHBoxLayout()
        self.pixel_layout.setContentsMargins(0, 5, 0, 5)
        self.pixel_layout.setSpacing(2)
        self.pixel_layout.addWidget(QLabel("Pixel Location (X, Y):"))
        self.pixel_layout.addWidget(self.pixel_xy_box)

        #  Wrap the layout in a QWidget
        self.pixel_widget = QWidget()
        self.pixel_widget.setLayout(self.pixel_layout)

        self.wcs_layout = QHBoxLayout()
        self.wcs_layout.setContentsMargins(20, 5, 0, 5)
        self.wcs_layout.setSpacing(4)
        self.wcs_layout.addWidget(QLabel("WCS:"))
        self.wcs_layout.addWidget(self.wcs_x_label)
        self.wcs_layout.addWidget(self.wcs_x_value_box)
        self.wcs_layout.addWidget(self.wcs_space_label)
        self.wcs_layout.addWidget(self.wcs_y_label)
        self.wcs_layout.addWidget(self.wcs_y_value_box)

        #  Wrap the layout in a QWidget
        self.wcs_widget = QWidget()
        self.wcs_widget.setLayout(self.wcs_layout)

        self.value_layout = QHBoxLayout()
        self.value_layout.setContentsMargins(50, 5, 50, 5)
        self.value_layout.setSpacing(2)
        self.value_layout.addWidget(QLabel("Pixel Value:"))
        self.value_layout.addWidget(self.pixel_value_box)
    
        #  Wrap the layout in a QWidget
        self.value_widget = QWidget()
        self.value_widget.setLayout(self.value_layout)

        self.contrast_slider = QSlider(Qt.Orientation.Horizontal)
        self.contrast_label = QLabel("Contrast Level 0%")
        self.contrast_slider.setRange(0, 100)
        self.contrast_slider.setValue(0)
        self.contrast_slider.valueChanged.connect(self.update_contrast)

        self.slider_layout = QVBoxLayout()
        self.slider_layout.addWidget(self.contrast_label)
        self.slider_layout.addWidget(self.contrast_slider)

        #  Wrap the layout in a QWidget
        self.slider_widget = QWidget()
        self.slider_widget.setLayout(self.slider_layout)

        self.contrast_slider.setMinimumWidth(200)
        self.slider_widget.setFixedWidth(250)  # or adjust as needed

        layout = QHBoxLayout()
        layout.addWidget(self.pixel_widget)
        layout.addWidget(self.wcs_widget)
        layout.addWidget(self.value_widget)
        layout.addWidget(self.slider_widget)

        container = QWidget()
        container.setLayout(layout)
        container.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.ds9_button = QPushButton("Send to DS9")
        self.ds9_button.clicked.connect(self.send_to_ds9)

        self.cmap_label = QLabel("Colormap:")

        self.cmap_combo = QComboBox()
        self.cmap_combo.addItems(["gray", "viridis", "plasma", "magma", "cividis", "hot", "cool"])
        self.cmap_combo.currentTextChanged.connect(self.update_colormap)

        self.invert_cmap_btn = QPushButton("Invert")
        self.invert_cmap_btn.clicked.connect(self.toggle_cmap_invert)

        self.toggle_cmap_btn = QPushButton("Hide Colormap")
        self.toggle_cmap_btn.clicked.connect(self.toggle_colorbar)

        self.scale_controls = QHBoxLayout()

        self.scaling_label = QLabel("Scaling:")
        self.scale_combo = QComboBox()
        #self.scale_combo.addItems(["Linear", "Logarithmic", "Square Root"])

        self.scale_combo.addItems([
            "Linear", 
            "Logarithmic", 
            "Square Root", 
            "Asinh", 
            #"Histogram Equalization", 
            #"ZScale", 
            #"Percentile (1–99%)"
        ])

        self.scale_combo.currentIndexChanged.connect(self.show_image)
        self.scale_controls.addWidget(self.scale_combo)

        self.view_label = QLabel("View:")

        self.zoom_in_btn = QPushButton("Zoom In")
        self.zoom_out_btn = QPushButton("Zoom Out")
        self.zoom_reset_btn = QPushButton("Reset Zoom")
        self.invert_x_axis_btn = QPushButton("Invert X Axis")
        self.invert_y_axis_btn = QPushButton("Invert Y Axis")
        self.invert_both_axis_btn = QPushButton("Invert Both Axis")
        self.undo_invert_axis_btn = QPushButton("Undo Invert")

        self.zoom_in_btn.clicked.connect(lambda: self.zoom(1.2))
        self.zoom_out_btn.clicked.connect(lambda: self.zoom(0.8))
        self.zoom_reset_btn.clicked.connect(self.reset_zoom)
        self.invert_x_axis_btn.clicked.connect(lambda: self.invert_axis('x'))
        self.invert_y_axis_btn.clicked.connect(lambda: self.invert_axis('y'))
        self.invert_both_axis_btn.clicked.connect(lambda: self.invert_axis('b'))
        self.undo_invert_axis_btn.clicked.connect(lambda: self.invert_axis('u'))

        #self.hist_canvas = FigureCanvas(Figure(figsize=(4.5, 3)))
        self.hist_canvas = FigureCanvas(Figure(figsize=(3, 2)))
        self.hist_ax = self.hist_canvas.figure.subplots()
        self.hist_canvas.figure.subplots_adjust(left=0.15)
        self.hist_canvas.setMinimumWidth(300)
        self.hist_canvas.setMinimumHeight(100)

        self.left_layout.addWidget(self.image_title_label)

        #self.img_layout = QHBoxLayout()
        #self.img_layout.addWidget(self.image_canvas)
        #self.img_layout.addWidget(self.zoom_canvas)

        # Create a container widget to hold the image layout
        #image_container = QWidget()
        #image_container.setLayout(self.img_layout)

        # Now add the container to the left layout
        #self.left_layout.addWidget(image_container)

        self.left_layout.addWidget(self.image_canvas)

        # Add it next to the main canvas (adjust layout as needed)
        #self.left_layout.addWidget(self.zoom_canvas, stretch=1)

        self.toolbar = NavigationToolbar(self.image_canvas, self)
        self.toolbar.setStyleSheet("QToolBar { icon-size: 16px; }")  # or 12px, 14px etc.
        self.left_layout.addWidget(self.toolbar)

        #self.left_layout.addWidget(NavigationToolbar(self.image_canvas, self))

        # self.left_layout.addWidget(self.pixel_label)
        self.left_layout.addWidget(container)  # Add to main layout

        self.ds9_empty_label = QLabel("    ")

        ds9_row = QHBoxLayout()
        ds9_row.addWidget(self.ds9_button)
        ds9_row.addWidget(self.ds9_empty_label)
        
        ds9_row_widget = QWidget()
        ds9_row_widget.setLayout(ds9_row)

        cmap_row_1 = QHBoxLayout()
        cmap_row_1.addWidget(self.cmap_combo)
        cmap_row_1.addWidget(self.invert_cmap_btn)
        cmap_row_1_widget = QWidget()
        cmap_row_1_widget.setLayout(cmap_row_1)

        cmap_row_2 = QHBoxLayout()

        # Wrap the layout in a QWidget
        self.scale_controls_widget = QWidget()
        self.scale_controls_widget.setLayout(self.scale_controls)

        cmap_row_2.addWidget(self.scale_controls_widget)
        cmap_row_2.addWidget(self.toggle_cmap_btn)
        cmap_row_2_widget = QWidget()
        cmap_row_2_widget.setLayout(cmap_row_2)

        zoom_row = QHBoxLayout()
        zoom_row.addWidget(self.zoom_in_btn)
        zoom_row.addWidget(self.zoom_out_btn)
        zoom_row.addWidget(self.zoom_reset_btn)

        zoom_row_widget = QWidget()
        zoom_row_widget.setLayout(zoom_row)

        invert_row_1 = QHBoxLayout()
        invert_row_1.addWidget(self.invert_x_axis_btn)
        invert_row_1.addWidget(self.invert_y_axis_btn)
        invert_row_2 = QHBoxLayout()
        invert_row_2.addWidget(self.invert_both_axis_btn)
        invert_row_2.addWidget(self.undo_invert_axis_btn)

        invert_row_1_widget = QWidget()
        invert_row_1_widget.setLayout(invert_row_1)

        invert_row_2_widget = QWidget()
        invert_row_2_widget.setLayout(invert_row_2)

        grid_empty_top_label = QLabel("    ")
        grid_empty_label = QLabel("    ")
        grid_histogram_label = QLabel("Histogram:") 

        # --- Plot Style (for 1D plots) ---------------------------------------------
        # --- 1D plot state (for Plot mode) ---
        self.plot_x = None
        self.plot_y = None
        self._plot_line = None
        self._plot_style_ready = False

        self.plot_style_label = QLabel("Plot Style:")

        self.line_color_combo = QComboBox()
        self.line_color_combo.addItems(
            ["blue", "red", "green", "orange", "purple", "black", "gray", "cyan", "magenta", "None"]
        )
        self.line_color_combo.currentTextChanged.connect(self.update_plot_style)

        self.marker_symbol_combo = QComboBox()
        self.marker_symbol_combo.addItems(
            ["None", "o", "+", "x", "s", "^", "v", "*", "D", "P"]
        )
        self.marker_symbol_combo.currentTextChanged.connect(self.update_plot_style)
        
        self.marker_color_combo = QComboBox()
        self.marker_color_combo.addItems(
            ["red", "blue", "green", "orange", "purple", "black", "gray", "cyan", "magenta"]
        )
        self.marker_color_combo.currentTextChanged.connect(self.update_plot_style)

        plot_row_1 = QHBoxLayout()
        plot_row_1.addWidget(QLabel("Line"))
        plot_row_1.addWidget(self.line_color_combo)
        self.plot_row_1_widget = QWidget()
        self.plot_row_1_widget.setLayout(plot_row_1)

        plot_row_2 = QHBoxLayout()
        plot_row_2.addWidget(QLabel("Marker"))
        plot_row_2.addWidget(self.marker_symbol_combo)
        plot_row_2.addWidget(QLabel("Color"))
        plot_row_2.addWidget(self.marker_color_combo)
        self.plot_row_2_widget = QWidget()
        self.plot_row_2_widget.setLayout(plot_row_2)
        # ---------------------------------------------------------------------------

        for widget in [
            self.zoom_canvas,
            ds9_row_widget,
            self.cmap_label, 
            cmap_row_1_widget,
            self.scaling_label, 
            cmap_row_2_widget,
            self.view_label, 
            zoom_row_widget,
            invert_row_1_widget,
            invert_row_2_widget,
            self.plot_style_label,
            self.plot_row_1_widget,
            self.plot_row_2_widget,
            grid_empty_top_label, 
            grid_histogram_label,
            grid_empty_label, 
            self.hist_canvas,
        ]:
            self.right_layout.addWidget(widget)
        
        # Hide plot-style widgets by default; shown when in Plot mode
        self.plot_style_label.setVisible(False)
        self.plot_row_1_widget.setVisible(False)
        self.plot_row_2_widget.setVisible(False)

        # ---- Slices / Animation panel (hidden unless a 3D/4D cube is loaded) ----
        self.slice_panel = QGroupBox("Slices / Animation")
        slice_layout = QVBoxLayout(self.slice_panel)

        # Info label: "Slice i of N (range a–b)"
        self.slice_info_label = QLabel("")
        slice_layout.addWidget(self.slice_info_label)

        # Data Cube selector (for 4D only; hidden for 2D/3D)
        cube_row = QHBoxLayout()
        cube_row.addWidget(QLabel("Data Cube:"))
        self.cube_spin = QSpinBox()
        self.cube_spin.setRange(1, 1)
        self.cube_spin.setValue(1)
        self.cube_spin.valueChanged.connect(self._on_cube_changed)
        cube_row.addWidget(self.cube_spin)
        cube_row_widget = QWidget()
        cube_row_widget.setLayout(cube_row)
        slice_layout.addWidget(cube_row_widget)

        # Slider row
        self.slice_slider = QSlider(Qt.Orientation.Horizontal)
        self.slice_slider.setRange(1, 1)
        self.slice_slider.setValue(1)
        self.slice_slider.valueChanged.connect(self._on_slider_changed)
        slice_layout.addWidget(self.slice_slider)

        # Start / End / FPS row
        se_row = QHBoxLayout()
        se_row.addWidget(QLabel("Start"))
        self.slice_start = QSpinBox()
        self.slice_start.setRange(1, 1)
        self.slice_start.setValue(1)
        self.slice_start.valueChanged.connect(self._on_range_changed)
        se_row.addWidget(self.slice_start)

        se_row.addWidget(QLabel("End"))
        self.slice_end = QSpinBox()
        self.slice_end.setRange(1, 1)
        self.slice_end.setValue(1)
        self.slice_end.valueChanged.connect(self._on_range_changed)
        se_row.addWidget(self.slice_end)

        se_row.addWidget(QLabel("FPS"))
        self.slice_fps = QSpinBox()
        self.slice_fps.setRange(1, 60)
        self.slice_fps.setValue(8)
        self.slice_fps.valueChanged.connect(self._on_fps_changed)
        se_row.addWidget(self.slice_fps)

        se_row_widget = QWidget()
        se_row_widget.setLayout(se_row)
        slice_layout.addWidget(se_row_widget)

        # Play/Pause row
        pp_row = QHBoxLayout()
        self.slice_play_btn = QPushButton("Play")
        self.slice_play_btn.clicked.connect(self._play_slices)
        self.slice_pause_btn = QPushButton("Pause")
        self.slice_pause_btn.clicked.connect(self._pause_slices)
        pp_row.addWidget(self.slice_play_btn)
        pp_row.addWidget(self.slice_pause_btn)
        pp_row_widget = QWidget()
        pp_row_widget.setLayout(pp_row)
        slice_layout.addWidget(pp_row_widget)

        # Hide by default; only show when 3D/4D data is loaded
        self.slice_panel.setVisible(False)
        self.right_layout.addWidget(self.slice_panel)

        # Timer for animation
        self.slice_timer = QTimer(self)
        self.slice_timer.timeout.connect(self._advance_slice)

        # Data holders for stacks
        self._stack_4d = None     # shape (S,Z,Y,X) or None
        self._stack_3d = None     # shape (Z,Y,X) or None
        self._Z = 0               # slices per cube
        self._S = 0               # number of cubes (for 4D)
        self._cur_s = 0           # current cube index (0-based)
        self._cur_z = 0           # current slice index (0-based)
        self._range_start = 0     # 0-based inclusive
        self._range_end = 0       # 0-based inclusive
        self.right_layout.addStretch()

        self.right_layout.setSpacing(0)      # reduce space between widgets (default is usually 6–10)
        self.right_layout.setContentsMargins(0, 0, 0, 0)  # remove outer padding

        self.current_fits_path = None
        self.image_wcs = None
        self.image_data = None
        self.image_header = None
        self.current_zoom = 1.0
        self.ds9_path = os.environ["DS9_PATH"]
        self.ds9_target_name = "pyqt_ds9"
        self.ds9_launched = False
        self.min_val = 0
        self.max_val = 0
        self.org_min_val = 0
        self.org_max_val = 0

        self.check_dependencies()

        # Load FITS file
        self.load_file(fits_filename)

        if self.mode == "plot":
           self.invert_x_axis_btn.setVisible(False)
           self.invert_y_axis_btn.setVisible(False)
           self.invert_both_axis_btn.setVisible(False)
           self.undo_invert_axis_btn.setVisible(False)
           self.wcs_checkbox.setVisible(False)
           self.grid_checkbox.setVisible(False)
           self.cmap_label.setVisible(False)
           self.cmap_combo.setVisible(False)
           self.scaling_label.setVisible(False)
           self.toggle_cmap_btn.setVisible(False)

           grid_histogram_label.setVisible(False)
           self.ds9_button.setVisible(False)
           self.invert_cmap_btn.setVisible(False)

           self.zoom_canvas.setVisible(False)
           self.hist_canvas.setVisible(False)
           self.scale_controls_widget.setVisible(False)
           self.pixel_widget.setVisible(False)
           self.wcs_widget.setVisible(False)
           self.value_widget.setVisible(False)
           self.slider_widget.setVisible(False)

    # ---- Slice animation helpers ----
    def _configure_slice_panel(self, z_len: int, s_len: Optional[int]):
        """Prepare the slice panel for a 3D/4D stack and show it."""
        self.slice_panel.setVisible(True)
        self.slice_slider.setRange(1, z_len)
        self.slice_slider.setValue(1)

        self.slice_start.setRange(1, z_len)
        self.slice_end.setRange(1, z_len)
        self.slice_start.setValue(1)
        self.slice_end.setValue(z_len)

        self._range_start = 0
        self._range_end = z_len - 1
        self._update_slice_label()

    def _update_slice_label(self):
        n = self._Z if self._Z else 1
        a = self._range_start + 1
        b = self._range_end + 1
        cur = self._cur_z + 1
        if self._stack_4d is not None:
            self.slice_info_label.setText(f"Slice {cur} of {n}  (range {a}–{b})   Cube {self._cur_s+1} of {self._S}")
        else:
            self.slice_info_label.setText(f"Slice {cur} of {n}  (range {a}–{b})")

    def _current_stack_slice(self):
        """Return the 2D array for the current cube/slice selection."""
        if self._stack_3d is not None:
            return self._stack_3d[self._cur_z]
        if self._stack_4d is not None:
            return self._stack_4d[self._cur_s, self._cur_z]
        return None

    def _update_frame_from_stack(self):
        frame = self._current_stack_slice()
        if frame is None:
            return
        self.image_data = frame  # 2D array
        self.show_image()        # reuse full viewer rendering
        self.show_histogram()
        self._update_slice_label()

    def _on_slider_changed(self, val: int):
        self._cur_z = max(0, min(self._Z - 1, int(val) - 1))
        self._update_frame_from_stack()

    def _on_range_changed(self):
        s = int(self.slice_start.value()) - 1
        e = int(self.slice_end.value()) - 1
        if e < s:
            e = s
            self.slice_end.setValue(e + 1)
        self._range_start, self._range_end = s, e
        self._update_slice_label()

    def _on_fps_changed(self):
        fps = int(self.slice_fps.value())
        fps = max(1, min(60, fps))
        self.slice_timer.setInterval(int(1000 / fps))

    def _on_cube_changed(self, val: int):
        self._cur_s = max(0, min(self._S - 1, int(val) - 1))
        self._update_frame_from_stack()

    def _advance_slice(self):
        if self._Z <= 0:
            return
        z = self._cur_z + 1
        if z > self._range_end:
            z = self._range_start
        self._cur_z = z
        # Keep the UI slider in sync without sending another signal loop
        self.slice_slider.blockSignals(True)
        self.slice_slider.setValue(self._cur_z + 1)
        self.slice_slider.blockSignals(False)
        self._update_frame_from_stack()

    def _play_slices(self):
        self._on_fps_changed()
        self.slice_timer.start()

    def _pause_slices(self):
        self.slice_timer.stop()


    def toggle_cmap_invert(self):
        self.cmap_reversed = not self.cmap_reversed
        self.update_colormap()

    def toggle_colorbar(self):
        self.show_colorbar = not self.show_colorbar
        self.toggle_cmap_btn.setText("Hide Colormap" if self.show_colorbar else "Show Colormap")
        self.show_image()
        
    def parse_msg_and_update_boxes(self, msg):
        try:
            # Extract pixel coordinates
            pixel_match = re.search(r"Pixel:\s*\((\d+),\s*(\d+)\)", msg)
            x, y = int(pixel_match.group(1)), int(pixel_match.group(2)) if pixel_match else (None, None)
    
            # Extract WCS info (optional)
            wcs_match = re.search(r"\|\s*(\w+):\s*([-+]?[\d\.]+),\s*(\w+):\s*([-+]?[\d\.]+)", msg)
            if wcs_match:
                x_label = wcs_match.group(1)
                x_val = float(wcs_match.group(2))
                y_label = wcs_match.group(3)
                y_val = float(wcs_match.group(4))
                wcs_info = (x_label, x_val, y_label, y_val)
            else:
                wcs_info = None
    
            # Extract pixel value
            val_match = re.search(r"=\s*([-+]?[\d\.]+)", msg)
            pixel_val = float(val_match.group(1)) if val_match else None
    
            self.update_pixel_info_boxes(x, y, wcs_info, pixel_val)
    
        except Exception as e:
            print(f"Failed to parse msg: {e}")

    def update_pixel_info_boxes(self, x, y, wcs_info=None, pixel_val=None):
        self.pixel_xy_box.setText(f"({x}, {y})")
    
        if wcs_info:
            x_label, x_val, y_label, y_val = wcs_info
            self.wcs_x_label.setText(x_label[:6].ljust(6))
            self.wcs_y_label.setText(y_label[:6].ljust(6))

            # Assuming x_val is in degrees
            x_angle = Angle(x_val, unit='deg')
            h, m, s = x_angle.hms  # hours, minutes, seconds as floats
            x_str = f"{int(h)}h{int(m)}m{abs(s):05.2f}s"
            self.wcs_x_value_box.setText(x_str)

            y_angle = Angle(y_val, unit='deg')
            sign = '-' if y_angle.deg < 0 else ''
            d, m, s = y_angle.dms  # Get raw dms values (can be negative)
            d, m, s = abs(d), abs(m), abs(s)  # Apply abs to each component
            y_str = f"{sign}{int(d)}°{int(m)}'{abs(s):05.2f}\""
            self.wcs_y_value_box.setText(y_str)

            #self.wcs_x_value_box.setText(f"{x_val:.6f}")
            #self.wcs_y_value_box.setText(f"{y_val:.6f}")
        else:
            self.wcs_x_label.clear()
            self.wcs_x_value_box.clear()
            self.wcs_y_label.clear()
            self.wcs_y_value_box.clear()
    
        if pixel_val is not None:
            self.pixel_value_box.setText(f"{pixel_val:.2f}")
        else:
            self.pixel_value_box.clear()

    def update_pixel_info_boxes_A(self, x, y, wcs_info=None, pixel_val=None):
        self.pixel_x_box.setText(str(x))
        self.pixel_y_box.setText(str(y))
    
        if wcs_info:
            x_label, x_val, y_label, y_val = wcs_info
            self.wcs_x_label_box.setText(x_label)
            self.wcs_x_value_box.setText(f"{x_val:.6f}")
            self.wcs_y_label_box.setText(y_label)
            self.wcs_y_value_box.setText(f"{y_val:.6f}")
        else:
            self.wcs_x_label_box.clear()
            self.wcs_x_value_box.clear()
            self.wcs_y_label_box.clear()
            self.wcs_y_value_box.clear()
    
        if pixel_val is not None:
            self.pixel_value_box.setText(f"{pixel_val:.2f}")
        else:
            self.pixel_value_box.clear()

    def check_dependencies(self):
        if not os.path.exists(self.ds9_path):
            QtWidgets.QMessageBox.critical(self, "DS9 Not Found", "SAOImage DS9 not found in /Applications.")
        if shutil.which("xpaaccess") is None:
            QtWidgets.QMessageBox.critical(self, "XPA Not Found", "'xpaaccess' is not in your PATH.")

    def load_file(self, path):
        if not os.path.exists(path):
            QtWidgets.QMessageBox.critical(self, "Error", f"File not found:\n{path}")
            return
    
        self.current_fits_path = path
    
        try:
            with fits.open(path) as hdul:
                if self.mode == "plot":
                    if self.hdu_index >= len(hdul):
                        QtWidgets.QMessageBox.critical(self, "Error", f"HDU index {self.hdu_index} out of range.")
                        return
    
                    hdu = hdul[self.hdu_index]
                    if not hasattr(hdu, "data") or not hasattr(hdu, "columns"):
                        QtWidgets.QMessageBox.warning(self, "Warning", "Selected HDU is not a table.")
                        return
    
                    if self.col_x not in hdu.columns.names or self.col_y not in hdu.columns.names:
                        QtWidgets.QMessageBox.warning(self, "Warning", f"Columns not found: {self.col_x}, {self.col_y}")
                        return
    
                    # Extract and plot
                    #x = hdu.data[self.col_x]
                    #y = hdu.data[self.col_y]
                    #self.img_ax.clear()
                    #self.hist_ax.clear()
                    #self.img_ax.plot(x, y)
                    #self.img_ax.set_xlabel(self.col_x)
                    #self.img_ax.set_ylabel(self.col_y)
                    #self.img_ax.set_title(f"{os.path.basename(path)}: {self.col_y} vs {self.col_x}")
                    #self.image_title_label.setText(f"Plot Viewer: {os.path.basename(path)}")

                    # Extract and plot
                    x = np.asarray(hdu.data[self.col_x])
                    y = np.asarray(hdu.data[self.col_y])

                    # save for styling
                    self.plot_x = x
                    self.plot_y = y
                    self._plot_style_ready = True
                    self._plot_line = None  # reset when a new table/plot is loaded

                    # draw using current style controls
                    self.img_ax.clear()
                    self.update_plot_style(redraw_axes=False)

                    self.img_ax.set_xlabel(self.col_x)
                    self.img_ax.set_ylabel(self.col_y)
                    self.img_ax.set_title(f"{os.path.basename(path)}: {self.col_y} vs {self.col_x}")
                    self.image_title_label.setText(f"Plot Viewer: {os.path.basename(path)}")
    
                    # Hide unused widgets in plot mode
                    self.zoom_canvas.setVisible(False)
                    self.hist_canvas.setVisible(False)
                    self.scale_controls_widget.setVisible(False)
                    self.pixel_widget.setVisible(False)
                    self.wcs_widget.setVisible(False)
                    self.value_widget.setVisible(False)
                    self.slider_widget.setVisible(False)
                    self.toolbar.setVisible(True)

                    self.zoom_canvas.setVisible(True)             # Tracker visible for Plot
                    self.plot_style_label.setVisible(True)
                    self.plot_row_1_widget.setVisible(True)
                    self.plot_row_2_widget.setVisible(True)

                    self.image_canvas.draw()
                    return
                # Image mode (2D / 3D / 4D) — embedded viewer only
                found = None
                for hdu in hdul:
                    if getattr(hdu, "data", None) is not None:
                        found = hdu
                        break

                if found is None or found.data is None:
                    QtWidgets.QMessageBox.warning(self, "Warning", "No image data found in FITS file.")
                else:
                    arr = np.asarray(found.data)
                    if arr.ndim == 2:
                        # 2D
                        self.slice_panel.setVisible(False)
                        self._stack_3d = None
                        self._stack_4d = None
                        self.image_data = arr.astype(np.float32)
                        self.image_title_label.setText(f"Image Viewer: {os.path.basename(path)}")
                        self.show_image()
                        self.show_histogram()
                        self.min_val = int(np.min(self.image_data))
                        self.max_val = int(np.max(self.image_data))
                        self.org_min_val = self.min_val
                        self.org_max_val = self.max_val
                        return
                    elif arr.ndim == 3:
                        # 3D
                        self._stack_3d = arr.astype(np.float32)
                        self._stack_4d = None
                        self._S = 1
                        self._Z = self._stack_3d.shape[0]
                        self.cube_spin.setRange(1, 1)
                        self.cube_spin.setValue(1)
                        self.cube_spin.parent().setVisible(False)
                        self._configure_slice_panel(z_len=self._Z)
                        self.image_title_label.setText(f"Image Viewer: {os.path.basename(path)} [3D]")
                        self._cur_z = 0
                        self._update_frame_from_stack()
                        return
                    elif arr.ndim == 4:
                        # 4D
                        self._stack_4d = arr.astype(np.float32)
                        self._stack_3d = None
                        self._S = self._stack_4d.shape[0]
                        self._Z = self._stack_4d.shape[1]
                        self.cube_spin.setRange(1, self._S)
                        self.cube_spin.setValue(1)
                        self.cube_spin.parent().setVisible(True)
                        self._configure_slice_panel(z_len=self._Z, s_len=self._S)
                        self.image_title_label.setText(f"Image Viewer: {os.path.basename(path)} [4D]")
                        self._cur_s = 0
                        self._cur_z = 0
                        self._update_frame_from_stack()
                        return
                    else:
                        QtWidgets.QMessageBox.warning(self, "Warning", f"Unsupported image dimensionality: {arr.ndim}D")
                        return
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to load FITS file:\n{e}")

    def open_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open FITS File", "", "FITS files (*.fits *.fit)")
        if path:
            self.load_file(path)

    def update_zoom(self, event):
        if self.mode != "image":
            return
        if not hasattr(self, 'ax') or self.ax is None:
            return
        if event.inaxes != self.ax or event.xdata is None or event.ydata is None:
            return
    
        zoom_size = 50
        half = zoom_size // 2
        x, y = int(event.xdata), int(event.ydata)
    
        if not hasattr(self, 'image_data') or self.image_data is None:
            print("No image data.")
            return
    
        height, width = self.image_data.shape
        x_min = max(x - half, 0)
        x_max = min(x + half, width)
        y_min = max(y - half, 0)
        y_max = min(y + half, height)
    
        region = self.image_data[y_min:y_max, x_min:x_max]
        insert_y = max(half - y, 0)
        insert_x = max(half - x, 0)
    
        zoomed = np.zeros((zoom_size, zoom_size))
        zoomed[insert_y:insert_y + region.shape[0], insert_x:insert_x + region.shape[1]] = region
    
        vmin = np.nanpercentile(self.image_data, 1)
        vmax = np.nanpercentile(self.image_data, 99)
    
        self.zoom_ax.clear()

        cmap = self.cmap_combo.currentText()

        if self.cmap_reversed:
            cmap += "_r"

        self.zoom_ax.imshow(zoomed, origin='lower', cmap=cmap, vmin=vmin, vmax=vmax)
        # self.zoom_ax.imshow(zoomed, origin='lower', cmap='gray', vmin=vmin, vmax=vmax)
    
        # Add yellow frame using a rectangle
        rect = Rectangle((0, 0), zoom_size - 1, zoom_size - 1,
                         linewidth=1.5, edgecolor='yellow', facecolor='none')
        self.zoom_ax.add_patch(rect)
    
        self.zoom_ax.set_title("Tracker")
        self.zoom_ax.axis("off")
        self.zoom_fig.tight_layout()
        self.zoom_canvas.draw()

        self._last_cursor_position = event

    def send_to_ds9(self):
        try:
            from pyds9 import DS9
        except ImportError:
            print("[FV] pyds9 not installed. Please install it with 'pip install pyds9'")
            return
    
        # Check if DS9 is already running
        ds9_path = self.ds9_path
        ds9_running = subprocess.run(["pgrep", "-x", "ds9"], capture_output=True).returncode == 0
    
        if not ds9_running:
            # print("[FV] DS9 not running — launching it now...")
            try:
                subprocess.Popen([ds9_path])
                time.sleep(2)  # Give DS9 a moment to launch and register with XPA
            except Exception as e:
                print(f"[FV] Failed to launch DS9: {e}")
                return
    
        try:
            d = DS9()
        except Exception as e:
            print(f"[FV] Could not connect to DS9 via XPA: {e}")
            return
    
        if self.image_data is None:
            print("[FV] No image data to send.")
            return
    
        try:
            # Save image to temporary FITS file
            from astropy.io import fits
            import tempfile
    
            tmp_fits_path = os.path.join(tempfile.gettempdir(), "fv_ds9_temp.fits")
            fits.writeto(tmp_fits_path, self.image_data, overwrite=True)
    
            d.set(f"file {tmp_fits_path}")
            # print(f"[FV] Image sent to DS9: {tmp_fits_path}")
        except Exception as e:
            print(f"[FV] Error sending image to DS9: {e}")

    def update_colormap(self):
        self.show_image()
        self.update_zoom_with_last_position()

    def update_zoom_with_last_position(self):
        if hasattr(self, "_last_cursor_position"):
            self.update_zoom(self._last_cursor_position)

    def update_contrast(self):
        if self.image_data is None or self.im is None:
            return

        slider_val = self.contrast_slider.value()
    
        # Apply square root scaling and cap max clip to 5%
        clip_total = (slider_val ** 0.5) * 0.7
        clip_each_side = clip_total / 2

        vmin = np.percentile(self.image_data, clip_each_side)
        vmax = np.percentile(self.image_data, 100 - clip_each_side)

        self.contrast_label.setText(f"Contrasst Level {int(slider_val)}%")
        self.im.set_clim(vmin, vmax)
        self.min_val = vmin
        self.max_val = vmax
        self.image_canvas.draw()

    def apply_scaling(self, image):
        min_val = self.min_val
        max_val = self.max_val

        clipped = np.clip(image, min_val, max_val)
        scale_type = self.scale_combo.currentText()

        clipped = image
        if scale_type == "Linear":
            self.min_val = self.org_min_val
            self.max_val = self.org_max_val
        elif scale_type == "Logarithmic":
            clipped = np.log1p(clipped - min_val)
        elif scale_type == "Square Root":
            clipped = np.sqrt(clipped - min_val)
        elif scale_type == "Asinh":
            clipped = np.arcsinh(clipped - min_val)

        min_val = np.nanmin(clipped)
        max_val = np.nanmax(clipped)
        self.min_val = np.nanmin(clipped)
        self.max_val = np.nanmax(clipped)
        return clipped, min_val, max_val

    def apply_scaling_x(self, data):
        mode = self.scale_combo.currentText()
        data = np.array(data, dtype=np.float32)
        offset = 1e-3  # small offset to avoid log(0)

        if mode == "Linear":
            scaled = data
        elif mode == "Logarithmic":
            scaled = np.log10(data + offset)
        elif mode == "Square Root":
            scaled = np.sqrt(np.clip(data, 0, None))
        else:
            scaled = data

        vmin = np.nanmin(scaled)
        vmax = np.nanmax(scaled)
        return scaled, vmin, vmax

    def show_image(self, vmin=None, vmax=None):
        # Save current view limits if axes exist
        xlim = self.ax.get_xlim() if hasattr(self, 'ax') else None
        ylim = self.ax.get_ylim() if hasattr(self, 'ax') else None
    
        if self.image_data is None:
            return
    
        # Clear and rebuild the figure layout
        self.image_canvas.figure.clf()
        self.image_figure = self.image_canvas.figure
        gs = self.image_figure.add_gridspec(1, 2, width_ratios=[20, 1])
    
        use_wcs = self.wcs_checkbox.isChecked()

        #self.min_val = vmin
        #self.max_val = vmax

        scaled, vmin, vmax = self.apply_scaling(self.image_data)
        #self.image_data = scaled
    
        try:
            if use_wcs:
                with fits.open(self.current_fits_path) as hdul:
                    header = hdul[0].header
                    with warnings.catch_warnings():
                        warnings.simplefilter('ignore', FITSFixedWarning)
                        san = _sanitize_header_for_wcs(header)
                        self.image_wcs = WCS(san, relax=True)
    
                    if self.image_wcs.has_celestial:
                        from astropy.visualization.wcsaxes import WCSAxes
    
                        celestial_wcs = self.image_wcs.celestial
                        ctype1, ctype2 = celestial_wcs.wcs.ctype
                        label_x = ctype1.split('-')[0]
                        label_y = ctype2.split('-')[0]
    
                        self.ax = WCSAxes(self.image_figure, gs[0], celestial_wcs)
                        self.image_figure.add_axes(self.ax)
    
                        if vmin is None or vmax is None:
                            vmin = self.image_data.min()
                            vmax = self.image_data.max()
                        elif vmin > vmax:
                            vmin, vmax = vmax, vmin
    
                        cmap = self.cmap_combo.currentText()
                        if self.cmap_reversed:
                            cmap += "_r"
    
                        self.im = self.ax.imshow(
                            scaled,
                            origin='lower',
                            cmap=cmap,
                            vmin=vmin,
                            vmax=vmax
                        )
    
                        coord1 = self.ax.coords[0]
                        coord2 = self.ax.coords[1]
    
                        coord1.set_major_formatter('hh:mm:ss')
                        coord2.set_major_formatter('dd:mm:ss')
                        coord1.set_separator((u'h', u'm', u's'))
                        coord2.set_separator((u'°', u'′', u'″'))
                        coord1.set_ticklabel(size=9)
                        coord2.set_ticklabel(size=9)
    
                        coord1.set_axislabel(label_x)
                        coord2.set_axislabel(label_y)
                    else:
                        raise ValueError("No valid celestial WCS found.")
            else:
                raise ValueError("WCS display disabled.")
    
        except Exception:
            self.ax = self.image_figure.add_subplot(gs[0])
    
            if vmin is None or vmax is None:
                vmin = self.image_data.min()
                vmax = self.image_data.max()
            elif vmin > vmax:
                vmin, vmax = vmax, vmin
    
            cmap = self.cmap_combo.currentText()
            if self.cmap_reversed:
                cmap += "_r"
    
            self.im = self.ax.imshow(
                scaled,
                origin='lower',
                cmap=cmap,
                vmin=vmin,
                vmax=vmax
            )
    
            self.ax.set_xlabel("X")
            self.ax.set_ylabel("Y")
    
        # Set up colorbar axis and manage display
        self.colorbar_ax = self.image_figure.add_subplot(self.gs[1, 1])
        self.colorbar_ax.axis('off')
    
        #scaled, vmin, vmax = self.apply_scaling(self.image_data)

        if self.show_colorbar:
            self.colorbar = self.image_figure.colorbar(self.im, cax=self.colorbar_ax, orientation='vertical')
            self.colorbar.set_label("Pixel Value (scaled)")
            self.colorbar_ax.axis('on')
        else:
            if self.colorbar:
                self.colorbar_ax.clear()
                self.colorbar = None
            self.colorbar_ax.axis('off')

        self.ax.set_title(os.path.basename(self.current_fits_path))
    
        if self.grid_checkbox.isChecked():
            self.ax.grid(color="white", ls=":", lw=0.5)
    
        try:
            if xlim is not None and ylim is not None:
                self.ax.set_xlim(xlim)
                self.ax.set_ylim(ylim)
            self.ax.xaxis.set_inverted(self.x_flipped)
            self.ax.yaxis.set_inverted(self.y_flipped)
        except Exception as e:
            print(f"[Zoom/pan restore failed] {e}")
    
        self.image_canvas.draw()

    def invert_axis(self, axis):
        if self.image_data is not None:
            # Get current zoom view
            x0, x1 = self.ax.get_xlim()
            y0, y1 = self.ax.get_ylim()
    
            # Update flip flags
            if axis == 'x':
                self.x_flipped = not self.x_flipped
            elif axis == 'y':
                self.y_flipped = not self.y_flipped
            elif axis == 'b':
                self.x_flipped = not self.x_flipped
                self.y_flipped = not self.y_flipped
            elif axis == 'u':
                self.x_flipped = False
                self.y_flipped = False
    
            # Apply flip by reversing limits if needed
            if self.x_flipped:
                self.ax.set_xlim(x1, x0)
            else:
                self.ax.set_xlim(sorted([x0, x1]))
    
            if self.y_flipped:
                self.ax.set_ylim(y1, y0)
            else:
                self.ax.set_ylim(sorted([y0, y1]))
    
            self.image_canvas.draw()

    def reset_zoom(self):
        if self.mode == "image" and self.image_data is not None and hasattr(self, 'ax'):
            self.ax.set_xlim(0, self.image_data.shape[1])
            self.ax.set_ylim(0, self.image_data.shape[0])

            # Retain flip state
            self.ax.xaxis.set_inverted(self.x_flipped)
            self.ax.yaxis.set_inverted(self.y_flipped)

        elif self.mode == "plot" and hasattr(self, 'img_ax'):
            self.img_ax.autoscale()
            self.img_ax.relim()

        self.image_canvas.draw()

    def zoom(self, factor):
        # Use appropriate axis depending on mode
        ax = self.ax if self.mode == "image" else self.img_ax

        if ax is None:
            print("Zoom skipped: axis not defined yet.")
            return

        xlim = ax.get_xlim()
        ylim = ax.get_ylim()
        x_center = (xlim[0] + xlim[1]) / 2
        y_center = (ylim[0] + ylim[1]) / 2
        x_range = (xlim[1] - xlim[0]) / factor
        y_range = (ylim[1] - ylim[0]) / factor
        ax.set_xlim(x_center - x_range / 2, x_center + x_range / 2)
        ax.set_ylim(y_center - y_range / 2, y_center + y_range / 2)
        self.image_canvas.draw()

    
    def show_pixel_value(self, event):
        # Mouse move callback to update Pixel (x,y), WCS coords, and pixel value.
        if event.xdata is None or event.ydata is None or self.image_data is None:
            return
        x, y = int(event.xdata), int(event.ydata)

        # Pixel value (bounded)
        pix = None
        try:
            if 0 <= y < self.image_data.shape[0] and 0 <= x < self.image_data.shape[1]:
                v = self.image_data[y, x]
                if np.isfinite(v):
                    pix = float(v)
        except Exception:
            pix = None

        # WCS conversion (if available & enabled)
        wcs_info = None
        try:
            if getattr(self, "image_wcs", None) is not None and self.wcs_checkbox.isChecked():
                cw = self.image_wcs.celestial if self.image_wcs.has_celestial else None
                if cw is not None:
                    world = cw.wcs_pix2world([[x, y]], 0)[0]
                    ctype1, ctype2 = cw.wcs.ctype
                    x_label = ctype1.split('-')[0]
                    y_label = ctype2.split('-')[0]
                    wcs_info = (x_label, float(world[0]), y_label, float(world[1]))
        except Exception:
            wcs_info = None

        # Update UI fields directly
        self.update_pixel_info_boxes(x, y, wcs_info=wcs_info, pixel_val=pix)

    

    def pan_start(self, event):
        if event.button == 1 and event.xdata and event.ydata:
            self._pan_start_pos = (event.xdata, event.ydata)

    def pan_move(self, event):
        if self._pan_start_pos and event.button == 1 and event.xdata and event.ydata:
            dx = self._pan_start_pos[0] - event.xdata
            dy = self._pan_start_pos[1] - event.ydata
            xlim = self.ax.get_xlim()
            ylim = self.ax.get_ylim()
            self.ax.set_xlim([x + dx for x in xlim])
            self.ax.set_ylim([y + dy for y in ylim])
            self.image_canvas.draw()
            self._pan_start_pos = (event.xdata, event.ydata)

    def show_histogram(self):
        if self.image_data is not None:
            self.hist_ax.clear()
            data = self.image_data.ravel()
            data = data[np.isfinite(data)]
            if data.size:
                lo, hi = np.percentile(data, [1, 99])
                data = np.clip(data, lo, hi)
                self.hist_ax.hist(data, bins=128)
            else:
                self.hist_ax.text(0.5, 0.5, 'No data', transform=self.hist_ax.transAxes, ha='center')
            self.hist_ax.set_title("Histogram")
            self.hist_ax.set_xlabel("Pixel Value")
            self.hist_ax.set_ylabel("Frequency")
            try:
                self.hist_canvas.figure.subplots_adjust(left=0.12, right=0.98, bottom=0.22, top=0.95)
            except Exception:
                pass
            self.hist_canvas.draw()

    def update_plot_style(self, *_args, redraw_axes=True):
        if getattr(self, "mode", None) != "plot":
            return
        if not getattr(self, "_plot_style_ready", False):
            return
        if self.plot_x is None or self.plot_y is None or not hasattr(self, "img_ax"):
            return

        line_color = self.line_color_combo.currentText() if hasattr(self, "line_color_combo") else "blue"
        marker_sym = self.marker_symbol_combo.currentText() if hasattr(self, "marker_symbol_combo") else "None"
        marker_col = self.marker_color_combo.currentText() if hasattr(self, "marker_color_combo") else line_color
        marker_sym = None if marker_sym == "None" else marker_sym

        if redraw_axes:
            self.img_ax.clear()
            self._plot_line = None

        if line_color == "None":
            # Remove line, only plot markers if requested
            if marker_sym:
                (self._plot_line,) = self.img_ax.plot(
                    self.plot_x, self.plot_y,
                    linestyle='',  # no line
                    marker=marker_sym, markersize=4,
                    markerfacecolor=marker_col, markeredgecolor=marker_col
                )
            else:
                self._plot_line = None
        else:
            if self._plot_line is None:
                (self._plot_line,) = self.img_ax.plot(
                    self.plot_x, self.plot_y,
                    color=line_color, linestyle='-',
                    marker=marker_sym, markersize=4,
                    markerfacecolor=marker_col, markeredgecolor=marker_col
                )
            else:
                self._plot_line.set_color(line_color)
                self._plot_line.set_linestyle('-')
                self._plot_line.set_marker(marker_sym or '')
                self._plot_line.set_markersize(4)
                self._plot_line.set_markerfacecolor(marker_col)
                self._plot_line.set_markeredgecolor(marker_col)

        self.image_canvas.draw()

if __name__ == '__main__':
    # print("len of argv =", len(sys.argv))
    if len(sys.argv) == 3:
        # Image mode
        fits_file = sys.argv[1]
        hdu_index = int(sys.argv[2])
        mode = "image"
        col_x = col_y = None
    elif len(sys.argv) == 6 and sys.argv[5].lower() == "plot":
        # Plot mode
        fits_file = sys.argv[1]
        hdu_index = int(sys.argv[2])
        col_x = sys.argv[3]
        col_y = sys.argv[4]
        mode = "plot"
    else:
        print("Usage:")
        print("  For image: python pow.py <fits_file> <hdu_index>")
        print("  For plot:  python pow.py <fits_file> <hdu_index> <col_x> <col_y> plot")
        sys.exit(1)

    app = QtWidgets.QApplication(sys.argv)
    viewer = FITSViewer(fits_file, mode, hdu_index, col_x, col_y)
    viewer.resize(1000, 800)
    viewer.show()
    sys.exit(app.exec())


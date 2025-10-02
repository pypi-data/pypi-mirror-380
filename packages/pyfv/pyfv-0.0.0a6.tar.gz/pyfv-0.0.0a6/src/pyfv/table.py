#!/opt/miniconda3/bin/python
# -----------------------------------------------------------------------------
# PyFV: A modern Python FITS Viewer
# Copyright (c) 2025, Pan S. Chai
# Distributed under the BSD 3-Clause License. See LICENSE file for details.
# -----------------------------------------------------------------------------
#
#  Python FV
#
#    Module: table.py
#
#  Version: Ver 1.0 (beta)
#
#-------------------------------------------------------------------------------
#
# Modification History:
#
#   - Pan Chai, October 2025
#     Package migrated and table/image display unified
#
#-------------------------------------------------------------------------------
#
# Description:
#   Routine to display data in tabulated form from FITS file
#
#-------------------------------------------------------------------------------
# PyFV: A modern Python FITS Viewer
# Copyright (c) 2025, Pan S. Chai
# Distributed under the BSD 3-Clause License. See LICENSE file for details.
# -----------------------------------------------------------------------------
#
#  Python FV
#
#    Module: table.py
#
#  Version: Ver 1.0 (beta)
#
#-------------------------------------------------------------------------------
#
# Modification History:
#    Refer to Git log for details.
#
# Notes:
#    This module provides a docked/undocked table editor for FITS tables and
#    a grid view for image data. It now supports selecting a 2-D slice from
#    3-D/4-D cubes for display/edit and saving that slice back.
#
#-------------------------------------------------------------------------------
# Description:
#   Routine to display data in tabulated form from FITS file
#
#-------------------------------------------------------------------------------
# table.py - PyQt6 docked Table/Image editor for FITS
from __future__ import annotations
import os
from typing import Any, List, Tuple, Optional
import numpy as np
from astropy.io import fits

from PyQt6.QtCore import Qt, QAbstractTableModel, QModelIndex, QVariant, pyqtSignal
from PyQt6.QtGui import QFont, QAction
from PyQt6.QtWidgets import (
QWidget, QVBoxLayout, QHBoxLayout, QTableView, QTabWidget, QDockWidget,
    QDialog, QDialogButtonBox, QLabel, QPushButton, QCheckBox, QLineEdit,
    QAbstractItemView, QMessageBox,
    QSpinBox,
    QGridLayout
)

# ------------------ Dock container ------------------
def _get_or_make_table_tab_container(parent):
    if getattr(parent, "table_tab_widget", None) is not None:
        mode = getattr(parent, "_table_container_mode", "dock")
        return mode, parent.table_tab_widget

    if hasattr(parent, "addDockWidget"):
        dock = QDockWidget("Table", parent)
        dock.setObjectName("fv_table_dock")
        dock.setFeatures(
            QDockWidget.DockWidgetFeature.DockWidgetMovable
            | QDockWidget.DockWidgetFeature.DockWidgetFloatable
        )
        parent.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, dock)
        parent.table_dock = dock
        tabw = QTabWidget(dock)
        dock.setWidget(tabw)
        parent.table_tab_widget = tabw
        parent._table_container_mode = "dock"
        return "dock", tabw

    # Fallback dialog
    dlg = QDialog(parent)
    dlg.setWindowTitle("Table")
    dlg.setObjectName("fv_table_dialog")
    dlg.resize(900, 600)
    layout = QVBoxLayout(dlg)
    tabw = QTabWidget(dlg)
    layout.addWidget(tabw)
    btns = QDialogButtonBox(QDialogButtonBox.StandardButton.Close, dlg)
    btns.rejected.connect(dlg.close)
    layout.addWidget(btns)
    dlg.show()

    parent.table_dialog = dlg
    parent.table_tab_widget = tabw
    parent._table_container_mode = "dialog"
    return "dialog", tabw

# -------------- Coercion helpers ------------------
def _coerce(value_str: str, target_dtype):
    s = value_str.strip()
    if s == "":
        # keep empty string for string columns; for numeric, use 0
        if target_dtype.kind in ("U", "S", "O"):
            return ""
        return 0
    try:
        if target_dtype.kind in ("i", "u"):
            return np.int64(s).astype(target_dtype)
        if target_dtype.kind == "f":
            return np.float64(s).astype(target_dtype)
        if target_dtype.kind in ("U", "S", "O"):
            return s
        if target_dtype.kind == "b":
            return s.upper() in ("1", "T", "TRUE", "YES")
    except Exception:
        pass
    # last resort: try Python eval-like conversion
    try:
        return type(target_dtype.type())(s)
    except Exception:
        return s

# ------------------ Models ------------------
class FitsTableModel(QAbstractTableModel):
    changed = pyqtSignal(int, int, object, object)  # row, col, old, new

    def __init__(self, recarray, colnames: List[str]):
        super().__init__()
        self.data_rec = recarray  # numpy.recarray or FITS_rec
        self.colnames = list(colnames)

    def rowCount(self, parent=QModelIndex()):
        return len(self.data_rec)

    def columnCount(self, parent=QModelIndex()):
        return len(self.colnames)

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if role != Qt.ItemDataRole.DisplayRole:
            return None
        if orientation == Qt.Orientation.Horizontal:
            return str(self.colnames[section])
        return str(section)

    def data(self, index: QModelIndex, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return None
        r, c = index.row(), index.column()
        col = self.colnames[c]
        val = self.data_rec[r][col]
        if role in (Qt.ItemDataRole.DisplayRole, Qt.ItemDataRole.EditRole):
            # handle bytes/strings
            if isinstance(val, (bytes, bytearray)):
                try:
                    return val.decode('utf-8', errors='ignore')
                except Exception:
                    return str(val)
            return str(val)
        return None

    def flags(self, index):
        if not index.isValid():
            return Qt.ItemFlag.NoItemFlags
        return (
            Qt.ItemFlag.ItemIsEnabled
            | Qt.ItemFlag.ItemIsSelectable
            | Qt.ItemFlag.ItemIsEditable
        )

    def setData(self, index: QModelIndex, value, role=Qt.ItemDataRole.EditRole):
        if role != Qt.ItemDataRole.EditRole or not index.isValid():
            return False
        r, c = index.row(), index.column()
        col = self.colnames[c]
        old = self.data_rec[r][col]
        # figure dtype
        dt = self.data_rec.dtype.fields[col][0]
        newv = _coerce(str(value), dt)
        try:
            self.data_rec[r][col] = newv
        except Exception:
            return False
        self.dataChanged.emit(index, index, [Qt.ItemDataRole.DisplayRole])
        self.changed.emit(r, c, old, newv)
        return True

class FitsImageModel(QAbstractTableModel):
    changed = pyqtSignal(int, int, object, object)  # row, col, old, new

    def __init__(self, array2d: np.ndarray):
        super().__init__()
        # Expect 2-D plane already
        self.arr = np.array(array2d)

    def rowCount(self, parent=QModelIndex()):
        return int(self.arr.shape[0])

    def columnCount(self, parent=QModelIndex()):
        return int(self.arr.shape[1]) if self.arr.ndim >= 2 else 0

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            return str(section)
        return None

    def data(self, index: QModelIndex, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return None
        r, c = index.row(), index.column()
        val = self.arr[r, c]
        if role in (Qt.ItemDataRole.DisplayRole, Qt.ItemDataRole.EditRole):
            return str(val)
        return None

    def flags(self, index):
        if not index.isValid():
            return Qt.ItemFlag.NoItemFlags
        return Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEditable

    def setData(self, index: QModelIndex, value, role=Qt.ItemDataRole.EditRole):
        if role != Qt.ItemDataRole.EditRole or not index.isValid():
            return False
        r, c = index.row(), index.column()
        old = self.arr[r, c]
        # coerce to array dtype
        newv = _coerce(str(value), self.arr.dtype)
        try:
            self.arr[r, c] = newv
        except Exception:
            return False
        self.dataChanged.emit(index, index, [Qt.ItemDataRole.DisplayRole])
        self.changed.emit(r, c, old, newv)
        return True

# ------------------ Image slice picker dialog ------------------
class SliceDialog(QDialog):
    """
    PyQt dialog to pick a single 2-D plane from a 3D/4D FITS image.
    UI matches classic FV: Data Cube (only for 4D) and Image Slice (z).
    Returns (cube_1based, slice_1based) if accepted; None if cancelled.
    """
    def __init__(self, parent, z_len: int, s_len: int | None = None):
        super().__init__(parent)
        self.setWindowTitle("fv: Image Selection")
        self._z_len = int(z_len)
        self._s_len = int(s_len) if s_len is not None else None

        layout = QVBoxLayout(self)
        banner = QLabel(
            f"The 4D image contains {self._s_len} data cube(s), each with {self._z_len} slices"
            if self._s_len is not None else
            f"The 3D image contains {self._z_len} slices"
        )
        layout.addWidget(banner)

        grid = QGridLayout()
        row = 0
        if self._s_len is not None:
            grid.addWidget(QLabel("Data Cube"), row, 0)
            self.cube_spin = QSpinBox()
            self.cube_spin.setRange(1, max(1, self._s_len))
            self.cube_spin.setValue(1)
            grid.addWidget(self.cube_spin, row, 1)
            row += 1

        grid.addWidget(QLabel("Image Slice"), row, 0)
        self.slice_spin = QSpinBox()
        self.slice_spin.setRange(1, max(1, self._z_len))
        self.slice_spin.setValue(1)
        grid.addWidget(self.slice_spin, row, 1)
        layout.addLayout(grid)

        btns = QDialogButtonBox()
        self.btn_ok = btns.addButton("Display", QDialogButtonBox.ButtonRole.AcceptRole)
        self.btn_cancel = btns.addButton(QDialogButtonBox.StandardButton.Cancel)
        self.btn_help = QPushButton("Help")
        btns.addButton(self.btn_help, QDialogButtonBox.ButtonRole.HelpRole)
        layout.addWidget(btns)

        self.btn_ok.clicked.connect(self.accept)
        self.btn_cancel.clicked.connect(self.reject)
        self.btn_help.clicked.connect(self._help)

    def _help(self):
        QMessageBox.information(self, "Help",
            "Pick Data Cube (if 4D) and Image Slice (z). Indices are 1-based.")

    def get_values(self):
        cube = int(self.cube_spin.value()) if hasattr(self, "cube_spin") else 1
        return cube, int(self.slice_spin.value())

# ------------------ Editor widget ------------------
class TableEditor(QWidget):
    def __init__(self, parent, fits_path: str, hdu_index: int):
        super().__init__(parent)
        self._image_ndim = None
        self._sel = {}
        self.fits_path = fits_path
        self.hdu_index = hdu_index
        self.undo_stack: List[Tuple[int,int,object,object]] = []  # (r,c,old,new)
        self.apply_on_edit = True

        layout = QVBoxLayout(self)

        # Controls row
        controls = QHBoxLayout()
        self.apply_chk = QCheckBox("Apply changes immediately")
        self.apply_chk.setChecked(True)
        self.save_btn = QPushButton("Save")
        self.revert_btn = QPushButton("Undo")
        controls.addWidget(self.apply_chk)
        controls.addStretch(1)
        controls.addWidget(self.save_btn)
        controls.addWidget(self.revert_btn)
        layout.addLayout(controls)

        # Table view
        self.view = QTableView(self)
        self.view.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectItems)
        self.view.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.view.setAlternatingRowColors(True)
        font = QFont()
        font.setFamily("Menlo")
        font.setPointSize(11)
        self.view.setFont(font)
        layout.addWidget(self.view)

        # Load data
        self._load()

        # Wire signals
        self.apply_chk.toggled.connect(self._toggle_apply)
        self.save_btn.clicked.connect(self._save)
        self.revert_btn.clicked.connect(self._undo)

    def _toggle_apply(self, state: bool):
        self.apply_on_edit = bool(state)

    def _load(self):
        with fits.open(self.fits_path, mode="readonly", memmap=False, ignore_missing_end=True) as hdul:
            hdu = hdul[self.hdu_index]
            if isinstance(hdu, (fits.BinTableHDU, fits.TableHDU)):
                data = hdu.data
                colnames = list(data.names)
                model = FitsTableModel(data, colnames)
                model.changed.connect(self._on_cell_changed)
                self.model = model
            elif isinstance(hdu, fits.ImageHDU) or (self.hdu_index == 0 and isinstance(hdu, fits.PrimaryHDU)):
                arr = hdu.data
                if arr is None:
                    arr = np.zeros((0,0))
                arr = np.array(arr)
                self._image_ndim = int(arr.ndim)
                plane = arr
                if arr.ndim == 3:
                    z_len = arr.shape[0]
                    dlg = SliceDialog(self, z_len=z_len, s_len=None)
                    if dlg.exec() == QDialog.DialogCode.Accepted:
                        _, slice1 = dlg.get_values()
                        self._sel = {"z": max(0, slice1-1)}
                    else:
                        self._sel = {"z": 0}
                    plane = arr[self._sel["z"], :, :]
                elif arr.ndim == 4:
                    s_len, z_len = arr.shape[0], arr.shape[1]
                    dlg = SliceDialog(self, z_len=z_len, s_len=s_len)
                    if dlg.exec() == QDialog.DialogCode.Accepted:
                        cube1, slice1 = dlg.get_values()
                        self._sel = {"s": max(0, cube1-1), "z": max(0, slice1-1)}
                    else:
                        self._sel = {"s": 0, "z": 0}
                    plane = arr[self._sel["s"], self._sel["z"], :, :]
                else:
                    self._sel = {}
                model = FitsImageModel(np.array(plane))
                model.changed.connect(self._on_cell_changed)
                self.model = model
            else:
                raise TypeError("Unsupported HDU type for Table editor.")
        self.view.setModel(self.model)
        self.view.resizeColumnsToContents()

    def _on_cell_changed(self, r, c, old, new):
        self.undo_stack.append((r,c,old,new))
        if self.apply_on_edit:
            self._save()

    def _save(self):
        # write back to fits
        with fits.open(self.fits_path, mode="update", memmap=False) as hdul:
            hdu = hdul[self.hdu_index]
            if isinstance(self.model, FitsTableModel):
                # Assign row-wise for changed cells; for simplicity we reassign all changed items since last save
                for r,c,old,new in self.undo_stack:
                    col = self.model.colnames[c]
                    try:
                        hdu.data[r][col] = self.model.data_rec[r][col]
                    except Exception:
                        pass
            elif isinstance(self.model, FitsImageModel):
                arr = hdu.data
                if arr is None:
                    pass
                elif (self._image_ndim in (None,2)) or (arr.ndim == 2) or (not self._sel):
                    hdu.data[...] = self.model.arr
                elif self._image_ndim == 3 and arr.ndim == 3:
                    z = int(self._sel.get("z", 0))
                    arr[z, :, :] = self.model.arr
                elif self._image_ndim == 4 and arr.ndim == 4:
                    s = int(self._sel.get("s", 0))
                    z = int(self._sel.get("z", 0))
                    arr[s, z, :, :] = self.model.arr
            hdul.flush(output_verify="silentfix+warn")
        # clear undo stack after save
        self.undo_stack.clear()

    def _undo(self):
        if not self.undo_stack:
            QMessageBox.information(self, "Undo", "Nothing to undo.")
            return
        r,c,old,new = self.undo_stack.pop()
        idx = self.model.index(r,c)
        # setData will push another change; temporarily disable apply/save
        prev_apply = self.apply_on_edit
        self.apply_on_edit = False
        self.model.setData(idx, str(old), role=Qt.ItemDataRole.EditRole)
        self.apply_on_edit = prev_apply
        self.view.scrollTo(idx)
        self.view.setCurrentIndex(idx)

# ------------------ Public entry ------------------
def open_table_editor(parent, fits_file: str, hdu_index: int):
    mode, tabw = _get_or_make_table_tab_container(parent)
    tab_name = f"{os.path.basename(fits_file)}[{hdu_index}]"

    # If already open for this file+HDU, focus it
    for i in range(tabw.count()):
        w = tabw.widget(i)
        if isinstance(w, TableEditor) and w.fits_path == fits_file and w.hdu_index == hdu_index:
            tabw.setCurrentIndex(i)
            if mode == "dock":
                parent.table_dock.show()
            else:
                parent.table_dialog.show()
            return

    editor = TableEditor(parent, fits_file, hdu_index)
    tabw.addTab(editor, tab_name)
    tabw.setCurrentWidget(editor)
    if mode == "dock":
        parent.table_dock.show()
    else:
        parent.table_dialog.show()


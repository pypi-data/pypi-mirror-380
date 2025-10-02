#!/opt/miniconda3/bin/python
# -----------------------------------------------------------------------------
# PyFV: A modern Python FITS Viewer
# Copyright (c) 2025, Pan S. Chai
# Distributed under the BSD 3-Clause License. See LICENSE file for details.
# -----------------------------------------------------------------------------
#
#  Python FV Project 
#
#      module: header.py
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
#   Routine to display Header info from FITS file. If there is more than one
#   hdu, all displayed header info will be tabbed together into one window.
#
#-------------------------------------------------------------------------------

from __future__ import annotations
import os
import re
from dataclasses import dataclass
from typing import Any, List, Optional, Tuple

from astropy.io import fits

# --------------------------- PyQt6 imports -----------------------------------
from PyQt6.QtCore import (
    Qt,
    QAbstractTableModel,
    QModelIndex,
    QObject,        # <-- this is the missing one
    pyqtSignal,
    pyqtSlot,
)

from PyQt6.QtWidgets import QDockWidget, QDialog, QDialogButtonBox
from PyQt6.QtCore import Qt

from PyQt6.QtGui import QBrush, QColor, QFont, QAction   # <-- QAction moved here
from PyQt6.QtWidgets import (
    QAbstractItemView, QCheckBox, QHBoxLayout, QLabel, QLineEdit,
    QMenu, QMessageBox, QPushButton, QTableView, QTabWidget, QTextEdit,
    QVBoxLayout, QWidget
)

# =============================================================================
#                          READ-ONLY (BACK-COMPAT)
# =============================================================================

class HeaderLoader(QObject):
    """
    Back-compat worker used by summary.py (PyQt6).
    Emits finished(hdu_index, header_text).
    """
    finished = pyqtSignal(int, str)

    def __init__(self, fits_file: str, hdu_index: int):
        super().__init__()
        self.fits_file = fits_file
        self.hdu_index = hdu_index

    @pyqtSlot()
    def run(self):
        try:
            with fits.open(self.fits_file) as hdulist:
                header_text = hdulist[self.hdu_index].header.tostring(sep="\n")
        except Exception as e:
            header_text = f"Error: {e}"
        self.finished.emit(self.hdu_index, header_text)


def _get_or_make_header_tab_container(parent):
    """
    Ensure there's a visible place to put header tabs.
    If parent is a QMainWindow (has addDockWidget), create/reuse a right-side QDockWidget
    that holds a QTabWidget. Otherwise, create/reuse a floating QDialog that contains a QTabWidget.
    Returns (mode, tab_widget) where mode is 'dock' or 'dialog'.
    """
    # Reuse if already made
    if getattr(parent, "header_tab_widget", None) is not None:
        mode = getattr(parent, "_header_container_mode", "dock")
        return mode, parent.header_tab_widget

    # QMainWindow path (dock)
    if hasattr(parent, "addDockWidget"):
        dock = QDockWidget("Header", parent)
        dock.setObjectName("fv_header_dock")
        dock.setAllowedAreas(
            Qt.DockWidgetArea.LeftDockWidgetArea
            | Qt.DockWidgetArea.RightDockWidgetArea
            | Qt.DockWidgetArea.BottomDockWidgetArea
        )
        tabw = QTabWidget(dock)
        dock.setWidget(tabw)
        parent.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, dock)
        dock.show()

        parent.header_dock = dock
        parent.header_tab_widget = tabw
        parent._header_container_mode = "dock"
        return "dock", tabw

    # Fallback: floating dialog with a tab widget
    dlg = QDialog(parent)
    dlg.setWindowTitle("Header")
    dlg.setObjectName("fv_header_dialog")
    dlg.resize(800, 600)
    layout = QVBoxLayout(dlg)
    tabw = QTabWidget(dlg)
    layout.addWidget(tabw)
    # Add a close button for the dialog
    btns = QDialogButtonBox(QDialogButtonBox.StandardButton.Close, dlg)
    btns.rejected.connect(dlg.close)
    layout.addWidget(btns)
    dlg.show()

    parent.header_dialog = dlg
    parent.header_tab_widget = tabw
    parent._header_container_mode = "dialog"
    return "dialog", tabw

def _ensure_header_tab_container(parent) -> None:
    if getattr(parent, "header_tab_widget", None) is None:
        parent.header_tab_widget = QTabWidget(parent)

def show_header_dialog(parent, fits_file: str, hdu_index: int, header_text: str) -> None:
    mode, tabw = _get_or_make_header_tab_container(parent)

    text_edit = QTextEdit()
    text_edit.setPlainText(header_text)
    text_edit.setReadOnly(True)
    mono = QFont("Courier New"); mono.setStyleHint(QFont.StyleHint.Monospace); mono.setPointSize(12)
    text_edit.setFont(mono)

    tab_name = f"{os.path.basename(fits_file)}[{hdu_index}]"
    tabw.addTab(text_edit, tab_name)
    tabw.setCurrentWidget(text_edit)

    # Ensure container is visible
    if mode == "dock":
        parent.header_dock.show()
    else:
        parent.header_dialog.show()


def open_header_editor(parent, fits_file: str, hdu_index: int):
    mode, tabw = _get_or_make_header_tab_container(parent)

    editor = HeaderEditor(parent, fits_file, hdu_index)
    tab_name = f"{os.path.basename(fits_file)}[{hdu_index}]"
    tabw.addTab(editor, tab_name)
    tabw.setCurrentWidget(editor)

    if mode == "dock":
        parent.header_dock.show()
    else:
        parent.header_dialog.show()

def show_header_dialog_X(parent, fits_file: str, hdu_index: int, header_text: str) -> None:
    _ensure_header_tab_container(parent)
    text_edit = QTextEdit()
    text_edit.setPlainText(header_text)
    text_edit.setReadOnly(True)
    mono = QFont("Courier New"); mono.setStyleHint(QFont.StyleHint.Monospace); mono.setPointSize(12)
    text_edit.setFont(mono)
    tab_name = f"{os.path.basename(fits_file)}[{hdu_index}]"
    parent.header_tab_widget.addTab(text_edit, tab_name)
    parent.header_tab_widget.setCurrentWidget(text_edit)
    parent.header_tab_widget.show()

# =============================================================================
#                          EDITABLE HEADER (NEW)
# =============================================================================

MANDATORY_PROTECTION_DEFAULT = True
PRIMARY_MANDATORY = {"SIMPLE", "BITPIX", "NAXIS", "EXTEND"}
EXT_MANDATORY_BASE = {"XTENSION", "BITPIX", "NAXIS", "PCOUNT", "GCOUNT"}

NAXISN_RE = re.compile(r"^NAXIS(\d+)$", re.IGNORECASE)
T_N_RE = re.compile(r"^(T(?:TYPE|FORM|UNIT|BCOL|SCAL|ZERO|NULL|DISP))(\d+)$", re.IGNORECASE)


def _is_mandatory(key: str, header: fits.Header, is_primary: bool) -> bool:
    k = key.upper().strip()
    if is_primary:
        if k in PRIMARY_MANDATORY: return True
        if NAXISN_RE.match(k): return True
        return False
    else:
        if k in EXT_MANDATORY_BASE: return True
        if NAXISN_RE.match(k): return True
        if T_N_RE.match(k): return True
        return False


def _coerce_value(text: str) -> Any:
    s = text.strip()
    u = s.upper()
    if u in ("T", "TRUE"): return True
    if u in ("F", "FALSE"): return False
    if re.fullmatch(r"[+-]?\d+", s):
        try: return int(s)
        except Exception: pass
    if re.fullmatch(r"[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?", s):
        try: return float(s)
        except Exception: pass
    return "" if s == "" else s


@dataclass
class CardRow:
    key: str
    value: Any
    comment: str
    mandatory: bool


class HeaderTableModel(QAbstractTableModel):
    COLS = ["Keyword", "Value", "Comment"]

    def __init__(self, rows: List[CardRow]):
        super().__init__()
        self.rows = rows

    def rowCount(self, parent=QModelIndex()): return len(self.rows)
    def columnCount(self, parent=QModelIndex()): return len(self.COLS)

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole and orientation == Qt.Orientation.Horizontal:
            return self.COLS[section]
        return None

    def data(self, index: QModelIndex, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid(): return None
        r, c = index.row(), index.column()
        row = self.rows[r]

        if role in (Qt.ItemDataRole.DisplayRole, Qt.ItemDataRole.EditRole):
            if c == 0: return row.key
            if c == 1:
                if isinstance(row.value, bool):
                    return "T" if row.value else "F"
                return "" if row.value is None else str(row.value)
            if c == 2: return row.comment

        if role == Qt.ItemDataRole.ForegroundRole and row.mandatory:
            return QBrush(QColor(140, 90, 20))
        if role == Qt.ItemDataRole.BackgroundRole and row.mandatory:
            return QBrush(QColor(255, 245, 230))
        return None

    def insert_before(self, idx: int, new_row: CardRow):
        self.beginInsertRows(QModelIndex(), idx, idx)
        self.rows.insert(idx, new_row)
        self.endInsertRows()

    def remove_at(self, idx: int):
        self.beginRemoveRows(QModelIndex(), idx, idx)
        self.rows.pop(idx)
        self.endRemoveRows()

    def update_row(self, idx: int, key: Optional[str], value: Optional[Any], comment: Optional[str]):
        row = self.rows[idx]
        if key is not None: row.key = key
        if value is not None: row.value = value
        if comment is not None: row.comment = comment
        self.dataChanged.emit(self.index(idx, 0), self.index(idx, self.columnCount() - 1),
                              [Qt.ItemDataRole.DisplayRole])


class HeaderEditor(QWidget):
    def __init__(self, parent, fits_path: str, hdu_index: int):
        super().__init__(parent)
        self.fits_path = fits_path
        self.hdu_index = hdu_index
        self.parent_window = parent
        self.protect_mandatory = getattr(parent, "protect_mandatory_keywords", MANDATORY_PROTECTION_DEFAULT)
        self.undo_stack: List[Tuple[str, Tuple]] = []
        self._load_header()
        self._build_ui()

    # ---------------- Load & Save ----------------

    def _load_header(self):
        # tolerate malformed blocks / missing END; disable memmap to avoid mmap on corrupt files
        with fits.open(self.fits_path, mode="readonly",
                       ignore_missing_end=True, memmap=False) as hdul:
            hdu = hdul[self.hdu_index]
            hdr = hdu.header
            is_primary = (self.hdu_index == 0)
            self.rows = []

            # Read directly from cards to get key/value/comment safely
            for card in hdr.cards:
                key = card.keyword
                if key in ("COMMENT", "HISTORY"):
                    continue
                val = card.value
                cmt = card.comment or ""
                self.rows.append(
                    CardRow(
                        key=key,
                        value=val,
                        comment=cmt,
                        mandatory=_is_mandatory(key, hdr, is_primary),
                    )
                )
    
            self._is_primary = is_primary

    def _write_all_to_fits(self):
        # Re-write the header in place and FLUSH to disk
        from astropy.io import fits
        with fits.open(self.fits_path, mode="update", memmap=False) as hdul:
            hdr = hdul[self.hdu_index].header

            # Remove all non-COMMENT/HISTORY cards (preserve those blocks)
            keys_to_delete = [k for k in list(hdr.keys()) if k not in ("COMMENT", "HISTORY")]
            for k in keys_to_delete:
                while k in hdr:
                    del hdr[k]

            # Re-append our current rows, in order
            for row in self.rows:
                hdr.append((row.key, row.value, row.comment))

            # Write now. Astropy will repair minor issues; warnings still go to console.
            hdul.flush(output_verify="silentfix+warn")

    # ---------------- UI ----------------

    def _build_ui(self):
        layout = QVBoxLayout(self)

        # Table
        self.model = HeaderTableModel(self.rows)
        self.table = QTableView(self)
        self.table.setModel(self.model)
        self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.table.setAlternatingRowColors(True)
        self.table.verticalHeader().setVisible(False)
        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        mono = QFont("Courier New"); mono.setStyleHint(QFont.StyleHint.Monospace); mono.setPointSize(12)
        self.table.setFont(mono)

        self.table.clicked.connect(self._on_row_clicked)
        self.table.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.table.customContextMenuRequested.connect(self._on_context_menu)

        layout.addWidget(self.table)

        # Search
        srow = QHBoxLayout()
        srow.addWidget(QLabel("Search for:"))
        self.search_edit = QLineEdit(self)
        self.find_btn = QPushButton("Find", self)
        self.case_chk = QCheckBox("Case sensitive", self)
        self.find_btn.clicked.connect(self._on_search)
        srow.addWidget(self.search_edit); srow.addWidget(self.find_btn); srow.addWidget(self.case_chk); srow.addStretch()
        layout.addLayout(srow)

        # Editors
        erow = QHBoxLayout()
        self.key_edit = QLineEdit(self); self.key_edit.setPlaceholderText("Keyword")
        self.val_edit = QLineEdit(self); self.val_edit.setPlaceholderText("Value")
        self.cmt_edit = QLineEdit(self); self.cmt_edit.setPlaceholderText("Comment")
        for w in (self.key_edit, self.val_edit, self.cmt_edit):
            w.returnPressed.connect(self._commit_edit)
        erow.addWidget(QLabel("Edit:"))
        erow.addWidget(self.key_edit, 2); erow.addWidget(self.val_edit, 3); erow.addWidget(self.cmt_edit, 5)
        self.save_btn = QPushButton("Save", self); self.save_btn.clicked.connect(self._commit_edit)
        self.undo_btn  = QPushButton("Undo", self);  self.undo_btn.clicked.connect(self._undo_last)
        erow.addWidget(self.save_btn); erow.addWidget(self.undo_btn)
        layout.addLayout(erow)

        self.table.resizeColumnsToContents()
        self.table.setColumnWidth(0, 170)
        self.table.setColumnWidth(1, 220)

    # ---------------- Handlers ----------------

    def _on_row_clicked(self, index: QModelIndex):
        r = index.row(); row = self.model.rows[r]
        self.key_edit.setText(row.key)
        if isinstance(row.value, bool):
            self.val_edit.setText("T" if row.value else "F")
        else:
            self.val_edit.setText("" if row.value is None else str(row.value))
        self.cmt_edit.setText(row.comment)

    def _selected_row_index(self) -> Optional[int]:
        sel = self.table.selectionModel().selectedRows()
        return None if not sel else sel[0].row()

    def _warn(self, msg: str):
        QMessageBox.warning(self, "Header Edit", msg)

    def _confirm(self, msg: str) -> bool:
        ret = QMessageBox.question(self, "Confirm", msg,
                                   QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                   QMessageBox.StandardButton.No)
        return ret == QMessageBox.StandardButton.Yes

    def _commit_edit(self):
        idx = self._selected_row_index()
        if idx is None:
            self._warn("Select a keyword row to edit.")
            return

        new_key = self.key_edit.text().strip()
        new_val = _coerce_value(self.val_edit.text())
        new_cmt = self.cmt_edit.text()
        row = self.model.rows[idx]

        # Mandatory protection: only allow COMMENT edits if enabled
        if row.mandatory and self.protect_mandatory:
            if (new_key != row.key) or (str(new_val) != str(row.value)):
                self._warn("Mandatory keyword: only COMMENT may be edited (protection enabled).")
                return

        before = CardRow(row.key, row.value, row.comment, row.mandatory)
        self.undo_stack.append(("edit", (idx, before)))
    
        # Update the model row
        self.model.update_row(idx, new_key, new_val, new_cmt)

        # WRITE TO DISK
        try:
            self._write_all_to_fits()
            # Optional: status bar feedback if the main window has one
            if hasattr(self.parent_window, "statusBar") and self.parent_window.statusBar():
                self.parent_window.statusBar().showMessage("Header saved", 2000)
        except Exception as e:
            self._warn(f"Failed to write to FITS: {e}")
            # rollback UI state
            self.model.update_row(idx, before.key, before.value, before.comment)
            if self.undo_stack and self.undo_stack[-1][0] == "edit":
                self.undo_stack.pop()
            return

        self.table.resizeColumnsToContents()

    def _on_context_menu(self, pos):
        idx = self.table.indexAt(pos)
        if not idx.isValid(): return
        row_i = idx.row(); row = self.model.rows[row_i]

        menu = QMenu(self)
        act_insert = QAction("Insert new keyword before", self)
        act_delete = QAction("Delete keyword", self)
        act_undo   = QAction("Undo", self)

        if row.mandatory and self.protect_mandatory:
            act_insert.setEnabled(False)
            act_delete.setEnabled(False)

        act_insert.triggered.connect(lambda: self._insert_before(row_i))
        act_delete.triggered.connect(lambda: self._delete_row(row_i))
        act_undo.triggered.connect(self._undo_last)
        menu.addAction(act_insert); menu.addAction(act_delete); menu.addSeparator(); menu.addAction(act_undo)
        menu.exec(self.table.viewport().mapToGlobal(pos))  # PyQt6 uses exec()

    def _insert_before(self, idx: int):
        key = self.key_edit.text().strip()
        if not key:
            self._warn("Enter a Keyword in the editor fields before inserting.")
            return
        val = _coerce_value(self.val_edit.text())
        cmt = self.cmt_edit.text()

        if self.protect_mandatory and _is_mandatory(key, fits.Header(), self._is_primary):
            self._warn("Cannot insert a mandatory keyword while protection is enabled.")
            return

        new_row = CardRow(key, val, cmt, _is_mandatory(key, fits.Header(), self._is_primary))
        self.undo_stack.append(("insert", (idx,)))
        self.model.insert_before(idx, new_row)

        try:
            self._write_all_to_fits()
        except Exception as e:
            self._warn(f"Failed to write to FITS: {e}")
            self.model.remove_at(idx)
            if self.undo_stack and self.undo_stack[-1][0] == "insert":
                self.undo_stack.pop()
            return

        self.table.selectRow(idx)
        self.table.resizeColumnsToContents()

    def _delete_row(self, idx: int):
        row = self.model.rows[idx]
        if row.mandatory and self.protect_mandatory:
            self._warn("Cannot delete a mandatory keyword while protection is enabled.")
            return
        if not self._confirm(f"Delete keyword '{row.key}'?"):
            return

        before = CardRow(row.key, row.value, row.comment, row.mandatory)
        self.undo_stack.append(("delete", (idx, before)))
        self.model.remove_at(idx)

        try:
            self._write_all_to_fits()
        except Exception as e:
            self._warn(f"Failed to write to FITS: {e}")
            self.model.insert_before(idx, before)
            if self.undo_stack and self.undo_stack[-1][0] == "delete":
                self.undo_stack.pop()
            return

        if idx >= self.model.rowCount(): idx = self.model.rowCount() - 1
        if idx >= 0: self.table.selectRow(idx)
        self.table.resizeColumnsToContents()

    def _undo_last(self):
        if not self.undo_stack:
            self._warn("Nothing to undo.")
            return
        op, args = self.undo_stack.pop()
        if op == "edit":
            idx, before = args
            self.model.update_row(idx, before.key, before.value, before.comment)
        elif op == "insert":
            (idx,) = args
            if 0 <= idx < self.model.rowCount():
                self.model.remove_at(idx)
        elif op == "delete":
            idx, before = args
            if idx < 0: idx = 0
            if idx > self.model.rowCount(): idx = self.model.rowCount()
            self.model.insert_before(idx, before)

        try:
            self._write_all_to_fits()
        except Exception as e:
            self._warn(f"Failed to write to FITS during undo: {e}")

        self.table.resizeColumnsToContents()

    def _on_search(self):
        term = self.search_edit.text()
        if not term: return
        flags = 0 if self.case_chk.isChecked() else re.IGNORECASE
        rx = re.compile(re.escape(term), flags)
        start = (self._selected_row_index() or -1) + 1
        n = self.model.rowCount()
        for step in range(n):
            r = (start + step) % n
            row = self.model.rows[r]
            hay = f"{row.key} {row.value} {row.comment}"
            if rx.search(hay):
                self.table.selectRow(r)
                self.table.scrollTo(self.model.index(r, 0))
                self._on_row_clicked(self.model.index(r, 0))
                return
        self._warn("No more matches.")

def open_header_editor_X(parent, fits_file: str, hdu_index: int):
    if not hasattr(parent, "header_tab_widget") or not isinstance(parent.header_tab_widget, QTabWidget):
        parent.header_tab_widget = QTabWidget(parent)
    editor = HeaderEditor(parent, fits_file, hdu_index)
    tab_name = f"{os.path.basename(fits_file)}[{hdu_index}]"
    parent.header_tab_widget.addTab(editor, tab_name)
    parent.header_tab_widget.setCurrentWidget(editor)
    parent.header_tab_widget.show()


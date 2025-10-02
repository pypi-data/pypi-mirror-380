#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fv_script.py
Tiny harness to drive your Python FV/POW app from the command line, without changing your app.

USAGE EXAMPLES
--------------
# One-shot (stays open; no --quit)
python3 fv_script.py \
  --file /path/to/demo.fits \
  --summary \
  --showheader value\
  --showtable value\
  --plot TIME FLUX \
  --screenshot /tmp/fv_window.png \
  --saveimage /tmp/canvas.png

# Scripted (closes at end)
cat > commands.txt <<'EOF'
OPEN /path/to/demo.fits
SUMMARY
HEADER true
TABLE true
IMAGE
PLOT TIME FLUX
SAVEIMAGE /tmp/plot.png
SCREENSHOT /tmp/window.png
SLEEP 500
QUIT
EOF
python3 fv_script.py --script commands.txt

COMMAND LANGUAGE
----------------
OPEN <path>                # load FITS file (bypass file dialog)
SUMMARY                    # show summary view
HEADER <true|false>        # show header viewer (true = show)
TABLE <true|false>         # show table view (true = show)
IMAGE                      # show image view (best-effort)
PLOT <XCOL> <YCOL>         # plot table columns (routes to POW if available, else fallback)
SCREENSHOT <path.png>      # save the entire FV main window
SAVEIMAGE <path.png>       # save only the canvas (image/plot) if available; fallback to window
SLEEP <ms>                 # wait N milliseconds between steps
QUIT                       # exit the app

ADAPTERS
--------
Edit the adapter functions below to call your app’s real hooks. Gentle fallbacks are included so
you can try it immediately. You can progressively wire in:
  - fv.load_summary_data(path)
  - fv.show_summary_dialog(parent, fits_file, summary_data)
  - table.show_table_dialog(parent, fits_file, hdu_index)
  - utility.display_hdu_header(fits_file, hdu_index=None)
  - pow.plot_from_table(path, xcol, ycol, hdu_index=None)
"""

from __future__ import annotations

import io, contextlib
import argparse
import sys
from dataclasses import dataclass
from typing import List

from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QTextEdit, QMessageBox
from PyQt6.QtWidgets import QWidget

import os, re
from pathlib import Path

# at top-level (after imports)
QUIET = False

os.environ["FV_DOC_DIR"] = os.path.join(os.getcwd(), "doc")

# =========================
# === ADAPTER — EDIT ME ===
# =========================

def _find_doc_root() -> Path | None:
    env = os.environ.get("FV_DOC_DIR")
    if env and Path(env).is_dir():
        return Path(env)
    p = Path.cwd() / "doc"
    if p.is_dir():
        return p
    try:
        import fv
        fv_path = Path(fv.__file__).resolve()
        p = fv_path.parent / "doc"
        if p.is_dir():
            return p
        p = fv_path.parent.parent / "doc"
        if p.is_dir():
            return p
    except Exception:
        pass
    return None

def _index_help_topics(doc_root: Path) -> dict[str, Path]:
    idx: dict[str, Path] = {}
    for html in sorted(doc_root.glob("*.html")):
        stem = html.stem
        keys = {stem, stem.lower()}
        keys.add(re.sub(r'(?<!^)(?=[A-Z])', '-', stem).lower())       # image-display
        keys.add(re.sub(r'[^a-z0-9]+', '', stem.lower()))             # imagedisplay
        keys.add(html.name.lower())                                   # imageDisplay.html
        for k in keys:
            idx[k] = html
    return idx

def _resolve_help_file(topic_words: list[str] | None) -> tuple[Path | None, str]:
    doc_root = _find_doc_root()
    if not doc_root:
        return None, "Could not locate 'doc' directory. Set FV_DOC_DIR or place doc/ next to fv.py."

    if not topic_words:
        for name in ("startFv.html", "aboutFv.html", "fileSummary.html", "README"):
            p = doc_root / name
            if p.exists():
                return p, ""
        any_html = next(doc_root.glob("*.html"), None)
        return (any_html, "") if any_html else (None, f"No HTML files found in {doc_root}")

    if len(topic_words) == 1 and topic_words[0].strip().lower() == "list":
        return doc_root / "__LIST__", ""

    index = _index_help_topics(doc_root)
    raw = " ".join(topic_words).strip()
    variants = [
        raw.lower(),
        re.sub(r'[^a-z0-9]+', '', raw.lower()),
        raw.replace(" ", "").lower(),
        raw.replace(" ", "-").lower(),
    ]
    for q in variants:
        if q in index:
            return index[q], ""
    # fuzzy startswith on hyphen/compact variant
    for k, p in index.items():
        if k.startswith(variants[-1]):
            return p, ""
    return None, f"No help topic matched '{raw}'. Try 'HELP LIST'."

# --- HELP adapter (uses in-house help.py only; fallback = QTextBrowser) ---
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QTextBrowser, QMessageBox, QApplication
from PyQt6.QtCore import QUrl

# --- HELP adapter: use your help.py HelpWindow with dropdown ---
from PyQt6.QtWidgets import QMessageBox, QApplication
import os

def show_help_adapter(win, *topic_parts) -> None:
    """
    HELP                  -> open HelpWindow at default topic ("Start FV")
    HELP LIST             -> print available titles/filenames in stdout (quick ref)
    HELP <topic words>    -> open HelpWindow and select the matching topic
                             (e.g., HELP imagedisplay, HELP image display, HELP imageDisplay)
    """
    # 1) Locate doc/ and normalize the requested topic -> filename
    topic = " ".join([t for t in topic_parts if t]).strip()
    doc_root = _find_doc_root()
    if not doc_root:
        QMessageBox.information(win, "Help", "Could not locate 'doc' directory. Set FV_DOC_DIR or place doc/ next to fv.py.")
        return

    if topic.lower() == "list":
        # quick list in stdout so you can see what to call
        files = sorted([p.name for p in doc_root.glob("*.html")])
        print("[HELP] Available topics (filename → call with stem, e.g. 'imagedisplay'):")
        for f in files:
            print("   ", f)
        return

    # Resolve to a real HTML file (keeps your loose matching: "imagedisplay" / "image display" / "imageDisplay")
    path, err = _resolve_help_file(topic.split() if topic else None)
    if path is None:
        QMessageBox.information(win, "Help", err)
        return
    target_file = path.name  # e.g., imageDisplay.html

    # 2) Ensure CWD is the folder that contains 'doc/', since help.py uses os.getcwd()/doc
    #    (If you already run from project root, this is a no-op.)
    desired_cwd = str(doc_root.parent)
    try:
        if os.getcwd() != desired_cwd:
            os.chdir(desired_cwd)
    except Exception as e:
        print(f"[HELP] Warning: failed to chdir to {desired_cwd}: {e}")

    # 3) Open your in-house HelpWindow and select the right topic title
    try:
        import help as fvhelp  # your file with HelpWindow
        from help import HelpWindow  # class with dropdown and map
    except Exception as e:
        QMessageBox.information(win, "Help", f"help.py import failed: {e}")
        return

    try:
        help_win = HelpWindow()  # default topic is "Start FV"
        # Find display title whose filename matches the resolved page (case-insensitive)
        display_title = None
        for title, fname in getattr(help_win, "help_pages", {}).items():
            if fname.lower() == target_file.lower():
                display_title = title
                break

        if display_title:
            # This drives the dropdown; it also triggers load_topic internally.
            help_win.select_box.setCurrentText(display_title)
        else:
            print(f"[HELP] Could not find a matching dropdown title for {target_file}; showing default.")

        help_win.show()
        _set_last_widget(win, help_win)  # so SCREENSHOT/SAVEIMAGE target the help window next
        return
    except Exception as e:
        QMessageBox.information(win, "Help", f"Failed to open HelpWindow: {e}")
        return

def show_help_adapter_X(win, *topic_parts) -> None:
    topic = [t for t in topic_parts if t]
    path, err = _resolve_help_file(topic if topic else None)
    if path is None:
        QMessageBox.information(win, "Help", err)
        return

    # Special: list topics
    if path.name == "__LIST__":
        doc_root = _find_doc_root()
        files = sorted([p.name for p in doc_root.glob("*.html")]) if doc_root else []
        listing = "Available help topics:\n" + "\n".join(files) if files else "No topics found."
        dlg = QDialog(win); dlg.setWindowTitle("FV Help — Topics")
        lay = QVBoxLayout(dlg); tb = QTextBrowser(dlg)
        tb.setPlainText(listing + "\n\nTip: HELP <topic>  (e.g., HELP image display)")
        lay.addWidget(tb); dlg.resize(700, 600); dlg.show()
        _set_last_widget(win, dlg)
        return

    doc_root = path.parent
    start_file = path.name
    full_path = str(path)

    # Use your in-house help module
    try:
        import help as fvhelp  # your module

        # If your help module wants a doc root, try to set it
        if hasattr(fvhelp, "DOC_ROOT"):
            fvhelp.DOC_ROOT = str(doc_root)
        elif hasattr(fvhelp, "setDocRoot"):
            try: fvhelp.setDocRoot(str(doc_root))
            except Exception: pass

        # Try common entry points
        # a) showHelp(parent, topic_or_path)
        try:
            dlg = fvhelp.showHelp(win, full_path)
            if dlg is None: dlg = QApplication.activeWindow()
            _set_last_widget(win, dlg)
            return
        except Exception:
            pass

        # b) showHelp(parent, start_file)  (doc root set above)
        try:
            dlg = fvhelp.showHelp(win, start_file)
            if dlg is None: dlg = QApplication.activeWindow()
            _set_last_widget(win, dlg)
            return
        except Exception:
            pass

        # c) callHelp(parent, path)
        try:
            dlg = fvhelp.callHelp(win, full_path)
            if dlg is None: dlg = QApplication.activeWindow()
            _set_last_widget(win, dlg)
            return
        except Exception:
            pass

        # d) Class-based API: HelpWindow / HelpBrowser / Browser / WebWindow
        for clsname in ("HelpWindow", "HelpBrowser", "Browser", "WebWindow"):
            if hasattr(fvhelp, clsname):
                try:
                    cls = getattr(fvhelp, clsname)
                    try:
                        dlg = cls(parent=win, doc_root=str(doc_root), start_page=start_file)
                    except Exception:
                        try: dlg = cls(win, str(doc_root), start_file)
                        except Exception:
                            dlg = cls(win, full_path)
                    dlg.resize(900, 700); dlg.show()
                    _set_last_widget(win, dlg)
                    return
                except Exception:
                    continue

        # e) Function open/openFile/openUrl
        for fn in ("openFile", "openUrl", "open"):
            if hasattr(fvhelp, fn):
                try:
                    dlg = getattr(fvhelp, fn)(full_path)
                    if dlg is None: dlg = QApplication.activeWindow()
                    _set_last_widget(win, dlg)
                    return
                except Exception:
                    pass

        # If none matched, fall back to a simple QTextBrowser (still no WebEngine)
        dlg = QDialog(win); dlg.setWindowTitle(f"FV Help — {start_file}")
        lay = QVBoxLayout(dlg); tb = QTextBrowser(dlg)
        tb.setSource(QUrl.fromLocalFile(full_path))
        lay.addWidget(tb); dlg.resize(900, 700); dlg.show()
        _set_last_widget(win, dlg)
        return

    except Exception:
        # help.py import failed — fallback to QTextBrowser only
        dlg = QDialog(win); dlg.setWindowTitle(f"FV Help — {start_file}")
        lay = QVBoxLayout(dlg); tb = QTextBrowser(dlg)
        tb.setSource(QUrl.fromLocalFile(full_path))
        lay.addWidget(tb); dlg.resize(900, 700); dlg.show()
        _set_last_widget(win, dlg)

def show_help_adapter_X(win, *topic_parts) -> None:
    """
    HELP                -> open main Help window
    HELP <topic words>  -> open Help on a specific topic (e.g., 'summary', 'image', 'table')
    Uses your help.py: showHelp(parent, topic=None) or callHelp(parent).
    """
    topic = " ".join([t for t in topic_parts if t]).strip() or None
    try:
        # Prefer showHelp if available; fall back to callHelp
        try:
            from help import showHelp  # type: ignore
            dlg = showHelp(win, topic) if topic else showHelp(win)
        except Exception:
            from help import callHelp  # type: ignore
            dlg = callHelp(win)

        # Track the opened help window for SCREENSHOT/SAVEIMAGE targeting
        try:
            _set_last_widget(win, dlg if dlg is not None else QApplication.activeWindow())
        except Exception:
            pass
        return
    except Exception as e:
        from PyQt6.QtWidgets import QMessageBox
        QMessageBox.information(win, "Help", f"Unable to open Help: {e}")

def _set_last_widget(win, w: QWidget | None):
    if w is not None:
        win._fv_last_widget = w
        # keep a strong ref so it doesn't get GC'd
        if hasattr(win, "_fv_refs"):
            win._fv_refs.append(w)

def _pick_target_widget_for_screenshot(win) -> QWidget:
    """
    Preference order:
      1) Most recently opened dialog/viewer (_fv_last_widget)
      2) QApplication.activeWindow()
      3) The FV main window (win)
    """
    w = getattr(win, "_fv_last_widget", None)
    if isinstance(w, QWidget) and w.isVisible():
        return w
    aw = QApplication.activeWindow()
    if isinstance(aw, QWidget) and aw.isVisible():
        return aw
    return win

def _find_matplotlib_canvas(widget: QWidget | None):
    """Return a Matplotlib Figure or Canvas if present under widget, else None."""
    try:
        from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
    except Exception:
        FigureCanvas = None
    if widget is None:
        return None
    if FigureCanvas and isinstance(widget, FigureCanvas):
        return widget.figure
    # Search children (depth-1 is usually enough)
    for ch in widget.findChildren(QWidget):
        if FigureCanvas and isinstance(ch, FigureCanvas):
            return ch.figure
    # Fallback to stored figs
    fig = getattr(widget, "_fv_image_fig", None) or getattr(widget, "_fv_plot_fig", None)
    if fig is not None:
        return fig
    return None

def build_main_window_adapter():
    """
    Use FV’s real main window from fv.py instead of a stub.
    """
    from fv import FV # adjust to match your fv.py
    win = FV()

    # make sure we attach the same harness refs
    win._fv_refs = []
    win._fv_current_path = None
    win._fv_summary = None
    win._fv_image_fig = None
    win._fv_plot_fig = None

    return win

def build_main_window_adapter_X():
    """
    Main FV Harness panel with an Exit button.
    """
    from PyQt6.QtWidgets import QMainWindow, QWidget, QPushButton, QVBoxLayout

    w = QMainWindow()
    w.setWindowTitle("FV Harness")
    w.resize(300, 120)   # make it smaller

    # Central widget with just an Exit button
    central = QWidget()
    layout = QVBoxLayout(central)

    exit_btn = QPushButton("Exit")
    exit_btn.setFixedHeight(40)
    exit_btn.clicked.connect(QApplication.instance().quit)
    layout.addWidget(exit_btn)

    w.setCentralWidget(central)

    # Keep refs for dialogs/plots
    w._fv_refs = []
    w._fv_current_path = None
    w._fv_summary = None
    w._fv_image_fig = None
    w._fv_plot_fig = None

    return w

from astropy.io import fits
from astropy.io.fits import BinTableHDU, TableHDU, ImageHDU, PrimaryHDU

def _scan_table_hdus(path: str):
    """Return list of table HDU indices."""
    idxs = []
    with fits.open(path) as hdul:
        for i, h in enumerate(hdul):
            if isinstance(h, (BinTableHDU, TableHDU)):
                idxs.append(i)
    return idxs

def _scan_image_hdus(path: str):
    """Return list of image HDU indices (including PrimaryHDU with 2D+ data)."""
    idxs = []
    with fits.open(path) as hdul:
        for i, h in enumerate(hdul):
            if isinstance(h, (PrimaryHDU, ImageHDU)):
                d = getattr(h, "data", None)
                if d is not None and getattr(d, "ndim", 0) >= 2:
                    idxs.append(i)
    return idxs


def _scan_hdus_for_tables(path: str):
    """
    Returns a list of dicts describing table HDUs.
    [
      {"idx": 1, "kind": "BinTableHDU", "nrows": 2928, "ncols": 7, "colnames": [...]},
      ...
    ]
    """
    out = []
    with fits.open(path) as hdul:
        for i, h in enumerate(hdul):
            if isinstance(h, (BinTableHDU, TableHDU)):
                names = list(h.columns.names or [])
                out.append({
                    "idx": i,
                    "kind": h.__class__.__name__,
                    "nrows": int(getattr(h.data, "shape", (0,))[0] or 0),
                    "ncols": len(names),
                    "colnames": names,
                })
    return out

def _hdu_kind(h):
    if isinstance(h, PrimaryHDU): return "PrimaryHDU"
    if isinstance(h, ImageHDU):   return "ImageHDU"
    if isinstance(h, (BinTableHDU, TableHDU)): return h.__class__.__name__
    return h.__class__.__name__

def _first_image_hdu_index(path: str) -> int | None:
    with fits.open(path) as hdul:
        for i, h in enumerate(hdul):
            d = getattr(h, "data", None)
            if d is not None and getattr(d, "ndim", 0) >= 2:
                return i
    return None

def _first_table_hdu_with_columns(path: str, xcol: str, ycol: str) -> int | None:
    with fits.open(path) as hdul:
        for i, h in enumerate(hdul):
            data = getattr(h, "data", None)
            if data is not None and hasattr(data, "columns"):
                names = list(data.columns.names or [])
                if xcol in names and ycol in names:
                    return i
    return None

def _log_hdu_overview(path: str):
    from astropy.io import fits
    with fits.open(path) as hdul:
        print("[i] HDU overview:")
        for i, h in enumerate(hdul):
            kind = _hdu_kind(h)
            shape = getattr(getattr(h, "data", None), "shape", None)
            print(f"    HDU {i}: {kind}  shape={shape}")

def _parse_header_table_spec(spec: str):
    """
    Parse TABLE/HEADER spec:
      - 'all' or '*'        -> ("all", None)
      - 'true'/'false' etc. -> ("bool", True/False)
      - 'N'                 -> ("indices", [N])
      - 'N,M,K' (CSV)       -> ("indices", [N,M,K])  # spaces ok

    Raises ValueError for bad tokens.
    """
    s = str(spec).strip()
    low = s.lower()

    if low in ("all", "*"):
        return ("all", None)

    # boolean forms
    if low in ("1", "true", "t", "yes", "y", "on"):
        return ("bool", True)
    if low in ("0", "false", "f", "no", "n", "off"):
        return ("bool", False)

    # CSV of integers
    parts = [p.strip() for p in s.split(",")]
    idxs = []
    for p in parts:
        if not p:
            continue
        if not p.isdigit():
            raise ValueError(f"Invalid index token: '{p}'")
        idxs.append(int(p))

    if not idxs:
        # If they passed an empty/invalid string, treat as True (default behavior)
        return ("bool", True)

    # Preserve the given order, remove duplicates while preserving order
    seen = set()
    ordered = []
    for i in idxs:
        if i not in seen:
            seen.add(i)
            ordered.append(i)
    return ("indices", ordered)

def open_fits_adapter(win, path: str) -> None:
    """
    Store the file path and (optionally) precompute summary_data.
    If your dialog can handle None, we can skip precompute.
    """
    win._fv_current_path = path
    win._fv_summary = None  # FitsSummaryDialog can build from the file itself

import io
import contextlib

def show_summary_adapter(win) -> None:
    if not getattr(win, "_fv_current_path", None):
        from PyQt6.QtWidgets import QMessageBox
        QMessageBox.information(win, "Summary", "No file is open. Use OPEN <path> first.")
        return
    try:
        summary = win.load_summary_data(win._fv_current_path, progress_callback=None)
        win._fv_summary = summary
        dlg = win.show_summary_dialog(win._fv_current_path, summary)
        # Some versions return None; in that case, use activeWindow
        if dlg is not None:
            _set_last_widget(win, dlg)
        else:
            _set_last_widget(win, QApplication.activeWindow())
    except Exception as e:
        from PyQt6.QtWidgets import QMessageBox
        QMessageBox.critical(win, "Summary", f"Failed to load summary:\n{e}")

def show_header_adapter(win, spec: str) -> None:
    """
    HEADER all       -> show header for every HDU
    HEADER N         -> show header for HDU N
    HEADER N,M,K     -> show header for specified HDUs
    HEADER true/false-> legacy (true = HDU 0, false = no-op)
    """
    kind, val = _parse_header_table_spec(spec)
    if kind == "bool" and not val:
        return

    from astropy.io import fits

    # Determine which HDUs to open
    indices = []
    with fits.open(win._fv_current_path) as hdul:
        if kind == "all":
            indices = list(range(len(hdul)))
        elif kind == "indices":
            indices = val
        else:  # bool True or default
            indices = [0]

        # Clamp to valid range, warn on any out-of-range
        max_idx = len(hdul) - 1
        valid = []
        for i in indices:
            if 0 <= i <= max_idx:
                valid.append(i)
            else:
                print(f"[i] HEADER: skip invalid HDU {i} (valid 0..{max_idx})")
        indices = valid
        if not indices:
            return

    # Try native dialog first; otherwise fallback text viewer
    try:
        from header import show_header_dialog  # (parent, fits_file, hdu_index, header_text)
        use_native = True
    except Exception:
        use_native = False

    for idx in indices:
        try:
            with fits.open(win._fv_current_path) as hdul:
                header_text = hdul[idx].header.tostring(sep="\n")
        except Exception as ee:
            header_text = f"[Error loading header for HDU {idx}: {ee}]"

        if use_native:
            try:
                dlg = show_header_dialog(win, win._fv_current_path, idx, header_text)
                if isinstance(dlg, QDialog):
                    win._fv_refs.append(dlg)
                continue
            except Exception as e:
                print(f"[i] header native dialog failed for HDU {idx}: {e}; using fallback.")

        # Fallback dialog
        dlg = QDialog(win)
        dlg.setWindowTitle(f"FITS Header — HDU {idx}")
        lay = QVBoxLayout(dlg)
        te = QTextEdit(dlg); te.setReadOnly(True); te.setPlainText(header_text)
        lay.addWidget(te)
        dlg.resize(900, 650)
        dlg.show()
        win._fv_refs.append(dlg)

def show_table_adapter(win, spec: str) -> None:
    """
    TABLE all        -> open table for all *table HDUs*; if none, try all *image HDUs*
    TABLE N          -> open table for HDU N (table or image)
    TABLE N,M,K      -> open table for listed HDUs (table or image)
    TABLE true/false -> legacy (true = first table HDU, else first image HDU; false = no-op)
    Native dialog only (no fallback tiles).
    """
    kind, val = _parse_header_table_spec(spec)
    if kind == "bool" and not val:
        return

    # Build candidate indices (tables first, else images)
    tbl_idxs = _scan_table_hdus(win._fv_current_path)
    img_idxs = _scan_image_hdus(win._fv_current_path)

    if kind == "all":
        indices = tbl_idxs if tbl_idxs else img_idxs
    elif kind == "indices":
        exists = set(tbl_idxs) | set(img_idxs)
        indices = [i for i in val if i in exists]
        for i in val:
            if i not in exists:
                print(f"[i] TABLE: HDU {i} not available as table or image; skipping.")
    else:
        indices = tbl_idxs[:1] if tbl_idxs else img_idxs[:1]

    if not indices:
        msg = "No table or image HDUs found to display as a table."
        if 'QUIET' in globals() and QUIET:
            print(f"[i] TABLE: {msg}")
            return
        QMessageBox.information(win, "Table View", msg)
        return

    # Native dialog only
    try:
        from table import show_table_dialog  # (parent, fits_file, hdu_index)
    except Exception as e:
        # No native dialog available — honor quiet mode, otherwise inform.
        msg = f"Native table dialog not available: {e}"
        if 'QUIET' in globals() and QUIET:
            print(f"[i] TABLE: {msg}")
            return
        QMessageBox.information(win, "Table View", msg)
        return

    # Open one native dialog per requested HDU; do NOT fall back
    for idx in indices:
        try:
            dlg = show_table_dialog(win, win._fv_current_path, hdu_index=idx)
            _set_last_widget(win, dlg if dlg is not None else QApplication.activeWindow())

            if isinstance(dlg, QDialog):
                win._fv_refs.append(dlg)
        except Exception as e:
            # Log and continue; still no fallback tiles
            print(f"[i] TABLE: native dialog failed for HDU {idx}: {e}")

def show_image_adapter(win, spec: str | None = None) -> None:
    """
    IMAGE            -> open first image HDU
    IMAGE all        -> open all image HDUs (one POW viewer per HDU)
    IMAGE N          -> open image HDU N
    IMAGE N,M,K      -> open listed image HDUs
    """
    try:
        from pow import FITSViewer
    except Exception as e:
        print(f"[i] show_image_adapter: POW not available ({e}); using fallback.")
        return _show_image_fallback(win)

    # Determine indices
    from astropy.io import fits
    with fits.open(win._fv_current_path) as hdul:
        img_idxs = [i for i,h in enumerate(hdul)
                    if getattr(h, "data", None) is not None and getattr(h.data, "ndim", 0) >= 2]

    if not img_idxs:
        msg = "No image HDU found."
        if QUIET:
            print(f"[i] IMAGE: {msg}")
            return
        QMessageBox.information(win, "Image", msg)
        return

    # Default behavior
    indices = img_idxs[:1]

    # If a spec string was provided, parse it like HEADER/TABLE
    if spec is not None:
        kind, val = _parse_header_table_spec(spec)
        if kind == "all":
            indices = img_idxs
        elif kind == "indices":
            indices = [i for i in val if i in img_idxs]
            dropped = [i for i in val if i not in img_idxs]
            for i in dropped:
                print(f"[i] IMAGE: HDU {i} is not an image; skipping.")
            if not indices:
                msg = "No requested indices are image HDUs."
                if QUIET:
                    print(f"[i] IMAGE: {msg}")
                    return
                QMessageBox.information(win, "Image", msg)
                return
        # kind == "bool": keep default (first image)

    # Launch POW viewers
    for idx in indices:
        viewer = FITSViewer(win._fv_current_path, mode="image", hdu_index=idx, col_x=None, col_y=None)
        viewer.resize(1000, 800)
        viewer.show()
        _set_last_widget(win, viewer)
        win._fv_refs.append(viewer)

def _show_image_fallback(win):
    # (optional) keep your old matplotlib fallback here if you still want it as a plan B
    import matplotlib as mpl
    mpl.use("QtAgg", force=True)
    import matplotlib.pyplot as plt
    from astropy.io import fits
    import numpy as np

    with fits.open(win._fv_current_path) as hdul:
        img_hdu = next((h for h in hdul if getattr(h, "data", None) is not None and getattr(h.data, "ndim", 0) >= 2), None)
        if img_hdu is None:
            QMessageBox.information(win, "Image", "No image HDU found.")
            return
        data = img_hdu.data.astype(float)
        vmin, vmax = np.nanpercentile(data, [1, 99])
        fig = plt.figure()
        ax = fig.add_subplot(111)
        im = ax.imshow(data, origin="lower", vmin=vmin, vmax=vmax)
        ax.set_title("Image HDU (fallback viewer)")
        fig.colorbar(im, ax=ax)
        try:
            fig.canvas.manager.set_window_title("FV Image (harness)")
        except Exception:
            pass
        fig.show()
        win._fv_image_fig = fig
        win._fv_refs.append(fig)

def plot_xy_adapter(win, xcol: str, ycol: str) -> None:
    """
    Prefer POW; else fallback scatter. Picks the first table HDU that has BOTH columns.
    """
    try:
        from pow import FITSViewer
        idx = _first_table_hdu_with_columns(win._fv_current_path, xcol, ycol)
        if idx is None:
            # help the user by listing table HDUs + their columns
            tables = _scan_hdus_for_tables(win._fv_current_path)
            if not tables:
                QMessageBox.information(win, "POW Plot", "No table HDUs found in this FITS.")
                return
            lines = []
            for t in tables:
                lines.append(f"HDU {t['idx']} ({t['kind']}): {t['colnames']}")
            QMessageBox.information(win, "POW Plot",
                f"No HDU has both '{xcol}' and '{ycol}'.\nAvailable columns:\n" + "\n".join(lines))
            return
        viewer = FITSViewer(win._fv_current_path, mode="plot", hdu_index=idx, col_x=xcol, col_y=ycol)
        viewer.resize(1000, 800)
        viewer.show()
        _set_last_widget(win, viewer)
        win._fv_refs.append(viewer)
        return
    except Exception:
        pass
    # … keep your matplotlib fallback here (unchanged) …

def _plot_fallback(win, xcol: str, ycol: str):
    import matplotlib as mpl
    mpl.use("QtAgg", force=True)
    import matplotlib.pyplot as plt
    from astropy.io import fits
    import numpy as np

    with fits.open(win._fv_current_path) as hdul:
        table_hdu = None
        for h in hdul:
            d = getattr(h, "data", None)
            if d is not None and hasattr(d, "columns"):
                table_hdu = h
                break
        if table_hdu is None:
            QMessageBox.information(win, "POW Plot", "No table HDUs found.")
            return
        cols = list(table_hdu.columns.names or [])
        if xcol not in cols or ycol not in cols:
            QMessageBox.information(win, "POW Plot", f"Columns not found in first table HDU.\nAvailable: {cols}")
            return
        x = np.array(table_hdu.data[xcol], dtype=float)
        y = np.array(table_hdu.data[ycol], dtype=float)
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(x, y, linestyle="none", marker=".", markersize=3)
        ax.set_xlabel(xcol); ax.set_ylabel(ycol); ax.set_title(f"{ycol} vs {xcol} (fallback plot)")
        try: fig.canvas.manager.set_window_title("POW Plot (harness)")
        except Exception: pass
        fig.show()
        win._fv_plot_fig = fig
        win._fv_refs.append(fig)

def take_screenshot_adapter(win, out_path: str) -> None:
    target = _pick_target_widget_for_screenshot(win)
    pix = target.grab()
    pix.save(out_path, "PNG")


def save_image_canvas_adapter(win, out_path: str) -> None:
    """
    Try to export just the image/plot canvas from the last viewer.
    Order:
      1) Matplotlib figure under the last widget
      2) Known canvas attributes on last widget or main window
      3) Fallback: screenshot of last/active window
    """
    lastw = getattr(win, "_fv_last_widget", None)

    # 1) Matplotlib figure?
    fig = _find_matplotlib_canvas(lastw)
    if fig is None:
        fig = getattr(win, "_fv_image_fig", None) or getattr(win, "_fv_plot_fig", None)
    if fig is not None:
        try:
            fig.savefig(out_path, dpi=150, bbox_inches="tight")
            return
        except Exception:
            pass

    # 2) Known QWidget canvas attributes (if your FV exposes them)
    for owner in (lastw, win):
        if owner is None:
            continue
        for name in ("imageCanvas", "plotCanvas", "canvas", "centralWidget"):
            canvas = getattr(owner, name, None)
            if hasattr(canvas, "grab"):
                pix = canvas.grab()
                try:
                    pix.save(out_path, "PNG")
                    return
                except Exception:
                    continue

    # 3) Fallback: window screenshot of the last/active window
    take_screenshot_adapter(win, out_path)

# ============
# COMMANDS API
# ============

@dataclass
class Command:
    name: str
    args: List[str]


class CommandRunner:
    """
    Runs commands on the Qt event loop, one per tick, so the UI remains responsive.
    """
    def __init__(self, app: QApplication, win, commands: List[Command], delay_ms: int = 250, auto_quit: bool = False):
        self.app = app
        self.win = win
        self.commands = commands
        self.delay_ms = delay_ms
        self.auto_quit = auto_quit

    def start(self):
        self.win.show()
        self.win.raise_()
        self.win.activateWindow()
        QTimer.singleShot(self.delay_ms, self._step)

    def _step(self):
        if not self.commands:
            if self.auto_quit:
                QTimer.singleShot(150, self.app.quit)
            return

        cmd = self.commands.pop(0)
        try:
            self._execute(cmd)
        except Exception as e:
            print(f"[!] Command '{cmd.name}' failed: {e}", file=sys.stderr)
        finally:
            # _execute may schedule its own wait (SLEEP); guard to avoid double scheduling
            if cmd.name.upper() != "SLEEP":
                QTimer.singleShot(self.delay_ms, self._step)

    def _execute(self, cmd: Command):
        n = cmd.name.upper()
        a = cmd.args

        if n in ("OPEN", "--FILE"):
            path = a[0]
            print(f"[i] OPEN {path}")
            open_fits_adapter(self.win, path)

        elif n in ("HELP", "--HELP"):
            # Accept: HELP        or  HELP <topic words...>
            print(f"[i] HELP {' '.join(a) if a else ''}".rstrip())
            show_help_adapter(self.win, *a)

        elif n in ("SUMMARY", "--SUMMARY"):
            print("[i] SUMMARY")
            show_summary_adapter(self.win)

        elif n in ("IMAGE", "--IMAGE"):
            spec = a[0] if a else None
            print(f"[i] IMAGE {spec if spec else ''}".rstrip())
            show_image_adapter(self.win, spec)

        elif n in ("TABLE", "--SHOWTABLE"):
            # Accept: TABLE all | TABLE <index> | TABLE true/false (legacy)
            spec = a[0] if a else "true"
            print(f"[i] TABLE {spec}")
            show_table_adapter(self.win, spec)

        elif n in ("HEADER", "--SHOWHEADER"):
            # Accept: HEADER all | HEADER <index> | HEADER true/false (legacy)
            spec = a[0] if a else "true"
            print(f"[i] HEADER {spec}")
            show_header_adapter(self.win, spec)

        elif n in ("PLOT", "--PLOT"):
            if len(a) < 2:
                raise ValueError("PLOT requires two args: <xcol> <ycol>")
            xcol, ycol = a[0], a[1]
            print(f"[i] PLOT {xcol} vs {ycol}")
            plot_xy_adapter(self.win, xcol, ycol)

        elif n in ("SCREENSHOT", "--SCREENSHOT"):
            out = a[0]
            if len(a) > 1 and a[1].lower() == "active":
                _set_last_widget(self.win, QApplication.activeWindow())
            print(f"[i] SCREENSHOT -> {out}")
            take_screenshot_adapter(self.win, out)

        elif n in ("SAVEIMAGE", "--SAVEIMAGE"):
            out = a[0]
            if len(a) > 1 and a[1].lower() == "active":
                _set_last_widget(self.win, QApplication.activeWindow())
            print(f"[i] SAVEIMAGE -> {out}")
            save_image_canvas_adapter(self.win, out)

        elif n == "SLEEP":
            ms = int(a[0]) if a else 250
            print(f"[i] SLEEP {ms}ms")
            QTimer.singleShot(ms, self._step)

        elif n in ("QUIT", "--QUIT"):
            print("[i] QUIT")
            QTimer.singleShot(50, self.app.quit)

        else:
            print(f"[?] Unknown command: {cmd.name} {' '.join(cmd.args)}")


# ==========
# UTILITIES
# ==========

def parse_bool(s: str) -> bool:
    return str(s).strip().lower() in ("1", "true", "t", "yes", "y", "on")


def parse_script_lines(lines: List[str]) -> List[Command]:
    cmds: List[Command] = []
    for raw in lines:
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        cmds.append(Command(parts[0], parts[1:]))
    return cmds


def cli_to_commands(args) -> List[Command]:
    cmds: List[Command] = []

    if args.fvhelp is not None:
        # args.fvhelp is [] when called with no topic
        cmds.append(Command("--HELP", args.fvhelp))
    if args.file:
        cmds.append(Command("--FILE", [args.file]))
    if args.summary:
        cmds.append(Command("--SUMMARY", []))
    if args.image:
        cmds.append(Command("--IMAGE", []))
    if args.showheader is not None:
        cmds.append(Command("--SHOWHEADER", [str(args.showheader)]))
    if args.showtable is not None:
        cmds.append(Command("--SHOWTABLE", [str(args.showtable)]))
    if args.plot:
        if len(args.plot) != 2:
            raise SystemExit("--plot needs exactly two args: <xcol> <ycol>")
        cmds.append(Command("--PLOT", list(args.plot)))
    if args.screenshot:
        cmds.append(Command("--SCREENSHOT", [args.screenshot]))
    if args.saveimage:
        cmds.append(Command("--SAVEIMAGE", [args.saveimage]))
    if args.quit:
        cmds.append(Command("--QUIT", []))
    return cmds


# =====
# MAIN
# =====

def main():
    global QUIET

    ap = argparse.ArgumentParser(description="CLI harness to drive Python FV/POW without modifying your app.")
    ap.add_argument("--script", help="Path to a command script (OPEN, SUMMARY, IMAGE, TABLE, HEADER, PLOT, SCREENSHOT, SAVEIMAGE, SLEEP, QUIT)")
    ap.add_argument("--file", help="Open a FITS file (equivalent to: OPEN <path>)")
    ap.add_argument("--summary", action="store_true", help="Show the summary view (equivalent to: SUMMARY)")
    ap.add_argument("--image", action="store_true", help="Show the image view (equivalent to: IMAGE)")
    ap.add_argument("--plot", nargs=2, metavar=("XCOL", "YCOL"), help="Plot table columns with POW/fallback")
    ap.add_argument("--showheader", nargs="?", const="true", metavar="SPEC", help="HEADER spec: all | N | N,M,K | true/false (default if omitted: true)")
    ap.add_argument( "--showtable", nargs="?", const="true", metavar="SPEC", help="TABLE spec: all | N | N,M,K | true/false (default if omitted: true)")
    ap.add_argument("--screenshot", help="Save a PNG of the whole window")
    ap.add_argument("--saveimage", help="Save only the image/plot canvas to PNG")
    ap.add_argument("--quit", action="store_true", help="Quit after executing commands")
    ap.add_argument("--delay", type=int, default=250, help="Delay (ms) between commands")
    ap.add_argument("--quiet", action="store_true", help="Suppress info popups (log to stdout instead)")
    ap.add_argument("--fvhelp", nargs="*", metavar="TOPIC", help="Open FV Help (optionally with a topic)")

    args = ap.parse_args()
    QUIET = args.quiet

    commands: List[Command] = []
    if args.script:
        with open(args.script, "r", encoding="utf-8") as f:
            commands.extend(parse_script_lines(f.readlines()))
    # CLI flags append after (override/extend script)
    commands.extend(cli_to_commands(args))

    if not commands:
        print("No commands given. Use --script or flags like --file/--summary/--image/--plot/--screenshot/--saveimage/--quit.")
        sys.exit(1)

    app = QApplication.instance() or QApplication(sys.argv)
    win = build_main_window_adapter()
    runner = CommandRunner(app, win, commands, delay_ms=args.delay, auto_quit=False)
    # If the final state should aut0-quit (explicit --quit), we’ll let the runner also see that command in the queue.
    # (If you prefer immediate auto-quit without needing a QUIT command, set auto_quit=args.quit)
    runner.start()
    app.exec()


if __name__ == "__main__":
    main()

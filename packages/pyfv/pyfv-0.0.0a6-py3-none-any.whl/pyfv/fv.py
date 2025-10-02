#!/opt/miniconda3/bin/python
# -----------------------------------------------------------------------------
# PyFV: A modern Python FITS Viewer
# Copyright (c) 2025, Pan S. Chai
# Distributed under the BSD 3-Clause License. See LICENSE file for details.
# -----------------------------------------------------------------------------
#
#  Python FV Project
#
#      module: fv.py
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
# Usage:
#
#   1. Run by executing this command INSIDE the directory
#
#          ./fv.py
#
#-------------------------------------------------------------------------------
#

import os
import PyQt6

# Ensure Qt can find the Cocoa plugin on macOS
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = os.path.join(
    os.path.dirname(PyQt6.__file__), "Qt6", "plugins", "platforms"
)

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

import time
import traceback, sys

# Path to THIS file (fv.py)
fv_dir = os.path.dirname(os.path.abspath(__file__))

# Path to pow.py in the same directory
help_path = os.path.join(fv_dir, "help.py")

#
# these modules are part of FV 
#

# from summary import callDialog, summarize_hdus, summarize_table_columns
from summary import *
        
def callDialog(parent):
    file_path, _ = QFileDialog.getOpenFileName(parent, "Select a file")
    return file_path

class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.
        
    Supported signals are:
        
    finished
        No data
        
    error   
        tuple (exctype, value, traceback.format_exc() )
            
    result  
        object data returned from processing, anything
        
    progress
        int indicating % progress
            
    '''
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(int)

class Worker(QRunnable):
    '''
    Worker thread
        
    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.
        
    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function
        
    ''' 

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        # Add the callback to our kwargs
        self.kwargs['progress_callback'] = self.signals.progress

    @pyqtSlot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''

        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done

class CollapsibleBox(QWidget):
    def __init__(self, title=""):
        global displayDeviceChoiceH

        super().__init__()
        self.select_title_button = QPushButton(title)
        self.select_title_button.clicked.connect(self.on_clicked)

        self.selection_area = QScrollArea(maximumHeight=0, minimumHeight=0)

        self.displayChoiceBox = QVBoxLayout(self)
        self.displayChoiceBox.setSpacing(0)
        self.displayChoiceBox.setContentsMargins(0, 0, 0, 0)
        self.displayChoiceBox.addWidget(self.select_title_button)
        self.displayChoiceBox.addWidget(self.selection_area)

    def on_clicked(self):
        global displayDeviceChoiceH
        global presetH

        ca_height = self.selection_area.height()
        widget = self.parent().parent().displayContainer

        if ca_height == 0:
           self.selection_area.setMaximumHeight(100)
           if displayDeviceChoiceH > 0:
              widget.setFixedHeight(displayDeviceChoiceH)
         
        else:
           self.selection_area.setMaximumHeight(0)
           widget.setFixedHeight(presetH)
           displayDeviceChoiceH = ca_height + presetH
  

class addSeparator(QFrame):

    def __init__(self):
        super().__init__()

        self.setMinimumWidth(1)
        self.setFixedHeight(20)
        self.setFrameShape(QFrame.Shape.HLine)
        # self.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        return

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class FV(QWidget) :

    def _remove_if_tracked(self, window):
        try:
            if window in self.open_windows:
                self.open_windows.remove(window)
        except Exception as e:
            print(f"[FV] Warning: Failed to remove window from open_windows: {e}")

    def callPreference(self):
        self.worker = Worker(self.showPreference)
        self.threadpool.start(self.worker)

    def showPreference(self, progress_callback):
        self.worker.p = QProcess()
        self.worker.p.start("python", ['preference.py'])

    def callHelp(self):
        p = QProcess(self)
        p.start("python", [help_path])
        # p.start("python", help_path)
        if not hasattr(self, "subprocesses"):
            self.subprocesses = []
        self.subprocesses.append(p)

    def show_summary_dialog(self, fits_file, summary_data):
        self.summary_dialog = FitsSummaryDialog(fits_file=fits_file, summary_data=summary_data, parent=self)
        self.summary_dialog.show()

        if not hasattr(self, 'open_windows'):
            self.open_windows = []
        self.open_windows.append(self.summary_dialog)

        # Use a safe wrapper to avoid ValueError
        self.summary_dialog.destroyed.connect(lambda _: self._remove_if_tracked(self.summary_dialog))

    def show_summary_dialog_X(self, fits_file, summary_data):
        self.summary_dialog = FitsSummaryDialog(fits_file=fits_file, summary_data=summary_data, parent=self)
        self.summary_dialog.show()

        if not hasattr(self, 'open_windows'):
            self.open_windows = []
        self.open_windows.append(self.summary_dialog)
        self.summary_dialog.destroyed.connect(lambda _: self.open_windows.remove(self.summary_dialog))

    def load_summary_data(self, fits_file, progress_callback=None):
        from astropy.io import fits
        summary = []

        with fits.open(fits_file) as hdulist:
            for idx, hdu in enumerate(hdulist):
                name = hdu.name.strip() or ("PRIMARY" if idx == 0 else f"HDU_{idx}")
                dimensions = str(hdu.shape) if hasattr(hdu, 'shape') else "N/A"
                dtype = type(hdu).__name__
                if dtype == "PrimaryHDU":
                    dtype = "Image"
                elif dtype == "BinTableHDU":
                    dtype = "Binary"

                view_type = "Binary" if dtype == "Binary" else "Image"
                summary.append((idx, name, dtype, dimensions, view_type))
    
        return summary

    def selectFile(self, progress_callback):
        fits_file = callDialog(self)
        if not fits_file:
            return

        # print("User selected:", fits_file)
        # self.statusBar().showMessage("Building FITS summary...")

        # Run background worker to extract HDU info
        worker = Worker(self.load_summary_data, fits_file)
        worker.signals.result.connect(lambda summary_data: self.show_summary_dialog(fits_file, summary_data))
        worker.signals.error.connect(self.handle_summary_error)
        # worker.signals.finished.connect(self.summary_finished)

        self.threadpool.start(worker)

    def build_summary_dialog(self, fits_file, progress_callback=None):
        return FitsSummaryDialog(fits_file, parent=self)

    def summary_finished(self):
        self.statusBar().clearMessage()

    def handle_summary_error(self, error_info):
        exctype, value, tb_str = error_info
        QMessageBox.critical(self, "Error", f"Error while opening FITS summary:\n{value}")
        print(tb_str)

    def selectFileX(self, progress_callback):
        #
        # select input file to continue
        #

        fits_file = callDialog(self)
        if fits_file:
            print("User selected:", fits_file);
        
        # Show HDU summary
        # summarize_hdus(fits_file)

        # Show table column details
        summary_panel = FitsSummaryDialog(fits_file, parent=self)
        summary_panel.exec()
 
        # summarize_all_hdus(fits_file)
        # display_hdu_header(fits_file, hdu_index=0)
        # display_hdu_header(fits_file)

        # summarize_table_columns(fits_file, hdu_index=1)

    def pow_state_changed(self, int):
        if self.check_pow.isChecked():
            self.check_pow.setChecked(True)
            self.check_ds9.setChecked(False)

    def ds9_state_changed(self, int):
        if self.check_ds9.isChecked():
            self.check_pow.setChecked(False)
            self.check_ds9.setChecked(True)

    def __init__(self):
        super().__init__()

        self.subprocesses = []
        self.initUI()

    def initUI(self):

        global displayDeviceChoiceH
        global presetH

        #
        #  fv main selection panel
        #

        fv_main = QVBoxLayout()

        self.threadpool = QThreadPool()
        self.threadpool.setExpiryTimeout(-1)
        
        #
        #  Choice:
        #
        #     New File
        #     Open File
        #     SkyView
        #     Catalogs
        #     VizieR
        #     Run Ftools
        #

        #self.newFile = QPushButton('New File..')
        #fv_main.addWidget(self.newFile)
        #self.newFile.clicked.connect(QApplication.instance().quit)

        self.openFile = QPushButton('Open File..')
        fv_main.addWidget(self.openFile)
        self.openFile.clicked.connect(self.selectFile);

        #self.skyView = QPushButton('SkyView..')
        #fv_main.addWidget(self.skyView)
        #self.skyView.clicked.connect(QApplication.instance().quit)

        #self.catalog = QPushButton('Catalogs..')
        #fv_main.addWidget(self.catalog)
        #self.catalog.clicked.connect(QApplication.instance().quit)

        #self.vizieR = QPushButton('VizieR..')
        #fv_main.addWidget(self.vizieR)
        #self.vizieR.clicked.connect(QApplication.instance().quit)

        #self.runFtool = QPushButton('Run Ftool..')
        #fv_main.addWidget(self.runFtool)
        #self.runFtool.clicked.connect(QApplication.instance().quit)

        #self.separator = addSeparator()
        #fv_main.addWidget(self.separator)

        #
        #  Choice:
        #
        #     Display Device
        #

        #self.displayDeviceBox = QVBoxLayout()
        #self.box = CollapsibleBox("Display Device")
        #self.displayDeviceBox.addWidget(self.box)

        #self.lay = QVBoxLayout()
        #self.check_pow = QCheckBox("POW")
        #self.lay.addWidget(self.check_pow)
        #self.check_pow.setChecked(True)

        #self.check_pow.stateChanged.connect(self.pow_state_changed)

        #self.check_ds9 = QCheckBox("DS9")
        #self.lay.addWidget(self.check_ds9)

        #self.check_ds9.stateChanged.connect(self.ds9_state_changed)

        #self.box.selection_area.setLayout(self.lay)

        #self.displayDeviceBox.addStretch()
        #self.displayContainer = QWidget()
        #self.displayContainer.setLayout(self.displayDeviceBox)

        #
        #  initialize the display Device Panel size to 0
        #
        #presetH = 50
        #displayDeviceChoiceH = 0

        #fv_main.addWidget(self.displayContainer)

        # fv_main.addWidget(Color('red'))
        #
        #  Choice:
        #
        #     Hide All Windows
        #     File Summary
        #     Header
        #     Table
        #     Image Table
        #     Vector Table
        #

        #self.separator = addSeparator()
        #fv_main.addWidget(self.separator)

        #self.hideAllWin = QPushButton('Hide All Windows')
        #fv_main.addWidget(self.hideAllWin)
        #self.hideAllWin.clicked.connect(QApplication.instance().quit)

        #self.fileSummary = QPushButton('File Summary')
        #fv_main.addWidget(self.fileSummary)
        #self.fileSummary.clicked.connect(QApplication.instance().quit)

        #self.header = QPushButton('Header')
        #fv_main.addWidget(self.header)
        #self.header.clicked.connect(QApplication.instance().quit)

        #self.table = QPushButton('Table')
        #fv_main.addWidget(self.table)
        #self.table.clicked.connect(QApplication.instance().quit)

        #self.imageTable = QPushButton('Imabge Table')
        #fv_main.addWidget(self.imageTable)
        #self.imageTable.clicked.connect(QApplication.instance().quit)

        #self.vectorTable = QPushButton('Vector Table')
        #fv_main.addWidget(self.vectorTable)
        #self.vectorTable.clicked.connect(QApplication.instance().quit)

        #self.separator = addSeparator()
        #fv_main.addWidget(self.separator)

        #
        #  Choice:
        #
        #     Preference
        #

        #self.preference = QPushButton('Preference')
        #fv_main.addWidget(self.preference)
        #self.preference.clicked.connect(self.callPreference)

        #self.separator = addSeparator()
        #fv_main.addWidget(self.separator)

        #
        #  Choice:
        #
        #     Clipboard
        #

        #self.clipboard = QPushButton('Clipboard')
        #fv_main.addWidget(self.clipboard)

        #self.clipboard.clicked.connect(QApplication.instance().quit)

        self.separator = addSeparator()
        fv_main.addWidget(self.separator)

        #
        #  Choice:
        #
        #     Help
        #     Quit
        #

        self.help = QPushButton('Help')
        fv_main.addWidget(self.help)
        self.help.clicked.connect(self.callHelp)

        self.quit = QPushButton('QUIT')
        fv_main.addWidget(self.quit)

        def safe_quit():
            try:
                if hasattr(self, "summary_dialog") and self.summary_dialog:
                    self.summary_dialog.close_all()
                for proc in getattr(self, "subprocesses", []):
                    if proc.state() != QProcess.ProcessState.NotRunning:
                        proc.terminate()
                        proc.waitForFinished(1000)
            except Exception as e:
                print(f"Error during cleanup: {e}")
            QApplication.instance().quit()

        self.quit.clicked.connect(safe_quit)

        #self.quit.clicked.connect(QApplication.instance().quit)

        #
        #  Set layout and title
        #

        self.setLayout(fv_main)
        self.setWindowTitle('FV')

        #
        #  Display the panel
        #

        self.show()



    def open_fits_summary(self, fits_file: str):
        """Open a FITS file directly and present the Summary panel.
        This mirrors selectFile() but skips the file dialog and can be
        triggered from the command line.
        """
        try:
            import os
            if not fits_file or not os.path.exists(fits_file):
                QMessageBox.warning(self, "Open FITS", f"File not found:\n{fits_file}")
                return

            # Start background worker to build summary data, then show dialog
            worker = Worker(self.load_summary_data, fits_file)
            worker.signals.result.connect(lambda summary_data: self.show_summary_dialog(fits_file, summary_data))
            worker.signals.error.connect(self.handle_summary_error)
            self.threadpool.start(worker)
        except Exception as e:
            QMessageBox.critical(self, "Open FITS Error", str(e))

def main():

    import argparse
    parser = argparse.ArgumentParser(prog="fv", description="PyFV - Python FITS Viewer")
    parser.add_argument("fits", nargs="?", help="Path to a FITS file to open and summarize at startup")
    args, unknown = parser.parse_known_args()

    # Rebuild sys.argv for Qt (drop our parsed args but keep unknown for Qt if any)
    sys.argv = [sys.argv[0]] + unknown

    app = QApplication(sys.argv)
    ex = FV()

    if args.fits:
        ex.open_fits_summary(args.fits)

    sys.exit(app.exec())
if __name__ == '__main__':
    main()


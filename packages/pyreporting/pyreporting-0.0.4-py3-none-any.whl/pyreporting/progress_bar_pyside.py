"""Pyside implementation of ProgressBar"""

from PySide6 import QtCore
from PySide6.QtCore import QCoreApplication, QObject, Qt, Signal
from PySide6.QtWidgets import QProgressDialog

from pyreporting.progress_bar import ProgressBar


class PySideProgressBar(ProgressBar):
    """A Pyside implementation of ProgressBar"""

    class PySideProgressBarSignals(QObject):
        """Signals used to trigger an update of the progress bar. The trigger
        can be from a worker thread by the GUI is updated on the main thread"""
        update = Signal(object, object, object)
        destroy = Signal()

    def __init__(self, parent: QObject, **kwargs):
        self.cancelled = False
        self.maximum = 100
        self.pyside_progress_bar = None
        self.signals = PySideProgressBar.PySideProgressBarSignals()
        self.signals.update.connect(self._update_signalled)
        self.signals.destroy.connect(self._destroy_signalled)
        super().__init__(parent=parent, **kwargs)

        # pylint:disable-next=c-extension-no-member
        if not QtCore.QThread.currentThread() == \
               QCoreApplication.instance().thread():
            raise RuntimeError("PySideProgressBar() should be created on the "
                               "main GUI thread")

    def update(self,
               label: str or None = None,
               value: int or None = None,
               title: str or None = None):
        """Trigger a signal to create or update the current progress dialog"""
        self.signals.update.emit(label, value, title)

    def close(self):
        """Trigger a signal to destroy the current progress dialog"""

        # Important to disconnect to avoid cancel signals from the old dialog
        # coming through while the new one is being created
        if self.pyside_progress_bar:
            self.pyside_progress_bar.canceled.disconnect()
        self.signals.destroy.emit()
        self.cancelled = False

    def cancel_clicked(self) -> bool:
        """Check if the cancel button has been clicked"""
        return self.cancelled

    def _update_signalled(self,
                          label: str or None = None,
                          value: int or None = None,
                          title: str or None = None):
        """Called on main thread to process an update request"""
        if not self.pyside_progress_bar:
            self.pyside_progress_bar = QProgressDialog(
                parent=self.parent,
                labelText=label,
                minimum=0,
                maximum=self.maximum
            )
            self.pyside_progress_bar.setMinimumDuration(0)
            self.pyside_progress_bar.setAutoReset(False)
            self.pyside_progress_bar.setAutoClose(False)
            self.pyside_progress_bar.setWindowModality(Qt.WindowModal)
            self.pyside_progress_bar.setWindowTitle(title)
            self.cancelled = False
            self.pyside_progress_bar.canceled.connect(self._cancel_signalled)
            if value is None:
                self.pyside_progress_bar.setRange(0, 0)
                self.pyside_progress_bar.setValue(0)

        if label is not None:
            self.pyside_progress_bar.setLabelText(label)

        if title is not None:
            self.pyside_progress_bar.setWindowTitle(title)

        # Note: setValue() must be the last call, because it can trigger
        # QApplication.processEvents() which could start processing the next
        # event before this one has completed
        if value is not None:
            if value == -1:
                self.pyside_progress_bar.setRange(0, 0)
                self.pyside_progress_bar.setValue(0)
            else:
                self.pyside_progress_bar.setRange(0, self.maximum)
                self.pyside_progress_bar.setValue(value)

    def _destroy_signalled(self):
        """Called on main thread to process a progress destroy request"""
        if self.pyside_progress_bar:
            self.pyside_progress_bar.close()
            self.pyside_progress_bar.deleteLater()
            self.pyside_progress_bar = None

    def _cancel_signalled(self):
        self.cancelled = True

import sys

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog
from single_signal_multiple_slot_ui import Ui_Form
from PySide6.QtCore import QFileInfo
from PySide6.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.horizontalSlider.valueChanged.connect(self.ui.progressBar.setValue)        
        self.ui.horizontalSlider.sliderMoved.connect(self.ui.lcdNumber.display)        

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
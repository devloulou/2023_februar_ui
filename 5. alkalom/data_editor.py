import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHeaderView, QMessageBox
from PySide6.QtGui import QStandardItemModel, QStandardItem

from data_editor_ui_ui import Ui_Form

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
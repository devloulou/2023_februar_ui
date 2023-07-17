import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('QPushButton')
        self.setGeometry(450, 250, 400, 350)
        self.setWindowIcon(QIcon(r"C:\WORK\2023_februar_ui\icon\test.png"))

        btn = QPushButton('Click me', self)
        btn.setGeometry(100, 100, 130, 130)
        btn.setStyleSheet('background-color: yellow')
        btn.setIcon(QIcon(r"C:\WORK\2023_februar_ui\icon\test.png"))
        btn.setIconSize(QSize(110, 110))




if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
import sys

from PySide6.QtWidgets import QApplication, QWidget, QLineEdit
from PySide6.QtGui import QIcon



class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('UI Tutorial')
        self.setGeometry(450, 250, 400, 350)
        self.setWindowIcon(QIcon(r"C:\WORK\2023_februar_ui\icon\test.png"))

        #QLineEdit - one line editor

        line = QLineEdit(self)
        # line.setGeometry(50, 50, 300, 100)
        line.setPlaceholderText('Please enter your password')
        line.setEchoMode(QLineEdit.Password)

       






if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
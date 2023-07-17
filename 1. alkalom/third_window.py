import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon

# QMainWindow valójában egy felokosított - előre létrehozott - widget
# ő a fő ablakom
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('UI Tutorial')
        self.setGeometry(450, 250, 400, 350) # az ablak méretének a megváltoztatása
        self.setWindowIcon(QIcon(r"C:\WORK\2023_februar_ui\icon\test.png"))
        self.setStyleSheet("border: 40px solid black")



if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
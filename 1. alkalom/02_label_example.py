import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel
from PySide6.QtGui import QIcon, QPixmap, QMovie
from PySide6.QtCore import QSize


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('UI Tutorial')
        self.setGeometry(450, 250, 400, 350)
        self.setWindowIcon(QIcon(r"C:\WORK\2023_februar_ui\icon\test.png"))

        label = QLabel('This is a label', self)
        # label.move(100, 100)
        label.setGeometry(100, 100, 100, 100)
        label.setStyleSheet("border: 4px solid black")

        label2 = QLabel(self)
        image = QPixmap(r"C:\WORK\2023_februar_ui\icon\test.png")

        label2.setPixmap(image)
        label2.setGeometry(300, 300, 500, 500)
        label2.setStyleSheet("border: 3px solid purple")

        label3 = QLabel(self)
        gif = QMovie(r"C:\WORK\2023_februar_ui\icon\alien.gif")
        gif.setSpeed(1000)
        label3.setMovie(gif)
        gif.start()






if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
import sys

from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout
from PySide6.QtGui import QIcon



class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('UI Tutorial')
        self.setGeometry(450, 250, 400, 350)
        self.setWindowIcon(QIcon(r"C:\WORK\2023_februar_ui\icon\test.png"))
        # horizontalis elrendezés
        hbox = QHBoxLayout()

        # vertikális elrendezés
        vbox = QVBoxLayout()

        # rácsos elrendezés
        grid = QGridLayout()

        btn = QPushButton('Click one')
        btn2 = QPushButton('Click 2')
        btn3 = QPushButton('Click 3')
        btn4 = QPushButton('Click 4')

        hbox.addWidget(btn)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)
        hbox.addWidget(btn4)

        vbox.addWidget(btn)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addWidget(btn4)

        grid.addWidget(btn, 0, 0)
        grid.addWidget(btn2, 0, 1)
        grid.addWidget(btn3, 3, 3)
        grid.addWidget(btn4, 1, 1)

        self.setLayout(grid)
       






if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
import sys

from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLCDNumber
from PySide6.QtCore import QTime, QTimer


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 400, 300)

        timer = QTimer()
        timer.timeout.connect(self.show_lcd)

        timer.start(1000)

        self.show_lcd()

    def show_lcd(self):
        vbox = QVBoxLayout()
        lcd = QLCDNumber()

        lcd.setStyleSheet("background: yellow")
        vbox.addWidget(lcd)

        time = QTime.currentTime()
        text = time.toString("hh:mm")
        lcd.display(text)

        self.setLayout(vbox)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
import sys

from PySide6.QtWidgets import QApplication, QWidget, QPushButton
from PySide6.QtCore import QObject, Signal


class CustomWidget(QObject):
    custom_signal = Signal(str)

    def __init__(self):
        super().__init__()

    def output_writer(self):
        self.custom_signal.emit("Custom signal emitted")


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Interactive")
        self.setGeometry(100, 100, 400, 300)

        self.custom_widget = CustomWidget()
        btn = QPushButton("Click me", self)

        btn.clicked.connect(self.custom_widget.output_writer)
        self.custom_widget.custom_signal.connect(self.handle_custom_signal)

    def handle_custom_signal(self, message):
        print("|")

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
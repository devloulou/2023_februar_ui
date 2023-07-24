import sys

from PySide6.QtWidgets import QApplication, QWidget
from slider_ui import Ui_Form

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.horizontalSlider.valueChanged.connect(self.slider_change)
        self.ui.horizontalScrollBar.valueChanged.connect(self.scroll_change)

    def slider_change(self, value):
        # value = self.ui.horizontalSlider.value()
        self.ui.lineEdit.setText(f"Sugar level: {str(value)}")

    def scroll_change(self):
        value = self.ui.horizontalScrollBar.value()
        self.ui.lineEdit.setText(f"Blood pressure: {str(value)}")

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
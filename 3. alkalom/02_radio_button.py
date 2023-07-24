import sys

from PySide6.QtWidgets import QApplication, QWidget
from radio_button_ui import Ui_Form

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.radioButtonBusiness.toggled.connect(self.checked_status)
        self.ui.radioButtonEconomy.toggled.connect(self.checked_status)
        self.ui.radioButtonFirst.toggled.connect(self.checked_status)

    def checked_status(self):
        value = 0

        if self.ui.radioButtonBusiness.isChecked():
            value = 125
        if self.ui.radioButtonEconomy.isChecked():
            value = 110
        if self.ui.radioButtonFirst.isChecked():
            value = 150

        self.ui.label_5.setText(f"Value is: {value}")

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
import sys

from PySide6.QtWidgets import QApplication, QWidget
from checkbox_ui import Ui_Form

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.cheeseCheckbox.stateChanged.connect(self.show_amount)
        self.ui.baconCheckbox.stateChanged.connect(self.show_amount)
        self.ui.colaCheckbox.stateChanged.connect(self.show_amount)

    def show_amount(self):
        amount = 10

        if self.ui.cheeseCheckbox.isChecked():
            amount += 1
        
        if self.ui.baconCheckbox.isChecked():
            amount += 2
        
        if self.ui.colaCheckbox.isChecked():
            amount += 1

        self.ui.totalLabel.setText(f"Total: $ {amount}")

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
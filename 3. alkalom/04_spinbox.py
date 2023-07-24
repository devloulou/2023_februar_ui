import sys

from PySide6.QtWidgets import QApplication, QWidget
from spin_ui import Ui_Form

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # self.ui.spinBox.editingFinished.connect(self.show_price)
        self.ui.spinBox.valueChanged.connect(self.show_price)

    def show_price(self):
        laptop_price = int(self.ui.lineEdit.text())
        total_price = laptop_price * int(self.ui.spinBox.value())

        self.ui.lineEdit_2.setText(f"Total Price: {total_price}")

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
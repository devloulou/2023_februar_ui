import sys 

from PySide6.QtWidgets import QApplication, QWidget, QComboBox, QVBoxLayout, QLineEdit, QFormLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Interactive")
        self.setGeometry(100, 100, 400, 300)

        vbox = QVBoxLayout()

        self.combo = QComboBox()
        self.combo.addItem("Option 1")
        self.combo.addItem("Option 2")
        self.combo.addItem("Option 3")

        self.combo.currentIndexChanged.connect(self.update_form)

        vbox.addWidget(self.combo)

        self.form_layout = QFormLayout()
        vbox.addLayout(self.form_layout)

        # self.update_form(self.combo.currentIndex())

        self.setLayout(vbox)        



    def update_form(self, selected_idx):
        while self.form_layout.count() > 0:
            item = self.form_layout.takeAt(0)

            widget = item.widget()

            if widget is not None:
                widget.deleteLater()

        if selected_idx == 0:
            self.form_layout.addRow("Field 1", QLineEdit())

        elif selected_idx == 1:
            self.form_layout.addRow("Field 1", QLineEdit())
            self.form_layout.addRow("Field 2", QLineEdit())

        elif selected_idx == 2:
            self.form_layout.addRow("Field 1", QLineEdit())
            self.form_layout.addRow("Field 2", QLineEdit())
            self.form_layout.addRow("Field 3", QLineEdit())



if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
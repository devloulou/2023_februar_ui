from PySide6.QtWidgets import (QApplication, QVBoxLayout,
                               QHBoxLayout, QMainWindow,
                               QWidget, QHeaderView,
                               QMessageBox, QDialog,
                               QLabel, QLineEdit, QDialogButtonBox)
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import QModelIndex

class EditDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout()
        self.setWindowTitle("Modify Item")

        self.line_edit = []
        self.new_values = None
        self.setLayout(self.layout)

    def setup_fields(self, headers, item):
        for header, value in zip(headers, item):
            layout = QHBoxLayout()
            layout.addWidget(QLabel(header))
            line_edit = QLineEdit(str(value))
            layout.addWidget(line_edit)
            self.line_edit.append(line_edit)
            self.layout.addLayout(layout)

        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        self.layout.addWidget(button_box)

    def get_new_values(self):
        # for item in self.line_edit:
        #     data = int(item.text()) if item.text().isdigit() else item.text()

        self.new_values = [int(item.text()) if item.text().isdigit() else item.text() for item in self.line_edit]

        return self.new_values
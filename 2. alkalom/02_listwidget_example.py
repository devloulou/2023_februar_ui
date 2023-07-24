import sys

from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QInputDialog, QMessageBox
from listwidget_ui import Ui_Form

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.addButton.clicked.connect(self.add_item) # slot 
        self.ui.editButton.clicked.connect(self.edit_item)
        self.ui.removeButton.clicked.connect(self.remove_item)
        self.ui.sortButton.clicked.connect(self.sort_item)

    def add_item(self):
        row = self.ui.listWidget.currentRow()
        title = "Add item"
        data, ok = QInputDialog.getText(self, title, title)

        if ok and data is not None:
            self.ui.listWidget.insertItem(row, data)

    def edit_item(self):
        row = self.ui.listWidget.currentRow()
        item = self.ui.listWidget.item(row)

        if item is not None:
            title = "Edit Item"
            data, ok = QInputDialog.getText(self, title, title, QLineEdit.EchoMode.Normal, item.text())

            if ok and data is not None:
                item.setText(data)

    def remove_item(self):
        row = self.ui.listWidget.currentRow()
        item = self.ui.listWidget.item(row)

        if item is None:
            return
        
        reply = QMessageBox.question(self, "Remove Item", "Biztos törölni akarod?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if reply == QMessageBox.StandardButton.Yes:
            self.ui.listWidget.takeItem(row)

    def sort_item(self):
        self.ui.listWidget.sortItems()

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
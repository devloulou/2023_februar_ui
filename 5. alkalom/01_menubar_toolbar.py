import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QHeaderView, QMessageBox
from PySide6.QtGui import QStandardItemModel, QStandardItem

from menubar_toolbar_ui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.model = QStandardItemModel(0, 2, self)
        self.model.setHorizontalHeaderItem(0, QStandardItem("Name"))
        self.model.setHorizontalHeaderItem(1, QStandardItem("Phone"))

        self.ui.tableView.setModel(self.model)

        first_item = QStandardItem("Karcsi")
        second_item = QStandardItem("125412515")

        # self.model.setItem(0, 0, first_item)6
        # self.model.setItem(0, 1, second_item)

        self.model.appendRow([first_item, second_item])

        self.ui.actionQuit.triggered.connect(self.close_window)
        self.ui.pushButtonSave.clicked.connect(self.add_item)
        self.ui.actionAbout.triggered.connect(self.about_page)
        self.ui.pushButtonClear.clicked.connect(self.clear_all_items)
        self.ui.pushButtonClearOne.clicked.connect(self.clear_one_item)

    def close_window(self):
        self.close()

    def add_item(self):
        name = QStandardItem(self.ui.lineEditName.text())
        phone = QStandardItem(self.ui.lineEditPhone.text())

        if not name.text() or not phone.text():
            return

        self.model.appendRow([name, phone])

        self.ui.lineEditName.clear()
        self.ui.lineEditPhone.clear()

    def about_page(self):
        QMessageBox.information(self, "About Page", "This was created with PySide6")

    def clear_all_items(self):
        msg = QMessageBox()
        msg.setText("Delete All Items")

        msg.setInformativeText("Do you want to delete all data?")
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        ret = msg.exec()

        if ret == QMessageBox.StandardButton.No:
            return 
        
        self.model.clear()
        self.model.setHorizontalHeaderItem(0, QStandardItem("Name"))
        self.model.setHorizontalHeaderItem(1, QStandardItem("Phone"))

    def clear_one_item(self):
        indicies = self.ui.tableView.selectionModel().selectedRows()

        for index in sorted(indicies):
            self.model.removeRow(index.row())

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
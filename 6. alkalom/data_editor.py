import sys
import json

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHeaderView, QMessageBox
from PySide6.QtGui import QStandardItemModel, QStandardItem

# from modules.window_module.data_editor_ui import Ui_Form
# from modules.window_module import Ui_Form
from modules import Ui_Form
from modules.window_module import MyTableModel
from modules.database_module import insert_users, DBHandler, delete_users

URL = "postgresql://postgres:postgres@localhost:5432/postgres"

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.sql = DBHandler(URL)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.model = MyTableModel([])

        self.ui.tableView.setModel(self.model)

        self.ui.pushButtonAdd.clicked.connect(self.insert_data)
        self.ui.pushButtonClearAll.clicked.connect(self.clear_all)

    def clear_all(self):
        self.sql.run_query(delete_users)
        self.model.clear()

    def insert_data(self):
        first_name = self.ui.lineEditFirstName.text()
        last_name = self.ui.lineEditLastName.text()
        age = self.ui.lineEditAge.text()

        if not first_name or not last_name or not age:
            return
        
        self.sql.run_query(insert_users, [{'firstname': first_name,
                                           'lastname':last_name, 'age':age}])

        self.add_data_to_model(firstname=first_name, lastname=last_name, age=age)

    def add_data_to_model(self, **data):
        # itt kellene hozzáadni az adatot a model-hez
        self.model.appendRow(list(data.values()))
        

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
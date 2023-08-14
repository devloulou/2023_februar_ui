import sys
import json

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHeaderView, QMessageBox, QDialog
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import QModelIndex

# from modules.window_module.data_editor_ui import Ui_Form
# from modules.window_module import Ui_Form
from modules import Ui_Form
from modules.window_module import MyTableModel, EditDialog
from modules.database_module import (insert_users,
                                     DBHandler,
                                     delete_users,
                                     select_users,
                                     truncate_users,
                                     update_users)

URL = "postgresql://postgres:postgres@localhost:5432/postgres"

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.sql = DBHandler(URL)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.model = self.get_all_data()

        self.ui.tableView.setModel(self.model)

        self.ui.pushButtonAdd.clicked.connect(self.insert_data)
        self.ui.pushButtonClearAll.clicked.connect(self.clear_all)
        self.ui.pushButtonClearItem.clicked.connect(self.clear_item)
        self.ui.pushButtonModify.clicked.connect(self.modify_item)

    def modify_item(self):
        selected_row = self.ui.tableView.selectedIndexes()
        

        row_index = selected_row[0].row()
        item = self.model._data[row_index]
        print(f'item: {item}')
        new_values, ok = self.show_input_dialog(item)

        if not ok:
            return
        
        # itt kellene az update-et megfuttatni, illetve módosítani a tableView értékeit
        self.sql.run_query(update_users.format(new_firstname=new_values[0], new_lastname=new_values[1],
                          new_age=new_values[2], old_firstname=item[0], old_lastname=item[1], old_age=item[2]))
    
        self.model.setData(self.model.index(row_index,0), new_values[0])
        self.model.setData(self.model.index(row_index,1), new_values[1])
        self.model.setData(self.model.index(row_index,2), new_values[2])

    def show_input_dialog(self, item):
        dialog = EditDialog(self)
        dialog.setup_fields(self.model.headers, item)
        
        if dialog.exec() == QDialog.DialogCode.Accepted:
            # itt kellene a módosítást elvégezni
            return dialog.get_new_values(), True
        else:
            # ha cancel, akkor ne csináljon semmit
            return item, False

        

    def get_all_data(self):
        result = self.sql.run_select_query(select_users)
       
        data = [list(item) for item in result]
        return MyTableModel(data)
        

    def clear_item(self):
        index = self.ui.tableView.selectionModel().selectedRows()        

        for e_x, idx in enumerate(sorted(index)):
            if e_x == 0:
                data = self.model._data[idx.row()]
                self.model.removeRow(idx.row())
            else:
                data = self.model._data[idx.row() - e_x]
                self.model.removeRow(idx.row() - e_x)
            self.sql.run_query(delete_users.format(firstname=data[0], lastname=data[1], age=data[2]))
            print(self.model._data)
            

    def clear_all(self):
        self.sql.run_query(truncate_users)
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
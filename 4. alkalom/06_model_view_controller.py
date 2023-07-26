"""
Model View Controller - MVC 

Model - database layer
View - reprezentációs layer - UI
Controller - "üzleti logika" , ő kommunikál a model és a view-val
"""
from typing import Union
from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex
from PySide6.QtWidgets import QApplication, QTableView


class MyTableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def rowCount(self, parent: QModelIndex):
        return len(self._data)
    
    def columnCount(self, parent: QModelIndex):
        if self._data:
            return len(self._data[0])
        
        return 0
        
    def data(self, index, role = Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            row = index.row()
            col = index.column()
            return str(self._data[row][col])
        
        return None
    
if __name__ == '__main__':
    app = QApplication([])

    data = [
        ['Ricsi', 'Kovacs', "33" ],
        ['Lewis', 'Hamilton', "38" ],
        ['Maris', 'Ka', "33" ],
    ]

    model = MyTableModel(data)
    table_view = QTableView()
    table_view.setModel(model)
    table_view.show()

    app.exec()
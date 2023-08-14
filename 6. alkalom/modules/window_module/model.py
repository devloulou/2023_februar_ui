from typing import Any
from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex

class MyTableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data:list = data 
        self.headers = ['First Name', 'Last Name', 'Age']

    def rowCount(self, parent: QModelIndex):
        return len(self._data)
    
    def columnCount(self, parent: QModelIndex):
        return len(self.headers)
        
    def data(self, index, role = Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            row = index.row()
            col = index.column()
            return str(self._data[row][col])
        
        return None
    
    def headerData(self, section, orientation, role):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return self.headers[section]
            elif orientation == Qt.Orientation.Vertical:
                return str(section + 1)
        return None
    
    def appendRow(self, data):
        row_index = len(data)
        self.beginInsertRows(QModelIndex(), row_index, row_index)
        self._data.append(data)
        self.endInsertRows()

    def clear(self):
        self.beginRemoveRows(QModelIndex(), 0, len(self._data) - 1)
        # self._data.clear()
        self._data = []
        self.endRemoveRows()

    def removeRow(self, idx: int):
        self.beginRemoveRows(QModelIndex(), idx, idx)        
        self._data.pop(idx)
        self.endRemoveRows()

    def setData(self, index, value, role=Qt.ItemDataRole.EditRole):
        if role == Qt.ItemDataRole.EditRole:
            self._data[index.row()][index.column()] = value
            self.dataChanged.emit(index, index)

            return True
        
        return False
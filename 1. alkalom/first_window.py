import sys

from PySide6.QtWidgets import QApplication, QMainWindow

# app = QApplication(sys.argv)
app = QApplication([])

window = QMainWindow()

window.statusBar().showMessage("Welcome to UI")
window.menuBar().addMenu('File')

window.show()


app.exec()
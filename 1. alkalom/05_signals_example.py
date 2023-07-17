import sys

from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PySide6.QtGui import QIcon



class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('UI Tutorial')
        self.setGeometry(450, 250, 400, 350)
        self.setWindowIcon(QIcon(r"C:\WORK\2023_februar_ui\icon\test.png"))
        # vertikális elrendezés
        vbox = QVBoxLayout()

        # signal kezelés -> figyelni kell azokat a jeleket, amelyekkel a műveletet akarom végezni
        btn = QPushButton('Change text')
        self.label = QLabel('Hello szia')

        vbox.addWidget(btn)
        vbox.addWidget(self.label)

        self.setLayout(vbox)
       
        btn.clicked.connect(self.change_text)


    def change_text(self):
        import random
        colors = {
            1: 'purple',
            2: "green",
            3: 'red'
        }
        self.label.setText(f"I changed this: {random.randint(10, 20)}")
        self.label.setStyleSheet(f"color: {colors[random.randint(1, 3)]}")





if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
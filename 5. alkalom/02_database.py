import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QWidget, QLineEdit
from PySide6.QtGui import QFont

import sqlite3


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SqLite")
        self.setGeometry(100, 100, 400, 300)

        vbox = QVBoxLayout()
        vbox2 = QVBoxLayout()

        self.label = QLabel()
        self.label.setFont(QFont("Times", 15))

        btn = QPushButton("Create Table")
        btn_insert = QPushButton("Insert Record")

        labelFirstName = QLabel("First Name")
        labelLastName = QLabel("Last Name")
        labelAge = QLabel("Age")

        self.lineEditFirstname = QLineEdit()
        self.lineEditLastName = QLineEdit()
        self.lineEditAge = QLineEdit()

        hbox = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()
        
        hbox.addWidget(labelFirstName)
        hbox.addWidget(self.lineEditFirstname )

        hbox2.addWidget(labelLastName)
        hbox2.addWidget(self.lineEditLastName)

        hbox3.addWidget(labelAge)
        hbox3.addWidget(self.lineEditAge)

        vbox.addLayout(hbox)        
        vbox.addLayout(hbox2)        
        vbox.addLayout(hbox3)        
        vbox.addWidget(btn_insert)   

        self.labelResult = QLabel()

        vbox2.addLayout(vbox)

        vbox2.addWidget(self.labelResult)

        btn_insert.clicked.connect(self.insert_data)

        self.setLayout(vbox2)

    def insert_data(self):
        first_name = self.lineEditFirstname.text()
        last_name = self.lineEditLastName.text()
        age = self.lineEditAge.text()

        query = f"insert into users (firstname, lastname, age) \
            values ('{first_name}', '{last_name}', {age})"
        
        try:
            with sqlite3.connect("employee.db") as conn:
                conn.execute(query)
                conn.commit()

                self.labelResult.setText("Insert finished.")

        except Exception as e:
            conn.rollback()
            self.labelResult.setText(f"error occured: {str(e)}")

    def create_table(self):
        try:
            with sqlite3.connect("employee.db") as conn:
                conn.execute("""
                create table users (
                    id integer primary key, 
                    firstname varchar(40),
                    lastname varchar(40),
                    age integer
                    )
                """)
                conn.commit()
                self.label.setText("Table Created")

        except Exception as e:
            conn.rollback()
            self.label.setText(f"Error occured: {str(e)}")

app = QApplication([])
window = MainWindow()
window.show()
sys.exit(app.exec())
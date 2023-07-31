# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'data_editor_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableView,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(632, 568)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelFirstName = QLabel(Form)
        self.labelFirstName.setObjectName(u"labelFirstName")
        font = QFont()
        font.setPointSize(14)
        self.labelFirstName.setFont(font)

        self.horizontalLayout.addWidget(self.labelFirstName)

        self.lineEditFirstName = QLineEdit(Form)
        self.lineEditFirstName.setObjectName(u"lineEditFirstName")
        self.lineEditFirstName.setFont(font)

        self.horizontalLayout.addWidget(self.lineEditFirstName)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelLastName = QLabel(Form)
        self.labelLastName.setObjectName(u"labelLastName")
        self.labelLastName.setFont(font)

        self.horizontalLayout_2.addWidget(self.labelLastName)

        self.lineEditLastName = QLineEdit(Form)
        self.lineEditLastName.setObjectName(u"lineEditLastName")
        self.lineEditLastName.setFont(font)

        self.horizontalLayout_2.addWidget(self.lineEditLastName)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.labelAge = QLabel(Form)
        self.labelAge.setObjectName(u"labelAge")
        self.labelAge.setFont(font)

        self.horizontalLayout_3.addWidget(self.labelAge)

        self.lineEditAge = QLineEdit(Form)
        self.lineEditAge.setObjectName(u"lineEditAge")
        self.lineEditAge.setFont(font)

        self.horizontalLayout_3.addWidget(self.lineEditAge)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.tableView = QTableView(Form)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButtonAdd = QPushButton(Form)
        self.pushButtonAdd.setObjectName(u"pushButtonAdd")
        self.pushButtonAdd.setFont(font)

        self.horizontalLayout_4.addWidget(self.pushButtonAdd)

        self.pushButtonModify = QPushButton(Form)
        self.pushButtonModify.setObjectName(u"pushButtonModify")
        self.pushButtonModify.setFont(font)

        self.horizontalLayout_4.addWidget(self.pushButtonModify)

        self.pushButtonClearItem = QPushButton(Form)
        self.pushButtonClearItem.setObjectName(u"pushButtonClearItem")
        self.pushButtonClearItem.setFont(font)

        self.horizontalLayout_4.addWidget(self.pushButtonClearItem)

        self.pushButtonClearAll = QPushButton(Form)
        self.pushButtonClearAll.setObjectName(u"pushButtonClearAll")
        self.pushButtonClearAll.setFont(font)

        self.horizontalLayout_4.addWidget(self.pushButtonClearAll)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.labelFirstName.setText(QCoreApplication.translate("Form", u"First Name", None))
        self.labelLastName.setText(QCoreApplication.translate("Form", u"Last Name", None))
        self.labelAge.setText(QCoreApplication.translate("Form", u"Age", None))
        self.pushButtonAdd.setText(QCoreApplication.translate("Form", u"Add Item", None))
        self.pushButtonModify.setText(QCoreApplication.translate("Form", u"Modify Item", None))
        self.pushButtonClearItem.setText(QCoreApplication.translate("Form", u"Clear Item", None))
        self.pushButtonClearAll.setText(QCoreApplication.translate("Form", u"Clear All", None))
    # retranslateUi


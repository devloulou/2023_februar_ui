# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'list_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(808, 804)
        self.horizontalLayout_2 = QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.listWidget = QListWidget(Form)
        self.listWidget.setObjectName(u"listWidget")

        self.horizontalLayout.addWidget(self.listWidget)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.addButton = QPushButton(Form)
        self.addButton.setObjectName(u"addButton")

        self.verticalLayout.addWidget(self.addButton)

        self.editButton = QPushButton(Form)
        self.editButton.setObjectName(u"editButton")

        self.verticalLayout.addWidget(self.editButton)

        self.removeButton = QPushButton(Form)
        self.removeButton.setObjectName(u"removeButton")

        self.verticalLayout.addWidget(self.removeButton)

        self.verticalSpacer = QSpacerItem(20, 218, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.sortButton = QPushButton(Form)
        self.sortButton.setObjectName(u"sortButton")

        self.verticalLayout.addWidget(self.sortButton)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.addButton.setText(QCoreApplication.translate("Form", u"ADD", None))
        self.editButton.setText(QCoreApplication.translate("Form", u"EDIT", None))
        self.removeButton.setText(QCoreApplication.translate("Form", u"Remove", None))
        self.sortButton.setText(QCoreApplication.translate("Form", u"Sort", None))
    # retranslateUi


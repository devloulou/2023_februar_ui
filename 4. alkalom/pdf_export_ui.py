# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerpFYbbJ.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(676, 448)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.printButton = QPushButton(Form)
        self.printButton.setObjectName(u"printButton")
        font = QFont()
        font.setPointSize(14)
        self.printButton.setFont(font)

        self.horizontalLayout.addWidget(self.printButton)

        self.previewButton = QPushButton(Form)
        self.previewButton.setObjectName(u"previewButton")
        self.previewButton.setFont(font)

        self.horizontalLayout.addWidget(self.previewButton)

        self.exportButton = QPushButton(Form)
        self.exportButton.setObjectName(u"exportButton")
        self.exportButton.setFont(font)

        self.horizontalLayout.addWidget(self.exportButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.printButton.setText(QCoreApplication.translate("Form", u"Print", None))
        self.previewButton.setText(QCoreApplication.translate("Form", u"Print Preview", None))
        self.exportButton.setText(QCoreApplication.translate("Form", u"Export PDF", None))
    # retranslateUi


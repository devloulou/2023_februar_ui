# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'radion_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QRadioButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(559, 439)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radioButtonFirst = QRadioButton(Form)
        self.radioButtonFirst.setObjectName(u"radioButtonFirst")
        self.radioButtonFirst.setFont(font)

        self.horizontalLayout.addWidget(self.radioButtonFirst)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout.addWidget(self.label_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.radioButtonBusiness = QRadioButton(Form)
        self.radioButtonBusiness.setObjectName(u"radioButtonBusiness")
        self.radioButtonBusiness.setFont(font)

        self.horizontalLayout_2.addWidget(self.radioButtonBusiness)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.radioButtonEconomy = QRadioButton(Form)
        self.radioButtonEconomy.setObjectName(u"radioButtonEconomy")
        self.radioButtonEconomy.setFont(font)

        self.horizontalLayout_3.addWidget(self.radioButtonEconomy)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_4)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.verticalLayout.addWidget(self.label_5)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Choose fligth type", None))
        self.radioButtonFirst.setText(QCoreApplication.translate("Form", u"First Class", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"$ 150", None))
        self.radioButtonBusiness.setText(QCoreApplication.translate("Form", u"Business Class", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"$ 125", None))
        self.radioButtonEconomy.setText(QCoreApplication.translate("Form", u"Economy CLass", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"$ 110", None))
        self.label_5.setText("")
    # retranslateUi


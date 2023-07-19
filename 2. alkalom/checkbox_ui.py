# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designernaogEQ.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(356, 256)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 40, 274, 174))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pizzaLabel = QLabel(self.widget)
        self.pizzaLabel.setObjectName(u"pizzaLabel")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.pizzaLabel.setFont(font)

        self.horizontalLayout.addWidget(self.pizzaLabel)

        self.priceLabel = QLabel(self.widget)
        self.priceLabel.setObjectName(u"priceLabel")
        self.priceLabel.setFont(font)

        self.horizontalLayout.addWidget(self.priceLabel)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.selectionLabel = QLabel(self.widget)
        self.selectionLabel.setObjectName(u"selectionLabel")
        self.selectionLabel.setFont(font)

        self.horizontalLayout_2.addWidget(self.selectionLabel)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.cheeseCheckbox = QCheckBox(self.widget)
        self.cheeseCheckbox.setObjectName(u"cheeseCheckbox")
        self.cheeseCheckbox.setFont(font)

        self.verticalLayout.addWidget(self.cheeseCheckbox)

        self.baconCheckbox = QCheckBox(self.widget)
        self.baconCheckbox.setObjectName(u"baconCheckbox")
        self.baconCheckbox.setFont(font)

        self.verticalLayout.addWidget(self.baconCheckbox)

        self.colaCheckbox = QCheckBox(self.widget)
        self.colaCheckbox.setObjectName(u"colaCheckbox")
        self.colaCheckbox.setFont(font)

        self.verticalLayout.addWidget(self.colaCheckbox)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.totalLabel = QLabel(self.widget)
        self.totalLabel.setObjectName(u"totalLabel")
        self.totalLabel.setFont(font)

        self.verticalLayout_2.addWidget(self.totalLabel)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pizzaLabel.setText(QCoreApplication.translate("Form", u"Pizza price", None))
        self.priceLabel.setText(QCoreApplication.translate("Form", u"$ 10", None))
        self.selectionLabel.setText(QCoreApplication.translate("Form", u"Select extra", None))
        self.cheeseCheckbox.setText(QCoreApplication.translate("Form", u"Extra cheese 1$", None))
        self.baconCheckbox.setText(QCoreApplication.translate("Form", u"Extra Bacon 2$", None))
        self.colaCheckbox.setText(QCoreApplication.translate("Form", u"Extra Cola 1$", None))
        self.totalLabel.setText(QCoreApplication.translate("Form", u"Total: $ ", None))
    # retranslateUi


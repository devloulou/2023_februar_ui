# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'table_view_menu.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QTableView, QToolBar,
    QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(639, 544)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        icon = QIcon()
        icon.addFile(u":/icons/new.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNew.setIcon(icon)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        icon1 = QIcon()
        icon1.addFile(u":/icons/open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpen.setIcon(icon1)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        icon2 = QIcon()
        icon2.addFile(u":/icons/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave.setIcon(icon2)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        icon3 = QIcon()
        icon3.addFile(u":/icons/exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionQuit.setIcon(icon3)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        icon4 = QIcon()
        icon4.addFile(u":/icons/about.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAbout.setIcon(icon4)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelName = QLabel(self.centralwidget)
        self.labelName.setObjectName(u"labelName")

        self.horizontalLayout.addWidget(self.labelName)

        self.lineEditName = QLineEdit(self.centralwidget)
        self.lineEditName.setObjectName(u"lineEditName")

        self.horizontalLayout.addWidget(self.lineEditName)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelPhone = QLabel(self.centralwidget)
        self.labelPhone.setObjectName(u"labelPhone")

        self.horizontalLayout_2.addWidget(self.labelPhone)

        self.lineEditPhone = QLineEdit(self.centralwidget)
        self.lineEditPhone.setObjectName(u"lineEditPhone")

        self.horizontalLayout_2.addWidget(self.lineEditPhone)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButtonSave = QPushButton(self.centralwidget)
        self.pushButtonSave.setObjectName(u"pushButtonSave")

        self.horizontalLayout_3.addWidget(self.pushButtonSave)

        self.pushButtonClear = QPushButton(self.centralwidget)
        self.pushButtonClear.setObjectName(u"pushButtonClear")

        self.horizontalLayout_3.addWidget(self.pushButtonClear)

        self.pushButtonClearOne = QPushButton(self.centralwidget)
        self.pushButtonClearOne.setObjectName(u"pushButtonClearOne")

        self.horizontalLayout_3.addWidget(self.pushButtonClearOne)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 639, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionQuit)
        self.toolBar.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
#if QT_CONFIG(shortcut)
        self.actionNew.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.labelName.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.labelPhone.setText(QCoreApplication.translate("MainWindow", u"Phone:", None))
        self.pushButtonSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pushButtonClear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.pushButtonClearOne.setText(QCoreApplication.translate("MainWindow", u"Clear One", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi


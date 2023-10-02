# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'asset_management.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_asset_management(object):
    def setupUi(self, asset_management):
        if not asset_management.objectName():
            asset_management.setObjectName(u"asset_management")
        asset_management.resize(800, 600)
        self.centralwidget = QWidget(asset_management)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.verticalLayout_2.addLayout(self.verticalLayout)

        asset_management.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(asset_management)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        asset_management.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(asset_management)
        self.statusbar.setObjectName(u"statusbar")
        asset_management.setStatusBar(self.statusbar)

        self.retranslateUi(asset_management)

        QMetaObject.connectSlotsByName(asset_management)
    # setupUi

    def retranslateUi(self, asset_management):
        asset_management.setWindowTitle(QCoreApplication.translate("asset_management", u"Asset Management", None))
    # retranslateUi


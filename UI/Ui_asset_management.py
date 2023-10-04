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
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.video_tab = QWidget()
        self.video_tab.setObjectName(u"video_tab")
        self.verticalLayout_4 = QVBoxLayout(self.video_tab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.listView_2 = QListView(self.video_tab)
        self.listView_2.setObjectName(u"listView_2")

        self.verticalLayout_4.addWidget(self.listView_2)

        self.tabWidget.addTab(self.video_tab, "")
        self.text_tab = QWidget()
        self.text_tab.setObjectName(u"text_tab")
        self.tabWidget.addTab(self.text_tab, "")
        self.image_tab = QWidget()
        self.image_tab.setObjectName(u"image_tab")
        self.tabWidget.addTab(self.image_tab, "")
        self.model_tab = QWidget()
        self.model_tab.setObjectName(u"model_tab")
        self.tabWidget.addTab(self.model_tab, "")
        self.production_tab = QWidget()
        self.production_tab.setObjectName(u"production_tab")
        self.verticalLayout_3 = QVBoxLayout(self.production_tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tabWidget.addTab(self.production_tab, "")

        self.verticalLayout.addWidget(self.tabWidget)


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

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(asset_management)
    # setupUi

    def retranslateUi(self, asset_management):
        asset_management.setWindowTitle(QCoreApplication.translate("asset_management", u"Asset Management", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.video_tab), QCoreApplication.translate("asset_management", u"Video", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.text_tab), QCoreApplication.translate("asset_management", u"Text", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.image_tab), QCoreApplication.translate("asset_management", u"Image", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.model_tab), QCoreApplication.translate("asset_management", u"Model", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.production_tab), QCoreApplication.translate("asset_management", u"Production", None))
    # retranslateUi


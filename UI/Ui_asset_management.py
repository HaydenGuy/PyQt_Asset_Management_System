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
        self.actionOpen = QAction(asset_management)
        self.actionOpen.setObjectName(u"actionOpen")
        self.centralwidget = QWidget(asset_management)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.h_lay_search_refresh = QHBoxLayout()
        self.h_lay_search_refresh.setObjectName(u"h_lay_search_refresh")
        self.h_lay_search_refresh.setContentsMargins(-1, 0, -1, -1)
        self.lb_search = QLabel(self.centralwidget)
        self.lb_search.setObjectName(u"lb_search")

        self.h_lay_search_refresh.addWidget(self.lb_search)

        self.le_searchbar = QLineEdit(self.centralwidget)
        self.le_searchbar.setObjectName(u"le_searchbar")

        self.h_lay_search_refresh.addWidget(self.le_searchbar)

        self.pb_refresh = QPushButton(self.centralwidget)
        self.pb_refresh.setObjectName(u"pb_refresh")

        self.h_lay_search_refresh.addWidget(self.pb_refresh)


        self.verticalLayout_2.addLayout(self.h_lay_search_refresh)

        self.v_lay_tabs = QVBoxLayout()
        self.v_lay_tabs.setObjectName(u"v_lay_tabs")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.video_tab = QWidget()
        self.video_tab.setObjectName(u"video_tab")
        self.verticalLayout_4 = QVBoxLayout(self.video_tab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.video_list = QListWidget(self.video_tab)
        self.video_list.setObjectName(u"video_list")

        self.verticalLayout_4.addWidget(self.video_list)

        self.tabWidget.addTab(self.video_tab, "")
        self.text_tab = QWidget()
        self.text_tab.setObjectName(u"text_tab")
        self.verticalLayout_5 = QVBoxLayout(self.text_tab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.text_list = QListWidget(self.text_tab)
        self.text_list.setObjectName(u"text_list")

        self.verticalLayout_5.addWidget(self.text_list)

        self.tabWidget.addTab(self.text_tab, "")
        self.image_tab = QWidget()
        self.image_tab.setObjectName(u"image_tab")
        self.verticalLayout_6 = QVBoxLayout(self.image_tab)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.image_list = QListWidget(self.image_tab)
        self.image_list.setObjectName(u"image_list")

        self.verticalLayout_6.addWidget(self.image_list)

        self.tabWidget.addTab(self.image_tab, "")
        self.model_tab = QWidget()
        self.model_tab.setObjectName(u"model_tab")
        self.verticalLayout_7 = QVBoxLayout(self.model_tab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.model_list = QListWidget(self.model_tab)
        self.model_list.setObjectName(u"model_list")

        self.verticalLayout_7.addWidget(self.model_list)

        self.tabWidget.addTab(self.model_tab, "")
        self.production_tab = QWidget()
        self.production_tab.setObjectName(u"production_tab")
        self.verticalLayout_3 = QVBoxLayout(self.production_tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.production_list = QListWidget(self.production_tab)
        self.production_list.setObjectName(u"production_list")

        self.verticalLayout_3.addWidget(self.production_list)

        self.tabWidget.addTab(self.production_tab, "")

        self.v_lay_tabs.addWidget(self.tabWidget)


        self.verticalLayout_2.addLayout(self.v_lay_tabs)

        asset_management.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(asset_management)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        asset_management.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(asset_management)
        self.statusbar.setObjectName(u"statusbar")
        asset_management.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionOpen)

        self.retranslateUi(asset_management)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(asset_management)
    # setupUi

    def retranslateUi(self, asset_management):
        asset_management.setWindowTitle(QCoreApplication.translate("asset_management", u"Asset Management", None))
        self.actionOpen.setText(QCoreApplication.translate("asset_management", u"Open", None))
        self.lb_search.setText(QCoreApplication.translate("asset_management", u"Search:", None))
        self.pb_refresh.setText(QCoreApplication.translate("asset_management", u"Refresh", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.video_tab), QCoreApplication.translate("asset_management", u"Video", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.text_tab), QCoreApplication.translate("asset_management", u"Text", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.image_tab), QCoreApplication.translate("asset_management", u"Image", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.model_tab), QCoreApplication.translate("asset_management", u"Model", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.production_tab), QCoreApplication.translate("asset_management", u"Production", None))
        self.menuFile.setTitle(QCoreApplication.translate("asset_management", u"File", None))
    # retranslateUi


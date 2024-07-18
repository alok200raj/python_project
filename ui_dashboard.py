# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboard_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,Slot,
    QSize, QTime, QUrl, Qt)
import sys
import pyodbc
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QSplitter, QStackedWidget,QMessageBox,QFileDialog,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)


import rc_resource
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
import pandas as pd


class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1119, 738)
        MainWindow.setStyleSheet(u"background-color: rgb(245, 250, 254);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.main_mnu = QWidget(self.centralwidget)
        self.main_mnu.setObjectName(u"main_mnu")
        self.verticalLayout_5 = QVBoxLayout(self.main_mnu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget = QWidget(self.main_mnu)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.menu_1 = QPushButton(self.widget)
        self.menu_1.setObjectName(u"menu_1")
        self.menu_1.setStyleSheet(u"border:none;")
        icon = QIcon()
        icon.addFile(u":/img/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_1.setIcon(icon)
        self.menu_1.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.menu_1)
        self.hello_label = QLabel(self.widget)
        self.hello_label.setObjectName(u"hello_label")
        self.hello_label.setStyleSheet(u"color:black;font-size:20px; font-weight:bold;")
        self.hello_label.setText(f"Hello, {self.user_name}")  # Set the text to include the user's name
        self.horizontalLayout_3.addWidget(self.hello_label)

        self.horizontalSpacer = QSpacerItem(252, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.splitter = QSplitter(self.widget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.lineEdit = QLineEdit(self.splitter)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"color:black;")
        self.splitter.addWidget(self.lineEdit)
        self.search_btn = QPushButton(self.splitter)
        self.search_btn.setObjectName(u"search_btn")
        self.search_btn.setMaximumSize(QSize(50, 16777215))
        icon1 = QIcon()
        icon1.addFile(u":/img/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.search_btn.setIcon(icon1)
        self.splitter.addWidget(self.search_btn)

        self.horizontalLayout_3.addWidget(self.splitter)

        self.horizontalSpacer_2 = QSpacerItem(252, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.profile_img = QPushButton(self.widget)
        self.profile_img.setObjectName(u"profile_img")
        self.profile_img.setStyleSheet(u"border:none;")
        icon2 = QIcon()
        icon2.addFile(u":/img/image.png", QSize(), QIcon.Normal, QIcon.Off)
        self.profile_img.setIcon(icon2)

        self.horizontalLayout_3.addWidget(self.profile_img)
   
        self.verticalLayout_5.addWidget(self.widget)

        self.stackedWidget_2 = QStackedWidget(self.main_mnu)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.Dashboard_page = QWidget()
        self.Dashboard_page.setObjectName(u"Dashboard_page")
        self.label_4 = QLabel(self.Dashboard_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(270, 120, 171, 51))
        font = QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.stackedWidget_2.addWidget(self.Dashboard_page)
        self.Employee_page = QWidget()
        self.Employee_page.setObjectName(u"Employee_page")
        self.widget1 = QWidget(self.Employee_page)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(0, 0, 881, 651))
        self.verticalLayout_6 = QVBoxLayout(self.widget1)
        self.verticalLayout_6.setSpacing(7)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_6.setContentsMargins(0, 0, 11, 0)
        self.frame = QFrame(self.widget1)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(85, 170, 255);\n"
"border-color: rgb(60, 229, 231);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.title_label = QLabel(self.frame)
        self.title_label.setObjectName(u"title_label")
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.title_label.setFont(font1)
        self.title_label.setFocusPolicy(Qt.NoFocus)
        self.title_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.title_label)


        self.verticalLayout_6.addWidget(self.frame)

        self.info_frame = QFrame(self.widget1)
        self.info_frame.setObjectName(u"info_frame")
        self.info_frame.setFrameShape(QFrame.StyledPanel)
        self.info_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.info_frame)
        self.gridLayout_3.setSpacing(20)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(30, 20, 30, 20)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(12)
        self.gridLayout_2.setVerticalSpacing(17)
        self.label_9 = QLabel(self.info_frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setEnabled(False)

        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)

        self.id = QLineEdit(self.info_frame)
        self.id.setObjectName(u"id")
        self.id.setEnabled(False)

        self.gridLayout_2.addWidget(self.id, 0, 1, 1, 1)

        self.label_5 = QLabel(self.info_frame)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)

        self.name = QLineEdit(self.info_frame)
        self.name.setObjectName(u"name")

        self.gridLayout_2.addWidget(self.name, 1, 1, 1, 1)

        self.label_10 = QLabel(self.info_frame)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 2, 0, 1, 1)

        self.label_11 = QLabel(self.info_frame)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 3, 0, 1, 1)

        self.gender = QComboBox(self.info_frame)
        self.gender.addItem("")
        self.gender.addItem("")
        self.gender.addItem("")
        self.gender.addItem("")
        self.gender.setObjectName(u"gender")

        self.gridLayout_2.addWidget(self.gender, 3, 1, 1, 1)

        self.doj = QDateEdit(self.info_frame)
        self.doj.setObjectName(u"doj")

        self.gridLayout_2.addWidget(self.doj, 2, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(12)
        self.gridLayout_4.setVerticalSpacing(15)
        self.label_12 = QLabel(self.info_frame)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_4.addWidget(self.label_12, 0, 0, 1, 1)

        self.label_13 = QLabel(self.info_frame)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_4.addWidget(self.label_13, 1, 0, 1, 1)

        self.designation = QLineEdit(self.info_frame)
        self.designation.setObjectName(u"designation")

        self.gridLayout_4.addWidget(self.designation, 1, 1, 1, 1)

        self.label_14 = QLabel(self.info_frame)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_4.addWidget(self.label_14, 2, 0, 1, 1)

        self.department = QComboBox(self.info_frame)
        self.department.addItem("")
        self.department.addItem("")
        self.department.addItem("")
        self.department.addItem("")
        self.department.addItem("")
        self.department.setObjectName(u"department")

        self.gridLayout_4.addWidget(self.department, 2, 1, 1, 1)

        self.mobile = QLineEdit(self.info_frame)
        self.mobile.setObjectName(u"mobile")

        self.gridLayout_4.addWidget(self.mobile, 0, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_4, 0, 1, 1, 1)


        self.verticalLayout_6.addWidget(self.info_frame)

        self.functio_frame = QFrame(self.widget1)
        self.functio_frame.setObjectName(u"functio_frame")
        self.functio_frame.setFrameShape(QFrame.StyledPanel)
        self.functio_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.functio_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(30, -1, 30, -1)
        self.add_btn = QPushButton(self.functio_frame)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setStyleSheet(u"background-color: rgb(0, 0, 255);")
        icon3 = QIcon()
        icon3.addFile(u"img/add-button-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.add_btn.setIcon(icon3)

        self.horizontalLayout_5.addWidget(self.add_btn)

        self.update_btn = QPushButton(self.functio_frame)
        self.update_btn.setObjectName(u"update_btn")
        self.update_btn.setStyleSheet(u"background-color: rgb(0, 255, 127);")
        icon4 = QIcon()
        icon4.addFile(u"img/update-business-user-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.update_btn.setIcon(icon4)

        self.horizontalLayout_5.addWidget(self.update_btn)

        self.search_btn_2 = QPushButton(self.functio_frame)
        self.search_btn_2.setObjectName(u"search_btn_2")
        self.search_btn_2.setStyleSheet(u"background-color: rgb(0, 85, 127);\n"
"background-color: rgb(0, 170, 255);")
        icon5 = QIcon()
        icon5.addFile(u"img/search-file-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.search_btn_2.setIcon(icon5)

        self.horizontalLayout_5.addWidget(self.search_btn_2)

        self.clear_btn = QPushButton(self.functio_frame)
        self.clear_btn.setObjectName(u"clear_btn")
        self.clear_btn.setStyleSheet(u"background-color: rgb(170, 0, 0);")
        icon6 = QIcon()
        icon6.addFile(u"img/clear-all-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.clear_btn.setIcon(icon6)

        self.horizontalLayout_5.addWidget(self.clear_btn)

        self.delete_btn = QPushButton(self.functio_frame)
        self.delete_btn.setObjectName(u"delete_btn")
        self.delete_btn.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        icon7 = QIcon()
        icon7.addFile(u"img/delete-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_btn.setIcon(icon7)

        self.horizontalLayout_5.addWidget(self.delete_btn)

        self.excel_btn = QPushButton(self.functio_frame)
        self.excel_btn.setObjectName(u"excel_btn")
        self.excel_btn.setStyleSheet(u"background-color: rgb(0, 255, 255);")

        self.horizontalLayout_5.addWidget(self.excel_btn)

        self.pdf_btn = QPushButton(self.functio_frame)
        self.pdf_btn.setObjectName(u"pdf_btn")
        self.pdf_btn.setStyleSheet(u"background-color: rgb(255, 144, 80);")
        icon8 = QIcon()
        icon8.addFile(u"img/select-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pdf_btn.setIcon(icon8)

        self.horizontalLayout_5.addWidget(self.pdf_btn)


        self.verticalLayout_6.addWidget(self.functio_frame)

        self.result_frame = QFrame(self.widget1)
        self.result_frame.setObjectName(u"result_frame")
        self.result_frame.setFrameShape(QFrame.StyledPanel)
        self.result_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.result_frame)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setVerticalSpacing(15)
        self.gridLayout_6.setContentsMargins(20, 10, 20, -1)
        self.tableWidget = QTableWidget(self.result_frame)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"QHeaderView::{\n"
"border:none;\n"
"boder-bottom:1px solid #d0c6ff;\n"
"text-align:left;\n"
"padding:3px 5px}")

        self.gridLayout_6.addWidget(self.tableWidget, 0, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.result_frame)

        self.stackedWidget_2.addWidget(self.Employee_page)
        self.Notification_page = QWidget()
        self.Notification_page.setObjectName(u"Notification_page")
        self.label_6 = QLabel(self.Notification_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(330, 150, 191, 61))
        self.label_6.setFont(font)
        self.stackedWidget_2.addWidget(self.Notification_page)
        self.Profile_page = QWidget()
        self.Profile_page.setObjectName(u"Profile_page")
        self.label_7 = QLabel(self.Profile_page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(330, 100, 101, 81))
        self.label_7.setFont(font)
        self.stackedWidget_2.addWidget(self.Profile_page)
        self.Setting_page = QWidget()
        self.Setting_page.setObjectName(u"Setting_page")
        self.label_8 = QLabel(self.Setting_page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(340, 200, 141, 51))
        self.label_8.setFont(font)
        self.stackedWidget_2.addWidget(self.Setting_page)

        self.verticalLayout_5.addWidget(self.stackedWidget_2)


        self.gridLayout.addWidget(self.main_mnu, 0, 2, 1, 1)

        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setStyleSheet(u"QWidget{\n"
"background-color: rgb(31, 149, 239);\n"
"color:white;\n"
"}\n"
"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"text-align:left;\n"
"height:30px;\n"
"border:none;\n"
"padding-left:10px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"}\n"
"QPushButton:checked{\n"
"background-color: rgb(245, 250, 254);\n"
"	color: rgb(31, 149, 239);\n"
" font-weight:bold;\n"
"}\n"
"	")
        self.verticalLayout_4 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 20, -1)
        self.label_2 = QLabel(self.icon_name_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(40, 40))
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setPixmap(QPixmap(u":/img/profile_pic.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.icon_name_widget)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.label_3.setFont(font2)

        self.horizontalLayout_2.addWidget(self.label_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 15, -1, -1)
        self.dashboard_2 = QPushButton(self.icon_name_widget)
        self.dashboard_2.setObjectName(u"dashboard_2")
        icon9 = QIcon()
        icon9.addFile(u":/img/dashboard_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon9.addFile(u":/img/dashboard.png", QSize(), QIcon.Normal, QIcon.On)
        self.dashboard_2.setIcon(icon9)
        self.dashboard_2.setCheckable(True)
        self.dashboard_2.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.dashboard_2)

        self.employee_2 = QPushButton(self.icon_name_widget)
        self.employee_2.setObjectName(u"employee_2")
        icon10 = QIcon()
        icon10.addFile(u":/img/profile_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon10.addFile(u":/img/profile.png", QSize(), QIcon.Normal, QIcon.On)
        self.employee_2.setIcon(icon10)
        self.employee_2.setCheckable(True)
        self.employee_2.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.employee_2)

        self.notification_2 = QPushButton(self.icon_name_widget)
        self.notification_2.setObjectName(u"notification_2")
        icon11 = QIcon()
        icon11.addFile(u":/img/notifications_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon11.addFile(u":/img/notifications.png", QSize(), QIcon.Normal, QIcon.On)
        self.notification_2.setIcon(icon11)
        self.notification_2.setCheckable(True)
        self.notification_2.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.notification_2)

        self.profile_2 = QPushButton(self.icon_name_widget)
        self.profile_2.setObjectName(u"profile_2")
        self.profile_2.setIcon(icon10)
        self.profile_2.setCheckable(True)
        self.profile_2.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.profile_2)

        self.setting_2 = QPushButton(self.icon_name_widget)
        self.setting_2.setObjectName(u"setting_2")
        icon12 = QIcon()
        icon12.addFile(u":/img/settings_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon12.addFile(u":/img/settings.png", QSize(), QIcon.Normal, QIcon.On)
        self.setting_2.setIcon(icon12)
        self.setting_2.setCheckable(True)
        self.setting_2.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.setting_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 395, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.signout_2 = QPushButton(self.icon_name_widget)
        self.signout_2.setObjectName(u"signout_2")
        icon13 = QIcon()
        icon13.addFile(u":/img/log_out_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon13.addFile(u":/img/log_out.png", QSize(), QIcon.Normal, QIcon.On)
        self.signout_2.setIcon(icon13)
        self.signout_2.setCheckable(True)
        self.signout_2.setAutoExclusive(False)

        self.verticalLayout_4.addWidget(self.signout_2)


        self.gridLayout.addWidget(self.icon_name_widget, 0, 1, 1, 1)

        self.icon_get_widget = QWidget(self.centralwidget)
        self.icon_get_widget.setObjectName(u"icon_get_widget")
        self.icon_get_widget.setStyleSheet(u"QWidget{\n"
"background-color: rgb(31, 149, 239);\n"
"}\n"
"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"border:none;\n"
"height:30px;\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:checked{\n"
"background-color: rgb(245, 250, 254);\n"
"	color: rgb(31, 149, 239);\n"
" font-weight:bold;\n"
"}\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.icon_get_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.icon_get_widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(40, 40))
        self.label.setMaximumSize(QSize(40, 40))
        self.label.setPixmap(QPixmap(u":/img/profile_pic.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 15, -1, -1)
        self.dashboard_1 = QPushButton(self.icon_get_widget)
        self.dashboard_1.setObjectName(u"dashboard_1")
        self.dashboard_1.setIcon(icon9)
        self.dashboard_1.setCheckable(True)
        self.dashboard_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.dashboard_1)

        self.employee_1 = QPushButton(self.icon_get_widget)
        self.employee_1.setObjectName(u"employee_1")
        self.employee_1.setIcon(icon10)
        self.employee_1.setCheckable(True)
        self.employee_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.employee_1)

        self.notification_1 = QPushButton(self.icon_get_widget)
        self.notification_1.setObjectName(u"notification_1")
        self.notification_1.setIcon(icon11)
        self.notification_1.setCheckable(True)
        self.notification_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.notification_1)

        self.profile_1 = QPushButton(self.icon_get_widget)
        self.profile_1.setObjectName(u"profile_1")
        self.profile_1.setIcon(icon10)
        self.profile_1.setCheckable(True)
        self.profile_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.profile_1)

        self.setting_1 = QPushButton(self.icon_get_widget)
        self.setting_1.setObjectName(u"setting_1")
        self.setting_1.setIcon(icon12)
        self.setting_1.setCheckable(True)
        self.setting_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.setting_1)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 395, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.signout_1 = QPushButton(self.icon_get_widget)
        self.signout_1.setObjectName(u"signout_1")
        self.signout_1.setIcon(icon13)
        self.signout_1.setCheckable(True)
        self.signout_1.setAutoExclusive(False)

        self.verticalLayout_2.addWidget(self.signout_1)


        self.gridLayout.addWidget(self.icon_get_widget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.menu_1.toggled.connect(self.icon_get_widget.setHidden)
        self.menu_1.toggled.connect(self.icon_name_widget.setVisible)
        self.setting_1.toggled.connect(self.setting_2.setChecked)
        self.profile_1.toggled.connect(self.profile_2.setChecked)
        self.notification_1.toggled.connect(self.notification_2.setChecked)
        self.employee_1.toggled.connect(self.employee_2.setChecked)
        self.dashboard_1.toggled.connect(self.dashboard_2.setChecked)
        self.dashboard_2.toggled.connect(self.dashboard_1.setChecked)
        self.employee_2.toggled.connect(self.employee_1.setChecked)
        self.notification_2.toggled.connect(self.notification_1.setChecked)
        self.profile_2.toggled.connect(self.profile_1.setChecked)
        self.setting_2.toggled.connect(self.setting_1.setChecked)
        self.signout_1.toggled.connect(MainWindow.close)
        self.signout_2.toggled.connect(self.icon_name_widget.close)

        self.stackedWidget_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menu_1.setText("")
        self.search_btn.setText("")
        self.profile_img.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"Employee Mangement System", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"id", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"DOJ", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Gender", None))
        self.gender.setItemText(0, "")
        self.gender.setItemText(1, QCoreApplication.translate("MainWindow", u"Male", None))
        self.gender.setItemText(2, QCoreApplication.translate("MainWindow", u"Female", None))
        self.gender.setItemText(3, QCoreApplication.translate("MainWindow", u"Other", None))

        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Mobile", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Designation", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Department", None))
        self.department.setItemText(0, "")
        self.department.setItemText(1, QCoreApplication.translate("MainWindow", u"IT", None))
        self.department.setItemText(2, QCoreApplication.translate("MainWindow", u"Account", None))
        self.department.setItemText(3, QCoreApplication.translate("MainWindow", u"Sales", None))
        self.department.setItemText(4, QCoreApplication.translate("MainWindow", u"HR", None))

        self.add_btn.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.update_btn.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.search_btn_2.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.clear_btn.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.delete_btn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.excel_btn.setText(QCoreApplication.translate("MainWindow", u"Export to Excel", None))
        self.pdf_btn.setText(QCoreApplication.translate("MainWindow", u"Export To PDF", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Gender", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"DOJ", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Mobile", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Designation", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Department", None));
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Notification", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Setting", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.dashboard_2.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.employee_2.setText(QCoreApplication.translate("MainWindow", u"Employee", None))
        self.notification_2.setText(QCoreApplication.translate("MainWindow", u"Notification", None))
        self.profile_2.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.setting_2.setText(QCoreApplication.translate("MainWindow", u"Setting", None))
        self.signout_2.setText(QCoreApplication.translate("MainWindow", u"Sing Out", None))
        self.label.setText("")
        self.dashboard_1.setText("")
        self.employee_1.setText("")
        self.notification_1.setText("")
        self.profile_1.setText("")
        self.setting_1.setText("")
        self.signout_1.setText("")
        self.clear_btn.clicked.connect(self.clear_field)
        self.add_btn.clicked.connect(self.add_employee)
        self.update_btn.clicked.connect(self.update_employee)
        self.delete_btn.clicked.connect(self.delete_employee)
        self.search_btn_2.clicked.connect(self.search_employee)
        self.pdf_btn.clicked.connect(self.export_to_pdf)
        self.excel_btn.clicked.connect(self.export_to_excel)
        self.signout_1.clicked.connect(self.redirect_to_login)
        self.signout_2.clicked.connect(self.redirect_to_login)
        self.load_data()
        self.tableWidget.cellDoubleClicked.connect(self.on_tableWidget_cellDoubleClicked)
    
    # retranslateUi
    def redirect_to_login(self):
        self.manager.clear_session()
        self.manager.close_current_window(self)
        self.manager.show_login_window()

    @Slot(int, int)        

    def clear_field(self):  
        self.id.clear()
        self.name.clear() 
        self.mobile.clear() 
        self.gender.setCurrentText("")
        self.department.setCurrentText("")
        self.designation.clear()
        self.doj.clear()

    def update_employee(self):
        id = self.id.text()
        name = self.name.text()
        mobile = self.mobile.text()
        gender = self.gender.currentText()
        department = self.department.currentText()
        designation = self.designation.text()
        doj = self.doj.text()
        
        if name == "" or mobile == "" or gender == "" or department == "" or designation == "" or doj == "":
            QMessageBox.critical(None, 'Error', 'Please fill all fields')
            return

        # Database connection parameters
        
        server = 'ALOK\\SQLEXPRESS'
        database = 'alokdb'
        try:
            connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;"
            conn = pyodbc.connect(connection_string)
            cursor = conn.cursor()
            
            
            update_query = "UPDATE employe SET name=?, mobile=?, gender=?, department=?, designation=?, doj=? WHERE id="+id
            cursor.execute(update_query, (name, mobile, gender, department, designation, doj))
            conn.commit()

            QMessageBox.information(None, 'EMP Update', 'Data Update successful!')
            self.clear_field()
            self.load_data()

        except pyodbc.Error as e:
            QMessageBox.critical(None, 'Database Error', f'An error occurred: {str(e)}')

        finally:
        # Close the database connection
         if cursor:
            cursor.close()
         if conn:
            conn.close()

            # Delete employee
    def delete_employee(self):
        id = self.id.text()
        server = 'ALOK\\SQLEXPRESS'
        database = 'alokdb'
        
        
        try:
            connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;"
            conn = pyodbc.connect(connection_string)
            cursor = conn.cursor()

        # Delete query
            delete_query = "DELETE FROM employe WHERE id="+id
            cursor.execute(delete_query)
            conn.commit()

            QMessageBox.information(None, 'EMP Delete', 'Data Delete successful!')
            self.clear_field()
            self.load_data()

        except pyodbc.Error as e:
            QMessageBox.critical(None, 'Database Error', f'An error occurred: {str(e)}')

        finally:
        # Close the database connection
         if cursor:
            cursor.close()
         if conn:
            conn.close()


      # Add employee   
    def add_employee(self):
        name = self.name.text()
        doj = self.doj.text()
        gender = self.gender.currentText()
        mobile = self.mobile.text()
        designation = self.designation.text()
        department = self.department.currentText()


        if name == "" or mobile == "" or gender == "" or department == "" or designation == "" or doj == "" :
            QMessageBox.critical(None, 'Error', 'Please fill all fields')
            return
       
        
        # Database connection parameters
        server = 'ALOK\\SQLEXPRESS'
        database = 'alokdb'
        
        try:
            # Establish connection to the database
            connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;"
            conn = pyodbc.connect(connection_string)
            cursor = conn.cursor()
            insert_query = "INSERT INTO employe (name, mobile, gender, department, designation, doj) VALUES (?, ?, ?, ?, ?, ?)"
            cursor.execute(insert_query, (name, mobile, gender, department, designation, doj))
            conn.commit()
            QMessageBox.information(None, ' EMP Registration', 'Data Insert successful!')
            self.clear_field()
            self.load_data()
        
        except pyodbc.Error as e:
           QMessageBox.critical(None, 'Database Error', f'An error occurred: {str(e)}')
        
        finally:
            # Close the database connection
            if cursor:
                cursor.close()
            if conn:
                conn.close() 

   
   
    def export_to_pdf(self): 
         file_dialog = QFileDialog()
         file_Path, _ = file_dialog.getSaveFileName(self, "Save PDF", "", "PDF Files (*.pdf);;All Files (*)")

         if file_Path:
            pdf_document =SimpleDocTemplate(file_Path, pagesize=letter)
            n = self.tableWidget.columnCount()
            headers = [self.tableWidget.horizontalHeaderItem(col).text() for col in range(n-1)]
            data = [headers]

            for row in range(self.tableWidget.rowCount()):
                row_data = [self.tableWidget.item(row, col).text() if self.tableWidget.item(row, col) is not None else '' for col in range(n-1)]
                data.append(row_data)

            pdf_table = Table(data)

            style = TableStyle([
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 8),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ])   

            pdf_table.setStyle(style)

            pdf_document.build([pdf_table])
            print(f"Table Exported to {file_Path}")

               

            

    #export to excel
    def export_to_excel(self):
        data = []
        self.headers = [self.tableWidget.horizontalHeaderItem(col).text() for col in range(self.tableWidget.columnCount())]
        for row in range(self.tableWidget.rowCount()):
            row_data = [self.tableWidget.item(row, col).text() if self.tableWidget.item(row, col) is not None else '' for col in range(self.tableWidget.columnCount())]
            data.append(row_data)

        df = pd.DataFrame(data, columns=self.headers)
        df_filtered = df.iloc[:, :-1]
        file_dialog = QFileDialog()
        file_Path, _ = file_dialog.getSaveFileName(self, "Save Excel File", "", "Excel Files (*.xlsx);;All Files (*)")


        if file_Path:
            df_filtered.to_excel(file_Path, index=False)
            print(f"Table Exported to {file_Path}")

            

                  

                # search employee
    def search_employee(self):
        name = self.name.text()
        mobile = self.mobile.text()
        gender = self.gender.currentText()
        department = self.department.currentText()
        designation = self.designation.text()


    # Database connection parameters
        server = 'ALOK\\SQLEXPRESS'
        database = 'alokdb'
        try:
            connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;"
            conn = pyodbc.connect(connection_string)
            cursor = conn.cursor()

        # Start building the query
            query = "SELECT * FROM employe WHERE 1=1"
            params = []

        # Append conditions based on provided inputs
            if name:
                query += " AND name LIKE ?"
                params.append(f"%{name}%")
            if mobile:
                query += " AND mobile LIKE ?"
                params.append(f"%{mobile}%")
            if gender:
                query += " AND gender = ?"
                params.append(gender)
            if department:
               query += " AND department = ?"
               params.append(department)
            if designation:
               query += " AND designation LIKE ?"
               params.append(f"%{designation}%")
           

            cursor.execute(query, params)
            rows = cursor.fetchall()

    

        # Insert the search results into the table
            self.tableWidget.setRowCount(len(rows))
            for row_idx, row in enumerate(rows):
                for col_idx, cell in enumerate(row):
                    self.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(cell)))

        except pyodbc.Error as e:
            QMessageBox.critical(None, 'Database Error', f'An error occurred: {str(e)}')

        finally:
        # Close the database connection
         if cursor:
            cursor.close()
         if conn:
            conn.close()




#load a table data
    def load_data(self):
        columns, rows = fetch_data()
        self.tableWidget.setColumnCount(len(columns))
        self.tableWidget.setRowCount(len(rows))
        self.tableWidget.setHorizontalHeaderLabels(columns)

        for row_idx, row in enumerate(rows):
            for col_idx, cell in enumerate(row):
                self.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(cell)))

    def on_tableWidget_cellDoubleClicked(self, row, column):
        # Get the data for the clicked row
        item_id = self.tableWidget.item(row, 0).text()
        item_name = self.tableWidget.item(row, 1).text()
        item_doj = self.tableWidget.item(row, 2).text()
        item_gender = self.tableWidget.item(row, 3).text()
        item_mobile = self.tableWidget.item(row, 4).text()
        item_designation = self.tableWidget.item(row, 5).text()
        item_department = self.tableWidget.item(row, 6).text()

        # Populate form fields with the data
        self.id.setText(item_id)
        self.name.setText(item_name)
        self.mobile.setText(item_mobile)
        self.gender.setCurrentText(item_gender)
        
        self.department.setCurrentText(item_department)
        self.designation.setText(item_designation)
        self.doj.setDate(QDate.fromString(item_doj, 'yyyy-MM-dd'))  

def fetch_data():
        server = 'ALOK\\SQLEXPRESS'
        database = 'alokdb'
        conn = pyodbc.connect(f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employe")
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        return columns, rows



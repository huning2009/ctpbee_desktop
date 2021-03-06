# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signin.ui',
# licensing of 'signin.ui' applies.
#
# Created: Fri Dec 27 14:08:14 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_SignIn(object):
    def setupUi(self, SignIn):
        SignIn.setObjectName("SignIn")
        SignIn.setEnabled(True)
        SignIn.resize(315, 368)
        SignIn.setMinimumSize(QtCore.QSize(315, 368))
        SignIn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/menu/images/bee_temp_grey.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SignIn.setWindowIcon(icon)
        SignIn.setAutoFillBackground(False)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(SignIn)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.icon = QtWidgets.QLabel(SignIn)
        self.icon.setMinimumSize(QtCore.QSize(0, 100))
        self.icon.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.icon.setStyleSheet("image: url(:/menu/images/bee_temp_grey.png);\n"
"")
        self.icon.setText("")
        self.icon.setObjectName("icon")
        self.verticalLayout_3.addWidget(self.icon)
        self.login_tab = QtWidgets.QStackedWidget(SignIn)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.login_tab.sizePolicy().hasHeightForWidth())
        self.login_tab.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.login_tab.setFont(font)
        self.login_tab.setStyleSheet("")
        self.login_tab.setObjectName("login_tab")
        self.login_tabPage1 = QtWidgets.QWidget()
        self.login_tabPage1.setObjectName("login_tabPage1")
        self.gridLayout = QtWidgets.QGridLayout(self.login_tabPage1)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayout.addLayout(self.horizontalLayout_4, 5, 1, 1, 1)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.login_tabPage1)
        self.scrollArea_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 262, 171))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.password_sim = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.password_sim.setMinimumSize(QtCore.QSize(0, 24))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.password_sim.setFont(font)
        self.password_sim.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_sim.setObjectName("password_sim")
        self.gridLayout_4.addWidget(self.password_sim, 1, 1, 1, 1)
        self.interface_sim = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.interface_sim.setMinimumSize(QtCore.QSize(0, 24))
        self.interface_sim.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setWeight(50)
        font.setBold(False)
        self.interface_sim.setFont(font)
        self.interface_sim.setObjectName("interface_sim")
        self.interface_sim.addItem("")
        self.interface_sim.addItem("")
        self.gridLayout_4.addWidget(self.interface_sim, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(50)
        font.setBold(False)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(50)
        font.setBold(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        self.other = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.other.setMinimumSize(QtCore.QSize(0, 24))
        self.other.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setWeight(50)
        font.setBold(False)
        self.other.setFont(font)
        self.other.setObjectName("other")
        self.other.addItem("")
        self.other.addItem("")
        self.gridLayout_4.addWidget(self.other, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(50)
        font.setBold(False)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 3, 0, 1, 1)
        self.userid_sim = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.userid_sim.setMinimumSize(QtCore.QSize(0, 24))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.userid_sim.setFont(font)
        self.userid_sim.setMouseTracking(False)
        self.userid_sim.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.userid_sim.setEditable(True)
        self.userid_sim.setObjectName("userid_sim")
        self.gridLayout_4.addWidget(self.userid_sim, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(50)
        font.setBold(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 1, 0, 1, 1)
        self.remember_me_sim = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.remember_me_sim.setFont(font)
        self.remember_me_sim.setChecked(True)
        self.remember_me_sim.setObjectName("remember_me_sim")
        self.gridLayout_4.addWidget(self.remember_me_sim, 4, 1, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout.addWidget(self.scrollArea_2, 0, 0, 1, 1)
        self.login_tab.addWidget(self.login_tabPage1)
        self.login_tabPage2 = QtWidgets.QWidget()
        self.login_tabPage2.setObjectName("login_tabPage2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.login_tabPage2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.login_tabPage2)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -116, 250, 299))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.password = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.password.setEnabled(True)
        self.password.setMinimumSize(QtCore.QSize(0, 24))
        self.password.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setWeight(50)
        font.setBold(False)
        self.password.setFont(font)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setPlaceholderText("")
        self.password.setObjectName("password")
        self.gridLayout_3.addWidget(self.password, 1, 1, 1, 1)
        self.td_address = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.td_address.setMinimumSize(QtCore.QSize(0, 24))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.td_address.setFont(font)
        self.td_address.setEditable(True)
        self.td_address.setObjectName("td_address")
        self.gridLayout_3.addWidget(self.td_address, 5, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(50)
        font.setBold(False)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 4, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(50)
        font.setBold(False)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(50)
        font.setBold(False)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 3, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(50)
        font.setBold(False)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 7, 0, 1, 1)
        self.userid = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.userid.setMinimumSize(QtCore.QSize(0, 24))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.userid.setFont(font)
        self.userid.setEditable(True)
        self.userid.setObjectName("userid")
        self.gridLayout_3.addWidget(self.userid, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(50)
        font.setBold(False)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 2, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(50)
        font.setBold(False)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 6, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(50)
        font.setBold(False)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 1, 0, 1, 1)
        self.appid = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.appid.setMinimumSize(QtCore.QSize(0, 24))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.appid.setFont(font)
        self.appid.setEditable(True)
        self.appid.setObjectName("appid")
        self.gridLayout_3.addWidget(self.appid, 4, 1, 1, 1)
        self.md_address = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.md_address.setMinimumSize(QtCore.QSize(0, 24))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.md_address.setFont(font)
        self.md_address.setEditable(True)
        self.md_address.setObjectName("md_address")
        self.gridLayout_3.addWidget(self.md_address, 6, 1, 1, 1)
        self.interface_ = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.interface_.setMinimumSize(QtCore.QSize(0, 24))
        self.interface_.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.interface_.setFont(font)
        self.interface_.setObjectName("interface_")
        self.interface_.addItem("")
        self.interface_.addItem("")
        self.gridLayout_3.addWidget(self.interface_, 7, 1, 1, 1)
        self.auth_code = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.auth_code.setMinimumSize(QtCore.QSize(0, 24))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.auth_code.setFont(font)
        self.auth_code.setEditable(True)
        self.auth_code.setObjectName("auth_code")
        self.gridLayout_3.addWidget(self.auth_code, 3, 1, 1, 1)
        self.brokerid = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.brokerid.setMinimumSize(QtCore.QSize(0, 24))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.brokerid.setFont(font)
        self.brokerid.setEditable(True)
        self.brokerid.setObjectName("brokerid")
        self.gridLayout_3.addWidget(self.brokerid, 2, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(50)
        font.setBold(False)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 5, 0, 1, 1)
        self.remember_me = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.remember_me.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setWeight(50)
        font.setBold(False)
        self.remember_me.setFont(font)
        self.remember_me.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.remember_me.setChecked(True)
        self.remember_me.setObjectName("remember_me")
        self.gridLayout_3.addWidget(self.remember_me, 8, 1, 1, 1)
        self.gridLayout_3.setColumnStretch(1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.login_tab.addWidget(self.login_tabPage2)
        self.verticalLayout_3.addWidget(self.login_tab)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.sign_in_btn = QtWidgets.QPushButton(SignIn)
        self.sign_in_btn.setEnabled(True)
        self.sign_in_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.sign_in_btn.setFont(font)
        self.sign_in_btn.setObjectName("sign_in_btn")
        self.horizontalLayout.addWidget(self.sign_in_btn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.retranslateUi(SignIn)
        self.login_tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SignIn)

    def retranslateUi(self, SignIn):
        SignIn.setWindowTitle(QtWidgets.QApplication.translate("SignIn", "Form", None, -1))
        self.interface_sim.setItemText(0, QtWidgets.QApplication.translate("SignIn", "ctp", None, -1))
        self.interface_sim.setItemText(1, QtWidgets.QApplication.translate("SignIn", "ctp_se", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("SignIn", "接  口", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("SignIn", "用户名", None, -1))
        self.other.setItemText(0, QtWidgets.QApplication.translate("SignIn", "simnow24小时", None, -1))
        self.other.setItemText(1, QtWidgets.QApplication.translate("SignIn", "simnow移动", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("SignIn", "前  置", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("SignIn", "密  码", None, -1))
        self.remember_me_sim.setText(QtWidgets.QApplication.translate("SignIn", "记住我", None, -1))
        self.label_10.setText(QtWidgets.QApplication.translate("SignIn", "产品名称", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("SignIn", "用户名", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate("SignIn", "认证码", None, -1))
        self.label_13.setText(QtWidgets.QApplication.translate("SignIn", "接口", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("SignIn", "期货公司\n"
"编码", None, -1))
        self.label_12.setText(QtWidgets.QApplication.translate("SignIn", "行情前置", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("SignIn", "密码", None, -1))
        self.interface_.setItemText(0, QtWidgets.QApplication.translate("SignIn", "ctp", None, -1))
        self.interface_.setItemText(1, QtWidgets.QApplication.translate("SignIn", "ctp_se", None, -1))
        self.label_11.setText(QtWidgets.QApplication.translate("SignIn", "交易前置", None, -1))
        self.remember_me.setText(QtWidgets.QApplication.translate("SignIn", "记住我", None, -1))
        self.sign_in_btn.setText(QtWidgets.QApplication.translate("SignIn", "登    录", None, -1))

import app.resource.mainwindow_rc

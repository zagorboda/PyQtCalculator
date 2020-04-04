# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 400)
        MainWindow.setStyleSheet("background-color:#fff")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.result = QtWidgets.QLabel(self.centralWidget)
        self.result.setGeometry(QtCore.QRect(30, 20, 230, 30))
        self.result.setText("")
        self.result.setObjectName("result")
        self.btn_clear = QtWidgets.QPushButton(self.centralWidget)
        self.btn_clear.setGeometry(QtCore.QRect(30, 60, 50, 50))
        self.btn_clear.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_clear.setStyleSheet("background-color:#FF7F00;\n"
"border-radius:10px;")
        self.btn_clear.setObjectName("btn_clear")
        self.btn_div = QtWidgets.QPushButton(self.centralWidget)
        self.btn_div.setGeometry(QtCore.QRect(210, 60, 50, 50))
        self.btn_div.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_div.setStyleSheet("background-color:#FF7F00;\n"
"border-radius:10px;")
        self.btn_div.setObjectName("btn_div")
        self.btn_mlt = QtWidgets.QPushButton(self.centralWidget)
        self.btn_mlt.setGeometry(QtCore.QRect(210, 120, 50, 50))
        self.btn_mlt.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_mlt.setStyleSheet("background-color:#FF7F00;\n"
"border-radius:10px;")
        self.btn_mlt.setObjectName("btn_mlt")
        self.btn_7 = QtWidgets.QPushButton(self.centralWidget)
        self.btn_7.setGeometry(QtCore.QRect(30, 120, 50, 50))
        self.btn_7.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_7.setStyleSheet("background-color:#52de65;\n"
"border-radius:10px;")
        self.btn_7.setObjectName("btn_7")
        self.btn_9 = QtWidgets.QPushButton(self.centralWidget)
        self.btn_9.setGeometry(QtCore.QRect(150, 120, 50, 50))
        self.btn_9.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_9.setStyleSheet("background-color:#52de65;\n"
"border-radius:10px;")
        self.btn_9.setObjectName("btn_9")
        self.btn_8 = QtWidgets.QPushButton(self.centralWidget)
        self.btn_8.setGeometry(QtCore.QRect(90, 120, 50, 50))
        self.btn_8.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_8.setStyleSheet("background-color:#52de65;\n"
"border-radius:10px;")
        self.btn_8.setObjectName("btn_8")
        self.btn_minus = QtWidgets.QPushButton(self.centralWidget)
        self.btn_minus.setGeometry(QtCore.QRect(210, 180, 50, 50))
        self.btn_minus.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_minus.setStyleSheet("background-color:#FF7F00;\n"
"border-radius:10px;")
        self.btn_minus.setObjectName("btn_minus")
        self.btn_4 = QtWidgets.QPushButton(self.centralWidget)
        self.btn_4.setGeometry(QtCore.QRect(30, 180, 50, 50))
        self.btn_4.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_4.setStyleSheet("background-color:#52de65;\n"
"border-radius:10px;")
        self.btn_4.setObjectName("btn_4")
        self.btn_plus = QtWidgets.QPushButton(self.centralWidget)
        self.btn_plus.setGeometry(QtCore.QRect(210, 240, 50, 50))
        self.btn_plus.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_plus.setStyleSheet("background-color:#FF7F00;\n"
"border-radius:10px;")
        self.btn_plus.setObjectName("btn_plus")
        self.btn_1 = QtWidgets.QPushButton(self.centralWidget)
        self.btn_1.setGeometry(QtCore.QRect(30, 240, 50, 50))
        self.btn_1.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_1.setStyleSheet("background-color:#52de65;\n"
"border-radius:10px;")
        self.btn_1.setObjectName("btn_1")
        self.btn_2 = QtWidgets.QPushButton(self.centralWidget)
        self.btn_2.setGeometry(QtCore.QRect(90, 240, 50, 50))
        self.btn_2.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_2.setStyleSheet("background-color:#52de65;\n"
"border-radius:10px;")
        self.btn_2.setObjectName("btn_2")
        self.btn_6 = QtWidgets.QPushButton(self.centralWidget)
        self.btn_6.setGeometry(QtCore.QRect(150, 180, 50, 50))
        self.btn_6.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_6.setStyleSheet("background-color:#52de65;\n"
"border-radius:10px;")
        self.btn_6.setObjectName("btn_6")
        self.btn_5 = QtWidgets.QPushButton(self.centralWidget)
        self.btn_5.setGeometry(QtCore.QRect(90, 180, 50, 50))
        self.btn_5.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_5.setStyleSheet("background-color:#52de65;\n"
"border-radius:10px;")
        self.btn_5.setObjectName("btn_5")
        self.btn_3 = QtWidgets.QPushButton(self.centralWidget)
        self.btn_3.setGeometry(QtCore.QRect(150, 240, 50, 50))
        self.btn_3.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_3.setStyleSheet("background-color:#52de65;\n"
"border-radius:10px;")
        self.btn_3.setObjectName("btn_3")
        self.btn_eq = QtWidgets.QPushButton(self.centralWidget)
        self.btn_eq.setGeometry(QtCore.QRect(210, 300, 50, 50))
        self.btn_eq.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_eq.setStyleSheet("background-color:#26beff;\n"
"border-radius:10px;")
        self.btn_eq.setObjectName("btn_eq")
        self.btn_0 = QtWidgets.QPushButton(self.centralWidget)
        self.btn_0.setGeometry(QtCore.QRect(30, 300, 110, 50))
        self.btn_0.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_0.setStyleSheet("background-color:#52de65;\n"
"border-radius:10px;")
        self.btn_0.setObjectName("btn_0")
        self.btn_point = QtWidgets.QPushButton(self.centralWidget)
        self.btn_point.setGeometry(QtCore.QRect(150, 300, 50, 50))
        self.btn_point.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_point.setStyleSheet("background-color:#52de65;\n"
"border-radius:10px;")
        self.btn_point.setObjectName("btn_point")
        self.btn_left = QtWidgets.QPushButton(self.centralWidget)
        self.btn_left.setGeometry(QtCore.QRect(90, 60, 50, 50))
        self.btn_left.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_left.setStyleSheet("background-color:#FF7F00;\n"
"border-radius:10px;")
        self.btn_left.setObjectName("btn_left")
        self.btn_right = QtWidgets.QPushButton(self.centralWidget)
        self.btn_right.setGeometry(QtCore.QRect(150, 60, 50, 50))
        self.btn_right.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_right.setStyleSheet("background-color:#FF7F00;\n"
"border-radius:10px;")
        self.btn_right.setObjectName("btn_right")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.btn_clear.setText(_translate("MainWindow", "AC"))
        self.btn_div.setText(_translate("MainWindow", "/"))
        self.btn_mlt.setText(_translate("MainWindow", "x"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_minus.setText(_translate("MainWindow", "-"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_eq.setText(_translate("MainWindow", "="))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_point.setText(_translate("MainWindow", ","))
        self.btn_left.setText(_translate("MainWindow", "("))
        self.btn_right.setText(_translate("MainWindow", ")"))

# Form implementation generated from reading ui file 'E:\Personal Projects\___Pycharm___\FN4\ui\Bill.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(454, 584)
        MainWindow.setBaseSize(QtCore.QSize(800, 600))
        MainWindow.setStyleSheet("background-color: transparent")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-180, -20, 1000, 600))
        self.label.setMaximumSize(QtCore.QSize(1000, 600))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("E:\\Personal Projects\\___Pycharm___\\FN4\\ui\\../images/1.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 30, 371, 511))
        self.label_3.setStyleSheet("\n"
"background-color: rgb(0, 0, 0,150);\n"
"")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 40, 371, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"    border: none")
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(60, 220, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"    border: none")
        self.label_6.setObjectName("label_6")
        self.pushButtonPay = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonPay.setGeometry(QtCore.QRect(260, 480, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(20)
        self.pushButtonPay.setFont(font)
        self.pushButtonPay.setStyleSheet("background-color: rgb(173, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"  border-radius: 5px;\n"
"    padding: 5px")
        self.pushButtonPay.setObjectName("pushButtonPay")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 100, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"    border: none")
        self.label_2.setObjectName("label_2")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(60, 140, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"    border: none")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(60, 340, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"    border: none")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(60, 300, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"    border: none")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(60, 260, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"    border: none")
        self.label_11.setObjectName("label_11")
        self.pushButtonBack = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonBack.setGeometry(QtCore.QRect(90, 480, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(20)
        self.pushButtonBack.setFont(font)
        self.pushButtonBack.setStyleSheet("background-color: rgb(173, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"  border-radius: 5px;\n"
"    padding: 5px")
        self.pushButtonBack.setObjectName("pushButtonBack")
        self.labelTheater = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelTheater.setGeometry(QtCore.QRect(160, 230, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.labelTheater.setFont(font)
        self.labelTheater.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"    border: none")
        self.labelTheater.setText("")
        self.labelTheater.setObjectName("labelTheater")
        self.labelMail = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelMail.setGeometry(QtCore.QRect(130, 140, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.labelMail.setFont(font)
        self.labelMail.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"    border: none")
        self.labelMail.setText("")
        self.labelMail.setObjectName("labelMail")
        self.labelUsername = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelUsername.setGeometry(QtCore.QRect(180, 100, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.labelUsername.setFont(font)
        self.labelUsername.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"    border: none")
        self.labelUsername.setText("")
        self.labelUsername.setObjectName("labelUsername")
        self.labelTime = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelTime.setGeometry(QtCore.QRect(160, 270, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.labelTime.setFont(font)
        self.labelTime.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"    border: none")
        self.labelTime.setText("")
        self.labelTime.setObjectName("labelTime")
        self.labelSeat = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelSeat.setGeometry(QtCore.QRect(160, 310, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.labelSeat.setFont(font)
        self.labelSeat.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"    border: none")
        self.labelSeat.setText("")
        self.labelSeat.setObjectName("labelSeat")
        self.label_17 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(60, 420, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"    border: none")
        self.label_17.setObjectName("label_17")
        self.labelOrder = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelOrder.setGeometry(QtCore.QRect(160, 350, 221, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.labelOrder.setFont(font)
        self.labelOrder.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"    border: none")
        self.labelOrder.setText("")
        self.labelOrder.setObjectName("labelOrder")
        self.labelTotal = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelTotal.setGeometry(QtCore.QRect(130, 420, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.labelTotal.setFont(font)
        self.labelTotal.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"    border: none")
        self.labelTotal.setText("")
        self.labelTotal.setObjectName("labelTotal")
        self.label_12 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(60, 180, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"    border: none")
        self.label_12.setObjectName("label_12")
        self.labelMovie = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelMovie.setGeometry(QtCore.QRect(130, 180, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.labelMovie.setFont(font)
        self.labelMovie.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"    border: none")
        self.labelMovie.setText("")
        self.labelMovie.setObjectName("labelMovie")
        self.label.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_2.raise_()
        self.labelUsername.raise_()
        self.label_8.raise_()
        self.labelMail.raise_()
        self.label_6.raise_()
        self.labelTheater.raise_()
        self.label_11.raise_()
        self.labelTime.raise_()
        self.label_10.raise_()
        self.labelSeat.raise_()
        self.label_9.raise_()
        self.labelOrder.raise_()
        self.label_17.raise_()
        self.labelTotal.raise_()
        self.pushButtonBack.raise_()
        self.pushButtonPay.raise_()
        self.label_12.raise_()
        self.labelMovie.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "GFlix Cinema"))
        self.label_6.setText(_translate("MainWindow", "Theater :"))
        self.pushButtonPay.setText(_translate("MainWindow", "Pay"))
        self.label_2.setText(_translate("MainWindow", "User Name :"))
        self.label_8.setText(_translate("MainWindow", "Email :"))
        self.label_9.setText(_translate("MainWindow", "Order :"))
        self.label_10.setText(_translate("MainWindow", "Seat :"))
        self.label_11.setText(_translate("MainWindow", "Showtime :"))
        self.pushButtonBack.setText(_translate("MainWindow", "Back"))
        self.label_17.setText(_translate("MainWindow", "Total:"))
        self.label_12.setText(_translate("MainWindow", "Movie :"))

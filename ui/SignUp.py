# Form implementation generated from reading ui file 'E:\Personal Projects\___Pycharm___\FN1\ui\SignUp.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1016, 637)
        MainWindow.setBaseSize(QtCore.QSize(800, 600))
        MainWindow.setStyleSheet("background-color: transparent")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(6, 6, 1000, 600))
        self.label.setMaximumSize(QtCore.QSize(1000, 600))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("E:\\Personal Projects\\___Pycharm___\\FN1\\ui\\../images/thumble-muataikhoannetflixvn.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 181, 151))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("E:\\Personal Projects\\___Pycharm___\\FN1\\ui\\../images/logoreal.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.lineEditGmail = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditGmail.setGeometry(QtCore.QRect(360, 160, 291, 41))
        self.lineEditGmail.setStyleSheet("background-color: rgb(212, 229, 255,150);\n"
"border:rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"    padding: 5px")
        self.lineEditGmail.setObjectName("lineEditGmail")
        self.lineEditUsername = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditUsername.setGeometry(QtCore.QRect(360, 240, 291, 41))
        self.lineEditUsername.setStyleSheet("background-color: rgb(212, 229, 255,150);\n"
"border:rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"    padding: 5px")
        self.lineEditUsername.setObjectName("lineEditUsername")
        self.lineEditPw = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditPw.setGeometry(QtCore.QRect(360, 320, 291, 41))
        self.lineEditPw.setStyleSheet("background-color: rgb(212, 229, 255,150);\n"
"border:rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"    padding: 5px")
        self.lineEditPw.setText("")
        self.lineEditPw.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEditPw.setReadOnly(False)
        self.lineEditPw.setObjectName("lineEditPw")
        self.lineEditRePw = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditRePw.setGeometry(QtCore.QRect(360, 400, 291, 41))
        self.lineEditRePw.setStyleSheet("background-color: rgb(212, 229, 255,150);\n"
"border:rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"    padding: 5px")
        self.lineEditRePw.setText("")
        self.lineEditRePw.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEditRePw.setObjectName("lineEditRePw")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(360, 80, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"    border: none")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(370, 130, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"    border: none")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(370, 210, 141, 31))
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
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(370, 290, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"    border: none")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(370, 370, 141, 31))
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
        self.radioButtonAgree = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButtonAgree.setGeometry(QtCore.QRect(360, 455, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(12)
        self.radioButtonAgree.setFont(font)
        self.radioButtonAgree.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButtonAgree.setObjectName("radioButtonAgree")
        self.pushButtonSignUp = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonSignUp.setGeometry(QtCore.QRect(400, 520, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(15)
        self.pushButtonSignUp.setFont(font)
        self.pushButtonSignUp.setStyleSheet("background-color: rgb(173, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"  border-radius: 5px;\n"
"    padding: 5px")
        self.pushButtonSignUp.setObjectName("pushButtonSignUp")
        self.pushButtonSignIn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonSignIn.setGeometry(QtCore.QRect(360, 480, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSignIn.setFont(font)
        self.pushButtonSignIn.setStyleSheet("background-color: transparent;\n"
"color: rgb(170, 0, 0);\n"
"    border: none")
        self.pushButtonSignIn.setObjectName("pushButtonSignIn")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(270, 50, 471, 521))
        self.widget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget.setObjectName("widget")
        self.label.raise_()
        self.widget.raise_()
        self.label_2.raise_()
        self.lineEditGmail.raise_()
        self.lineEditUsername.raise_()
        self.lineEditPw.raise_()
        self.lineEditRePw.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.radioButtonAgree.raise_()
        self.pushButtonSignUp.raise_()
        self.pushButtonSignIn.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1016, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEditGmail.setText(_translate("MainWindow", "Mời nhập Gmail"))
        self.lineEditUsername.setText(_translate("MainWindow", "Chọn user là tên hiển thị và đăng nhập của bạn"))
        self.label_4.setText(_translate("MainWindow", "Sign Up"))
        self.label_5.setText(_translate("MainWindow", "Gmail"))
        self.label_6.setText(_translate("MainWindow", "Username:"))
        self.label_7.setText(_translate("MainWindow", "Password"))
        self.label_8.setText(_translate("MainWindow", "Password Again"))
        self.radioButtonAgree.setText(_translate("MainWindow", "Customers have agreed to the terms and conditions of GFlix membership"))
        self.pushButtonSignUp.setText(_translate("MainWindow", "SIGN UP"))
        self.pushButtonSignIn.setText(_translate("MainWindow", "Sign In Now!!! ->"))

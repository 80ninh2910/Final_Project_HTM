# Form implementation generated from reading ui file 'E:\Personal Projects\___Pycharm___\FN5\ui\Discount.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        MainWindow.resize(1009, 605)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"    border: none")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 0, 141, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: transparent;\n"
"\n"
"    border: none")
        self.pushButton_3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("E:\\Personal Projects\\___Pycharm___\\FN5\\ui\\../images/logoreal.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButtonDiscounts = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonDiscounts.setGeometry(QtCore.QRect(770, 70, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonDiscounts.setFont(font)
        self.pushButtonDiscounts.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 0);\n"
"    border: none")
        self.pushButtonDiscounts.setObjectName("pushButtonDiscounts")
        self.pushButtonAboutUs = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonAboutUs.setGeometry(QtCore.QRect(890, 70, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonAboutUs.setFont(font)
        self.pushButtonAboutUs.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"    border: none")
        self.pushButtonAboutUs.setObjectName("pushButtonAboutUs")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 100, 1001, 461))
        font = QtGui.QFont()
        font.setItalic(True)
        font.setKerning(True)
        self.scrollArea.setFont(font)
        self.scrollArea.setStyleSheet("QScrollBar::sub-line:vertical {\n"
"    border:none;\n"
"    background-color:rgb(59,59,90);\n"
"    height: 15px;\n"
"    border-top-left-radius:7px;\n"
"    border-top-right-radius:7px;\n"
"    subcontrol-position:top;\n"
"    subcontrol-origin:margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {\n"
"    background-color:rgb(255,0,127);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"    background-color:rgb(185,0,92);\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    border:none;\n"
"    background-color:rgb(59,59,90);\n"
"    height: 15px;\n"
"    border-top-left-radius:7px;\n"
"    border-top-right-radius:7px;\n"
"    subcontrol-position:bottom;\n"
"    subcontrol-origin:margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {\n"
"    background-color:rgb(255,0,127);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"    background-color:rgb(185,0,92);\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical{\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{\n"
"    background: none;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border:none;\n"
"    background-color:rgb(59,59,90);\n"
"    height: 15px;\n"
"    border-top-left-radius:7px;\n"
"    border-top-right-radius:7px;\n"
"    subcontrol-position:top;\n"
"    subcontrol-origin:margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"    background-color:rgb(255,0,127);\n"
"}\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"    background-color:rgb(185,0,92);\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border:none;\n"
"    background-color:rgb(59,59,90);\n"
"    height: 15px;\n"
"    border-top-left-radius:7px;\n"
"    border-top-right-radius:7px;\n"
"    subcontrol-position:bottom;\n"
"    subcontrol-origin:margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"    background-color:rgb(255,0,127);\n"
"}\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"    background-color:rgb(185,0,92);\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal{\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 988, 2012))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.frame.setMinimumSize(QtCore.QSize(100, 2000))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.frame.setFont(font)
        self.frame.setStyleSheet("    border: none")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(parent=self.frame)
        self.label_3.setGeometry(QtCore.QRect(0, 10, 981, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: transparent;\n"
"    border: none")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.frame)
        self.label_4.setGeometry(QtCore.QRect(530, 930, 411, 231))
        self.label_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.label_4.setText("")
        self.label_4.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_4.setPixmap(QtGui.QPixmap("E:\\Personal Projects\\___Pycharm___\\FN5\\ui\\../images/discount1.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.frame)
        self.label_5.setGeometry(QtCore.QRect(30, 670, 411, 231))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("E:\\Personal Projects\\___Pycharm___\\FN5\\ui\\../images/discount2.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.frame)
        self.label_6.setGeometry(QtCore.QRect(530, 410, 411, 221))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("E:\\Personal Projects\\___Pycharm___\\FN5\\ui\\../images/discount4.jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.pushButtonGetTK1 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButtonGetTK1.setGeometry(QtCore.QRect(630, 290, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButtonGetTK1.setFont(font)
        self.pushButtonGetTK1.setStyleSheet("background-color: rgb(229, 0, 28); /* Red background */\n"
"    color: white; /* White text */\n"
"    border-radius: 20px; /* Rounded corners */\n"
"    padding: 10px 20px; /* Padding */\n"
"    border: none; /* No border */\n"
"    font-size: 14px;\n"
"    cursor: pointer; /* Change cursor to pointer */\n"
" background-color: rgb(200, 0, 25); /* Slightly darker red on hover */")
        self.pushButtonGetTK1.setObjectName("pushButtonGetTK1")
        self.pushButtonPlanYourVisit = QtWidgets.QPushButton(parent=self.frame)
        self.pushButtonPlanYourVisit.setGeometry(QtCore.QRect(600, 820, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonPlanYourVisit.setFont(font)
        self.pushButtonPlanYourVisit.setStyleSheet(" background-color: transparent; /* Transparent background */\n"
"    color: white;                  /* White text */\n"
"    border: 2px solid white;       /* White border */\n"
"    border-radius: 20px;           /* Rounded corners */\n"
"    padding: 10px 20px;            /* Padding inside the button */\n"
"    font-size: 12px;               /* Font size */\n"
"    font-weight: bold; \n"
"  background-color: rgba(0, 0, 0,0.1);")
        self.pushButtonPlanYourVisit.setObjectName("pushButtonPlanYourVisit")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(30, 160, 411, 221))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("E:\\Personal Projects\\___Pycharm___\\FN5\\ui\\../images/discount3.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setGeometry(QtCore.QRect(-90, 0, 1161, 141))
        self.label_2.setStyleSheet("\n"
"background-color: rgb(123, 0, 0);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_12 = QtWidgets.QLabel(parent=self.frame)
        self.label_12.setGeometry(QtCore.QRect(120, 60, 741, 31))
        self.label_12.setStyleSheet("background-color: transparent;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"    border: none")
        self.label_12.setObjectName("label_12")
        self.label_11 = QtWidgets.QLabel(parent=self.frame)
        self.label_11.setGeometry(QtCore.QRect(530, 220, 341, 20))
        self.label_11.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_11.setObjectName("label_11")
        self.label_13 = QtWidgets.QLabel(parent=self.frame)
        self.label_13.setGeometry(QtCore.QRect(540, 240, 301, 20))
        self.label_13.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_13.setObjectName("label_13")
        self.label_10 = QtWidgets.QLabel(parent=self.frame)
        self.label_10.setGeometry(QtCore.QRect(570, 160, 251, 61))
        self.label_10.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.label_14 = QtWidgets.QLabel(parent=self.frame)
        self.label_14.setGeometry(QtCore.QRect(120, 420, 251, 61))
        self.label_14.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_14.setObjectName("label_14")
        self.label_16 = QtWidgets.QLabel(parent=self.frame)
        self.label_16.setGeometry(QtCore.QRect(50, 480, 401, 20))
        self.label_16.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(parent=self.frame)
        self.label_17.setGeometry(QtCore.QRect(600, 690, 251, 61))
        self.label_17.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(parent=self.frame)
        self.label_18.setGeometry(QtCore.QRect(530, 750, 391, 21))
        self.label_18.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(parent=self.frame)
        self.label_19.setGeometry(QtCore.QRect(160, 970, 171, 61))
        self.label_19.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(parent=self.frame)
        self.label_20.setGeometry(QtCore.QRect(40, 1030, 451, 20))
        self.label_20.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_20.setObjectName("label_20")
        self.label_7 = QtWidgets.QLabel(parent=self.frame)
        self.label_7.setGeometry(QtCore.QRect(0, 1190, 981, 61))
        self.label_7.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.line_2 = QtWidgets.QFrame(parent=self.frame)
        self.line_2.setGeometry(QtCore.QRect(580, 1510, 118, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_15 = QtWidgets.QLabel(parent=self.frame)
        self.label_15.setGeometry(QtCore.QRect(160, 90, 841, 31))
        self.label_15.setStyleSheet("background-color: transparent;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"    border: none")
        self.label_15.setObjectName("label_15")
        self.pushButtonSeeShowtimes = QtWidgets.QPushButton(parent=self.frame)
        self.pushButtonSeeShowtimes.setGeometry(QtCore.QRect(140, 1100, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSeeShowtimes.setFont(font)
        self.pushButtonSeeShowtimes.setStyleSheet(" background-color: transparent; /* Transparent background */\n"
"    color: white;                  /* White text */\n"
"    border: 2px solid white;       /* White border */\n"
"    border-radius: 20px;           /* Rounded corners */\n"
"    padding: 10px 20px;            /* Padding inside the button */\n"
"    font-size: 12px;               /* Font size */\n"
"    font-weight: bold; \n"
"  background-color: rgba(0, 0, 0,0.1);")
        self.pushButtonSeeShowtimes.setObjectName("pushButtonSeeShowtimes")
        self.label_8 = QtWidgets.QLabel(parent=self.frame)
        self.label_8.setGeometry(QtCore.QRect(630, 430, 121, 71))
        self.label_8.setStyleSheet("background-color: transparent;")
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("E:\\Personal Projects\\___Pycharm___\\FN5\\ui\\../images/logoreal.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_21 = QtWidgets.QLabel(parent=self.frame)
        self.label_21.setGeometry(QtCore.QRect(50, 520, 401, 20))
        self.label_21.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_21.setObjectName("label_21")
        self.label_24 = QtWidgets.QLabel(parent=self.frame)
        self.label_24.setGeometry(QtCore.QRect(50, 500, 411, 20))
        self.label_24.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_24.setObjectName("label_24")
        self.pushButtonGetTK2 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButtonGetTK2.setGeometry(QtCore.QRect(180, 570, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButtonGetTK2.setFont(font)
        self.pushButtonGetTK2.setStyleSheet("background-color: rgb(229, 0, 28); /* Red background */\n"
"    color: white; /* White text */\n"
"    border-radius: 20px; /* Rounded corners */\n"
"    padding: 10px 20px; /* Padding */\n"
"    border: none; /* No border */\n"
"    font-size: 14px;\n"
"    cursor: pointer; /* Change cursor to pointer */\n"
" background-color: rgb(200, 0, 25); /* Slightly darker red on hover */")
        self.pushButtonGetTK2.setObjectName("pushButtonGetTK2")
        self.label_22 = QtWidgets.QLabel(parent=self.frame)
        self.label_22.setGeometry(QtCore.QRect(540, 770, 371, 21))
        self.label_22.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_22.setObjectName("label_22")
        self.label_9 = QtWidgets.QLabel(parent=self.frame)
        self.label_9.setGeometry(QtCore.QRect(670, 440, 31, 31))
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_23 = QtWidgets.QLabel(parent=self.frame)
        self.label_23.setGeometry(QtCore.QRect(40, 1050, 451, 20))
        self.label_23.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_23.setObjectName("label_23")
        self.label_25 = QtWidgets.QLabel(parent=self.frame)
        self.label_25.setGeometry(QtCore.QRect(-100, 1270, 1161, 421))
        self.label_25.setStyleSheet("\n"
"background-color: rgb(123, 0, 0);")
        self.label_25.setText("")
        self.label_25.setPixmap(QtGui.QPixmap("E:\\Personal Projects\\___Pycharm___\\FN5\\ui\\../images/AboutUs7.jpg"))
        self.label_25.setScaledContents(True)
        self.label_25.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.pushButtonSeeMorePromotions = QtWidgets.QPushButton(parent=self.frame)
        self.pushButtonSeeMorePromotions.setGeometry(QtCore.QRect(-20, 1200, 1001, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSeeMorePromotions.setFont(font)
        self.pushButtonSeeMorePromotions.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"   ")
        self.pushButtonSeeMorePromotions.setText("")
        self.pushButtonSeeMorePromotions.setObjectName("pushButtonSeeMorePromotions")
        self.label_44 = QtWidgets.QLabel(parent=self.frame)
        self.label_44.setGeometry(QtCore.QRect(0, 1740, 981, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_44.setFont(font)
        self.label_44.setStyleSheet("background-color: transparent;\n"
"    border: none")
        self.label_44.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_44.setObjectName("label_44")
        self.pushButtonfb = QtWidgets.QPushButton(parent=self.frame)
        self.pushButtonfb.setGeometry(QtCore.QRect(430, 1810, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonfb.setFont(font)
        self.pushButtonfb.setStyleSheet("background-color:  rgb(255, 255, 255);\n"
"color:rgb(0, 0, 0);\n"
"    border-radius: 10px;\n"
"    padding: 5px")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("E:\\Personal Projects\\___Pycharm___\\FN5\\ui\\../../images/fb.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonfb.setIcon(icon1)
        self.pushButtonfb.setIconSize(QtCore.QSize(30, 30))
        self.pushButtonfb.setAutoRepeatDelay(305)
        self.pushButtonfb.setObjectName("pushButtonfb")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(420, 1820, 141, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: transparent;\n"
"\n"
"    border: none")
        self.pushButton_4.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("E:\\Personal Projects\\___Pycharm___\\FN5\\ui\\../../images/logoreal.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_42 = QtWidgets.QLabel(parent=self.frame)
        self.label_42.setGeometry(QtCore.QRect(0, 1850, 981, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_42.setFont(font)
        self.label_42.setStyleSheet("background-color: transparent;\n"
"    border: none")
        self.label_42.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(parent=self.frame)
        self.label_43.setGeometry(QtCore.QRect(-10, 1890, 1001, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_43.setFont(font)
        self.label_43.setStyleSheet("background-color: transparent;\n"
"    border: none")
        self.label_43.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_43.setObjectName("label_43")
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.pushButtonGetTK1.raise_()
        self.pushButtonPlanYourVisit.raise_()
        self.label.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_14.raise_()
        self.label_16.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.label_7.raise_()
        self.line_2.raise_()
        self.label_15.raise_()
        self.pushButtonSeeShowtimes.raise_()
        self.label_21.raise_()
        self.label_24.raise_()
        self.pushButtonGetTK2.raise_()
        self.label_22.raise_()
        self.label_9.raise_()
        self.label_8.raise_()
        self.label_23.raise_()
        self.label_25.raise_()
        self.pushButtonSeeMorePromotions.raise_()
        self.label_44.raise_()
        self.pushButtonfb.raise_()
        self.pushButton_4.raise_()
        self.label_42.raise_()
        self.label_43.raise_()
        self.verticalLayout.addWidget(self.frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 60, 1001, 1))
        self.line.setMaximumSize(QtCore.QSize(16777215, 1))
        self.line.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.pushButtonTicket_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonTicket_2.setGeometry(QtCore.QRect(730, 10, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButtonTicket_2.setFont(font)
        self.pushButtonTicket_2.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"    border-radius: 10px;\n"
"    padding: 5px")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("E:\\Personal Projects\\___Pycharm___\\FN5\\ui\\../images/ic_ticket.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonTicket_2.setIcon(icon3)
        self.pushButtonTicket_2.setIconSize(QtCore.QSize(30, 30))
        self.pushButtonTicket_2.setObjectName("pushButtonTicket_2")
        self.pushButtonBuyPop = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonBuyPop.setGeometry(QtCore.QRect(870, 10, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButtonBuyPop.setFont(font)
        self.pushButtonBuyPop.setStyleSheet("background-color: rgb(111, 56, 193);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"    border-radius: 10px;\n"
"    padding: 5px")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("E:\\Personal Projects\\___Pycharm___\\FN5\\ui\\../images/ic_popcorn.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonBuyPop.setIcon(icon4)
        self.pushButtonBuyPop.setIconSize(QtCore.QSize(30, 30))
        self.pushButtonBuyPop.setAutoRepeatDelay(305)
        self.pushButtonBuyPop.setObjectName("pushButtonBuyPop")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 0, 141, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: transparent;\n"
"\n"
"    border: none")
        self.pushButton_5.setText("")
        self.pushButton_5.setIcon(icon2)
        self.pushButton_5.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1009, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Discounts"))
        self.pushButtonDiscounts.setText(_translate("MainWindow", "Discounts"))
        self.pushButtonAboutUs.setText(_translate("MainWindow", "About Us"))
        self.label_3.setText(_translate("MainWindow", "Amazing Ticket Savings"))
        self.pushButtonGetTK1.setText(_translate("MainWindow", "Get Tickets"))
        self.pushButtonPlanYourVisit.setText(_translate("MainWindow", "Plan Your Visit"))
        self.label_12.setText(_translate("MainWindow", "Take advantage of amazing savings at participating GFLIX, GFLIX-DINE-IN™, and GFLIX CLASSIC™ theaters. Discover               more                       about our discounted movie tickets for matinee showtimes, Discount Tuesdays, and much more!"))
        self.label_11.setText(_translate("MainWindow", "Every day before 4pm, movie tickets are 25% off the evening ticket prices "))
        self.label_13.setText(_translate("MainWindow", "GFLIX  theatre. It’s always perfect day to see a movie and save!"))
        self.label_10.setText(_translate("MainWindow", "Enjoy Discount Matinees Any Day"))
        self.label_14.setText(_translate("MainWindow", "Tuesdays Are for Ticket Savings"))
        self.label_16.setText(_translate("MainWindow", "Tuesdays Mean Big Savings at GFLIX: GFLIX Stubs A-List™, Premiere, and Insider members enjoy discounted tickets to the latest big-screen movies every Tuesday, all year round. Not a member yet? Sign up for free as an Insider today and start saving on Tuesdays and more!"))
        self.label_17.setText(_translate("MainWindow", "Students Always Save at GFLIX"))
        self.label_18.setText(_translate("MainWindow", "Enjoy special student pricing every day at GFLIX Theaters! Just bring your student ID to the box office and get great discounts on tickets for the latest movies!"))
        self.label_19.setText(_translate("MainWindow", "Seniors Save on Tickets"))
        self.label_20.setText(_translate("MainWindow", "At GFLIX, we strive to bring you the movies you love at prices you\'ll enjoy. Guests aged 60+ can save on tickets all day, every day. Simply choose senior pricing when checking out online."))
        self.label_7.setText(_translate("MainWindow", "See More Offers & Promotions"))
        self.label_15.setText(_translate("MainWindow", " more about our discounted movie tickets for matinee showtimes, Discount Tuesdays, and much more!"))
        self.pushButtonSeeShowtimes.setText(_translate("MainWindow", "See Showtimes"))
        self.label_21.setText(_translate("MainWindow", " member yet? Sign up for free as an Insider today and start saving on Tuesdays and more!"))
        self.label_24.setText(_translate("MainWindow", "enjoy discounted tickets to the latest big-screen movies every Tuesday, all year round. Not a member yet? Sign up for free as an Insider today and start saving on Tuesdays and more!"))
        self.pushButtonGetTK2.setText(_translate("MainWindow", "Get Tickets"))
        self.label_22.setText(_translate("MainWindow", " the box office and get great discounts on tickets for the latest movies!"))
        self.label_23.setText(_translate("MainWindow", "on tickets all day, every day. Simply choose senior pricing when checking out online."))
        self.label_44.setText(_translate("MainWindow", "CONTACT US"))
        self.pushButtonfb.setText(_translate("MainWindow", "Facebook"))
        self.label_42.setText(_translate("MainWindow", "WE MAKE MOVIES BETTER"))
        self.label_43.setText(_translate("MainWindow", "© Copyright 2025 GFlix Theatres"))
        self.pushButtonTicket_2.setText(_translate("MainWindow", "BUY TICKETS"))
        self.pushButtonBuyPop.setText(_translate("MainWindow", "BUY POPCORN"))

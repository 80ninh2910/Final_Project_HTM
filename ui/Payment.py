# Form implementation generated from reading ui file 'E:\Personal Projects\___Pycharm___\FN6\ui\Payment.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1017, 717)
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
        self.pushButtonShwtm = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonShwtm.setGeometry(QtCore.QRect(20, 70, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonShwtm.setFont(font)
        self.pushButtonShwtm.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"    border: none")
        self.pushButtonShwtm.setObjectName("pushButtonShwtm")
        self.pushButtonDiscounts = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonDiscounts.setGeometry(QtCore.QRect(820, 70, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonDiscounts.setFont(font)
        self.pushButtonDiscounts.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"    border: none")
        self.pushButtonDiscounts.setObjectName("pushButtonDiscounts")
        self.pushButtonAboutUs = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonAboutUs.setGeometry(QtCore.QRect(910, 70, 81, 31))
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
        self.scrollArea.setGeometry(QtCore.QRect(0, 100, 1001, 561))
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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -484, 988, 1312))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.frame.setMinimumSize(QtCore.QSize(100, 1300))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.frame.setFont(font)
        self.frame.setMouseTracking(False)
        self.frame.setTabletTracking(False)
        self.frame.setAcceptDrops(True)
        self.frame.setStyleSheet("    border: none")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label_29 = QtWidgets.QLabel(parent=self.frame)
        self.label_29.setGeometry(QtCore.QRect(-10, 0, 991, 251))
        self.label_29.setText("")
        self.label_29.setPixmap(QtGui.QPixmap("E:\\Personal Projects\\___Pycharm___\\FN6\\ui\\../images/Red And Yellow Illustrated Movie Night Perfomance Invitation Outdor Banner.png"))
        self.label_29.setScaledContents(True)
        self.label_29.setObjectName("label_29")
        self.pushButtonDiscounts_4 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButtonDiscounts_4.setGeometry(QtCore.QRect(10, 290, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonDiscounts_4.setFont(font)
        self.pushButtonDiscounts_4.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"    border: none")
        self.pushButtonDiscounts_4.setText("")
        self.pushButtonDiscounts_4.setObjectName("pushButtonDiscounts_4")
        self.label_3 = QtWidgets.QLabel(parent=self.frame)
        self.label_3.setGeometry(QtCore.QRect(270, 250, 301, 71))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(40)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color:transparent")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.frame)
        self.label_4.setGeometry(QtCore.QRect(350, 300, 301, 71))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color:transparent;\n"
"color: rgb(75, 60, 41);")
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(-30, 240, 959, 361))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("E:\\Personal Projects\\___Pycharm___\\FN6\\ui\\../images/Blue Modern Cinema Ticket.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(parent=self.frame)
        self.label_5.setGeometry(QtCore.QRect(10, 350, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color:transparent;\n"
"color: rgb(75, 60, 41);")
        self.label_5.setObjectName("label_5")
        self.labelUsername = QtWidgets.QLabel(parent=self.frame)
        self.labelUsername.setGeometry(QtCore.QRect(10, 390, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.labelUsername.setFont(font)
        self.labelUsername.setStyleSheet("background-color:transparent;\n"
"color: rgb(75, 60, 41);")
        self.labelUsername.setText("")
        self.labelUsername.setObjectName("labelUsername")
        self.label_7 = QtWidgets.QLabel(parent=self.frame)
        self.label_7.setGeometry(QtCore.QRect(10, 450, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color:transparent;\n"
"color: rgb(75, 60, 41);")
        self.label_7.setObjectName("label_7")
        self.labelMail = QtWidgets.QLabel(parent=self.frame)
        self.labelMail.setGeometry(QtCore.QRect(10, 500, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.labelMail.setFont(font)
        self.labelMail.setStyleSheet("background-color:transparent;\n"
"color: rgb(75, 60, 41);")
        self.labelMail.setText("")
        self.labelMail.setObjectName("labelMail")
        self.labelTheater = QtWidgets.QLabel(parent=self.frame)
        self.labelTheater.setGeometry(QtCore.QRect(370, 390, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.labelTheater.setFont(font)
        self.labelTheater.setStyleSheet("background-color:transparent;\n"
"color: rgb(75, 60, 41);")
        self.labelTheater.setText("")
        self.labelTheater.setObjectName("labelTheater")
        self.label_10 = QtWidgets.QLabel(parent=self.frame)
        self.label_10.setGeometry(QtCore.QRect(280, 390, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color:transparent;\n"
"color: rgb(75, 60, 41);")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(parent=self.frame)
        self.label_11.setGeometry(QtCore.QRect(280, 430, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color:transparent;\n"
"color: rgb(75, 60, 41);")
        self.label_11.setObjectName("label_11")
        self.labelTime = QtWidgets.QLabel(parent=self.frame)
        self.labelTime.setGeometry(QtCore.QRect(370, 430, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.labelTime.setFont(font)
        self.labelTime.setStyleSheet("background-color:transparent;\n"
"color: rgb(75, 60, 41);")
        self.labelTime.setText("")
        self.labelTime.setObjectName("labelTime")
        self.label_13 = QtWidgets.QLabel(parent=self.frame)
        self.label_13.setGeometry(QtCore.QRect(280, 470, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color:transparent;\n"
"color: rgb(75, 60, 41);")
        self.label_13.setObjectName("label_13")
        self.labelSeat = QtWidgets.QLabel(parent=self.frame)
        self.labelSeat.setGeometry(QtCore.QRect(370, 470, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.labelSeat.setFont(font)
        self.labelSeat.setStyleSheet("background-color:transparent;\n"
"color: rgb(75, 60, 41);")
        self.labelSeat.setText("")
        self.labelSeat.setObjectName("labelSeat")
        self.label_15 = QtWidgets.QLabel(parent=self.frame)
        self.label_15.setGeometry(QtCore.QRect(10, 260, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background-color:transparent;\n"
"font: 16pt \"Cooper Black\";\n"
"\n"
"\n"
"color: rgb(148, 0, 0);")
        self.label_15.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(60, 620, 501, 271))
        self.tableWidget.setStyleSheet("QTableWidget {\n"
"    background-color: #DCCBA4;  /* Nền be */\n"
"    color: #4A321E;  /* Chữ nâu đậm */\n"
"    border-radius: 12px; /* Bo góc mềm */\n"
"    padding: 5px;\n"
"    border: 1px solid #8B6F47; /* Viền nâu */\n"
"}\n"
"\n"
"/* Header của bảng */\n"
"QHeaderView::section {\n"
"    background-color: #C4AB80; /* Màu vàng nhạt */\n"
"    color: #4A321E;\n"
"    font-weight: bold;\n"
"    border-radius: ;\n"
"    padding: 6px;\n"
"    border: 1px solid #8B6F47;\n"
"}\n"
"\n"
"/* Các ô trong bảng */\n"
"QTableWidget::item {\n"
"    border-bottom: 1px solid #8B6F47;\n"
"    padding: 6px;\n"
"}\n"
"")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(94)
        self.pushButtonConfirm = QtWidgets.QPushButton(parent=self.frame)
        self.pushButtonConfirm.setGeometry(QtCore.QRect(660, 800, 211, 91))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonConfirm.setFont(font)
        self.pushButtonConfirm.setStyleSheet("background-color: rgb(173, 54, 68);\n"
"color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    padding: 5px")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("E:\\Personal Projects\\___Pycharm___\\FN6\\ui\\../images/ic_popcorn.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonConfirm.setIcon(icon)
        self.pushButtonConfirm.setIconSize(QtCore.QSize(30, 30))
        self.pushButtonConfirm.setAutoRepeatDelay(305)
        self.pushButtonConfirm.setObjectName("pushButtonConfirm")
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setGeometry(QtCore.QRect(-10, 900, 991, 151))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("E:\\Personal Projects\\___Pycharm___\\FN6\\ui\\../images/Screenshot 2025-03-17 023822.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.line_2 = QtWidgets.QFrame(parent=self.frame)
        self.line_2.setGeometry(QtCore.QRect(-20, 1030, 1001, 1))
        self.line_2.setMaximumSize(QtCore.QSize(16777215, 1))
        self.line_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_44 = QtWidgets.QLabel(parent=self.frame)
        self.label_44.setGeometry(QtCore.QRect(270, 1020, 381, 71))
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
        self.label_43 = QtWidgets.QLabel(parent=self.frame)
        self.label_43.setGeometry(QtCore.QRect(260, 1190, 411, 61))
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
        self.pushButtonfb = QtWidgets.QPushButton(parent=self.frame)
        self.pushButtonfb.setGeometry(QtCore.QRect(400, 1080, 121, 31))
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
        icon1.addPixmap(QtGui.QPixmap("E:\\Personal Projects\\___Pycharm___\\FN6\\ui\\../images/fb.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonfb.setIcon(icon1)
        self.pushButtonfb.setIconSize(QtCore.QSize(30, 30))
        self.pushButtonfb.setAutoRepeatDelay(305)
        self.pushButtonfb.setObjectName("pushButtonfb")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(390, 1120, 141, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: transparent;\n"
"\n"
"    border: none")
        self.pushButton_4.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("E:\\Personal Projects\\___Pycharm___\\FN6\\ui\\../images/logoreal.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_42 = QtWidgets.QLabel(parent=self.frame)
        self.label_42.setGeometry(QtCore.QRect(250, 1160, 441, 61))
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
        self.label_16 = QtWidgets.QLabel(parent=self.frame)
        self.label_16.setGeometry(QtCore.QRect(300, 60, 441, 71))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("background-color:transparent;\n"
"color: rgb(148, 0, 0);")
        self.label_16.setObjectName("label_16")
        self.label_6 = QtWidgets.QLabel(parent=self.frame)
        self.label_6.setGeometry(QtCore.QRect(340, 120, 361, 71))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(40)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color:transparent")
        self.label_6.setObjectName("label_6")
        self.lineEditShowPoint = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEditShowPoint.setGeometry(QtCore.QRect(630, 640, 291, 41))
        self.lineEditShowPoint.setStyleSheet("\n"
"background-color: #DCCBA4;\n"
"color: rgb(0, 0, 0);\n"
"    border-radius: 10px;\n"
"    padding: 5px")
        self.lineEditShowPoint.setText("")
        self.lineEditShowPoint.setObjectName("lineEditShowPoint")
        self.lineEditFinalPayment = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEditFinalPayment.setGeometry(QtCore.QRect(630, 730, 291, 41))
        self.lineEditFinalPayment.setStyleSheet("\n"
"background-color: #DCCBA4;\n"
"color: rgb(0, 0, 0);\n"
"    border-radius: 10px;\n"
"    padding: 5px")
        self.lineEditFinalPayment.setText("")
        self.lineEditFinalPayment.setObjectName("lineEditFinalPayment")
        self.label_14 = QtWidgets.QLabel(parent=self.frame)
        self.label_14.setGeometry(QtCore.QRect(280, 510, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color:transparent;\n"
"color: rgb(75, 60, 41);")
        self.label_14.setObjectName("label_14")
        self.labelTicket = QtWidgets.QLabel(parent=self.frame)
        self.labelTicket.setGeometry(QtCore.QRect(370, 510, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.labelTicket.setFont(font)
        self.labelTicket.setStyleSheet("background-color:transparent;\n"
"color: rgb(75, 60, 41);")
        self.labelTicket.setText("")
        self.labelTicket.setObjectName("labelTicket")
        self.label_2.raise_()
        self.label.raise_()
        self.label_29.raise_()
        self.pushButtonDiscounts_4.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.labelUsername.raise_()
        self.label_7.raise_()
        self.labelMail.raise_()
        self.labelTheater.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.labelTime.raise_()
        self.label_13.raise_()
        self.labelSeat.raise_()
        self.label_15.raise_()
        self.tableWidget.raise_()
        self.pushButtonConfirm.raise_()
        self.line_2.raise_()
        self.label_44.raise_()
        self.label_43.raise_()
        self.pushButtonfb.raise_()
        self.pushButton_4.raise_()
        self.label_42.raise_()
        self.label_16.raise_()
        self.label_6.raise_()
        self.lineEditShowPoint.raise_()
        self.lineEditFinalPayment.raise_()
        self.label_14.raise_()
        self.labelTicket.raise_()
        self.verticalLayout.addWidget(self.frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 60, 1001, 1))
        self.line.setMaximumSize(QtCore.QSize(16777215, 1))
        self.line.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.pushButtonHome = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonHome.setGeometry(QtCore.QRect(20, 10, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonHome.setFont(font)
        self.pushButtonHome.setStyleSheet("background-color: rgb(173, 54, 68);\n"
"color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    padding: 5px")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("E:\\Personal Projects\\___Pycharm___\\FN6\\ui\\../images/home.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonHome.setIcon(icon3)
        self.pushButtonHome.setIconSize(QtCore.QSize(30, 30))
        self.pushButtonHome.setAutoRepeat(False)
        self.pushButtonHome.setAutoExclusive(False)
        self.pushButtonHome.setAutoRepeatDelay(250)
        self.pushButtonHome.setAutoRepeatInterval(250)
        self.pushButtonHome.setObjectName("pushButtonHome")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1017, 18))
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
        self.pushButtonShwtm.setText(_translate("MainWindow", "Showtimes"))
        self.pushButtonDiscounts.setText(_translate("MainWindow", "Discounts"))
        self.pushButtonAboutUs.setText(_translate("MainWindow", "About Us"))
        self.label_3.setText(_translate("MainWindow", "CINEMA"))
        self.label_4.setText(_translate("MainWindow", "TICKET"))
        self.label_5.setText(_translate("MainWindow", "Username:"))
        self.label_7.setText(_translate("MainWindow", "Mail:"))
        self.label_10.setText(_translate("MainWindow", "Theater:"))
        self.label_11.setText(_translate("MainWindow", "Time:"))
        self.label_13.setText(_translate("MainWindow", "Seat:"))
        self.label_15.setText(_translate("MainWindow", "CUSTOMER"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Quantity"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Price"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Total"))
        self.pushButtonConfirm.setText(_translate("MainWindow", "Confirm"))
        self.label_44.setText(_translate("MainWindow", "CONTACT US"))
        self.label_43.setText(_translate("MainWindow", "© Copyright 2025 GFlix Theatres"))
        self.pushButtonfb.setText(_translate("MainWindow", "Facebook"))
        self.label_42.setText(_translate("MainWindow", "WE MAKE MOVIES BETTER"))
        self.label_16.setText(_translate("MainWindow", "CHECK OUT"))
        self.label_6.setText(_translate("MainWindow", "PAYMENT"))
        self.label_14.setText(_translate("MainWindow", "Ticket:"))
        self.pushButtonHome.setText(_translate("MainWindow", "HOME"))

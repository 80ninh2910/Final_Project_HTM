# Form implementation generated from reading ui file 'E:\Personal Projects\___Pycharm___\FN1\ui\NGT.ui'
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
        MainWindow.resize(1010, 599)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color:  rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"    border: none")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonDiscounts = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonDiscounts.setGeometry(QtCore.QRect(730, 70, 111, 31))
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
        self.pushButtonAboutUs.setGeometry(QtCore.QRect(880, 70, 111, 31))
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
        self.scrollArea.setGeometry(QtCore.QRect(0, 100, 1001, 471))
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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -906, 988, 1812))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.frame.setMinimumSize(QtCore.QSize(100, 1800))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.frame.setFont(font)
        self.frame.setStyleSheet("    border: none")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label_4 = QtWidgets.QLabel(parent=self.frame)
        self.label_4.setGeometry(QtCore.QRect(20, -10, 381, 531))
        self.label_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.label_4.setText("")
        self.label_4.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_4.setPixmap(QtGui.QPixmap("E:\\Personal Projects\\___Pycharm___\\FN1\\ui\\../images/nha-gia-tien-sneak.webp"))
        self.label_4.setScaledContents(True)
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName("label_4")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(400, 1520, 141, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: transparent;\n"
"\n"
"    border: none")
        self.pushButton_4.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("E:\\Personal Projects\\___Pycharm___\\FN1\\ui\\../images/logoreal.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_42 = QtWidgets.QLabel(parent=self.frame)
        self.label_42.setGeometry(QtCore.QRect(260, 1560, 441, 61))
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
        self.label_43.setGeometry(QtCore.QRect(270, 1590, 411, 61))
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
        self.label_44 = QtWidgets.QLabel(parent=self.frame)
        self.label_44.setGeometry(QtCore.QRect(280, 1420, 381, 71))
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
        self.line_2 = QtWidgets.QFrame(parent=self.frame)
        self.line_2.setGeometry(QtCore.QRect(-10, 1430, 1001, 1))
        self.line_2.setMaximumSize(QtCore.QSize(16777215, 1))
        self.line_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.pushButtonfb = QtWidgets.QPushButton(parent=self.frame)
        self.pushButtonfb.setGeometry(QtCore.QRect(410, 1480, 121, 31))
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
        icon1.addPixmap(QtGui.QPixmap("E:\\Personal Projects\\___Pycharm___\\FN1\\ui\\../images/fb.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonfb.setIcon(icon1)
        self.pushButtonfb.setIconSize(QtCore.QSize(30, 30))
        self.pushButtonfb.setAutoRepeatDelay(305)
        self.pushButtonfb.setObjectName("pushButtonfb")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(540, 10, 301, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setGeometry(QtCore.QRect(450, 80, 61, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.frame)
        self.label_3.setGeometry(QtCore.QRect(450, 140, 91, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.groupBox = QtWidgets.QGroupBox(parent=self.frame)
        self.groupBox.setGeometry(QtCore.QRect(440, 220, 501, 321))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(15)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.scrollArea_2 = QtWidgets.QScrollArea(parent=self.groupBox)
        self.scrollArea_2.setGeometry(QtCore.QRect(30, 50, 401, 151))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 401, 151))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelDes = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_2)
        self.labelDes.setText("")
        self.labelDes.setWordWrap(True)
        self.labelDes.setObjectName("labelDes")
        self.verticalLayout_2.addWidget(self.labelDes)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.label_6 = QtWidgets.QLabel(parent=self.frame)
        self.label_6.setGeometry(QtCore.QRect(210, 550, 551, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(30)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.widgetuel = QtWidgets.QWidget(parent=self.frame)
        self.widgetuel.setGeometry(QtCore.QRect(220, 680, 551, 151))
        self.widgetuel.setStyleSheet("background-color: rgb(96, 0, 144);")
        self.widgetuel.setObjectName("widgetuel")
        self.label_7 = QtWidgets.QLabel(parent=self.widgetuel)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(219, 219, 0);")
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.widgetuel)
        self.label_8.setGeometry(QtCore.QRect(10, 40, 381, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=self.widgetuel)
        self.label_9.setGeometry(QtCore.QRect(10, 70, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.pushButtonUel_12 = QtWidgets.QPushButton(parent=self.widgetuel)
        self.pushButtonUel_12.setGeometry(QtCore.QRect(130, 100, 81, 31))
        self.pushButtonUel_12.setStyleSheet("QPushButton {\n"
"    border: 2px solid white;\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    color: yellow;  /* Đổi chữ thành màu vàng khi nhấn */\n"
"}\n"
"")
        self.pushButtonUel_12.setObjectName("pushButtonUel_12")
        self.pushButtonUel_9 = QtWidgets.QPushButton(parent=self.widgetuel)
        self.pushButtonUel_9.setGeometry(QtCore.QRect(20, 100, 81, 31))
        self.pushButtonUel_9.setStyleSheet("QPushButton {\n"
"    border: 2px solid white;\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    color: yellow;  /* Đổi chữ thành màu vàng khi nhấn */\n"
"}\n"
"")
        self.pushButtonUel_9.setObjectName("pushButtonUel_9")
        self.pushButtonUel_19 = QtWidgets.QPushButton(parent=self.widgetuel)
        self.pushButtonUel_19.setGeometry(QtCore.QRect(350, 100, 81, 31))
        self.pushButtonUel_19.setStyleSheet("QPushButton {\n"
"    border: 2px solid white;\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    color: yellow;  /* Đổi chữ thành màu vàng khi nhấn */\n"
"}\n"
"")
        self.pushButtonUel_19.setObjectName("pushButtonUel_19")
        self.pushButtonUel_14 = QtWidgets.QPushButton(parent=self.widgetuel)
        self.pushButtonUel_14.setGeometry(QtCore.QRect(240, 100, 81, 31))
        self.pushButtonUel_14.setStyleSheet("QPushButton {\n"
"    border: 2px solid white;\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    color: yellow;  /* Đổi chữ thành màu vàng khi nhấn */\n"
"}\n"
"")
        self.pushButtonUel_14.setObjectName("pushButtonUel_14")
        self.pushButtonUel_23 = QtWidgets.QPushButton(parent=self.widgetuel)
        self.pushButtonUel_23.setGeometry(QtCore.QRect(460, 100, 81, 31))
        self.pushButtonUel_23.setStyleSheet("QPushButton {\n"
"    border: 2px solid white;\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    color: yellow;  /* Đổi chữ thành màu vàng khi nhấn */\n"
"}\n"
"")
        self.pushButtonUel_23.setObjectName("pushButtonUel_23")
        self.widgethcm = QtWidgets.QWidget(parent=self.frame)
        self.widgethcm.setGeometry(QtCore.QRect(220, 850, 551, 151))
        self.widgethcm.setStyleSheet("background-color: rgb(96, 0, 144);")
        self.widgethcm.setObjectName("widgethcm")
        self.label_10 = QtWidgets.QLabel(parent=self.widgethcm)
        self.label_10.setGeometry(QtCore.QRect(10, 10, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(20)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(219, 219, 0);")
        self.label_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(parent=self.widgethcm)
        self.label_11.setGeometry(QtCore.QRect(10, 40, 381, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(parent=self.widgethcm)
        self.label_12.setGeometry(QtCore.QRect(10, 70, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.pushButtonhcm_12 = QtWidgets.QPushButton(parent=self.widgethcm)
        self.pushButtonhcm_12.setGeometry(QtCore.QRect(130, 100, 81, 31))
        self.pushButtonhcm_12.setStyleSheet("QPushButton {\n"
"    border: 2px solid white;\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    color: yellow;  /* Đổi chữ thành màu vàng khi nhấn */\n"
"}\n"
"")
        self.pushButtonhcm_12.setObjectName("pushButtonhcm_12")
        self.pushButtonhcm_9 = QtWidgets.QPushButton(parent=self.widgethcm)
        self.pushButtonhcm_9.setGeometry(QtCore.QRect(20, 100, 81, 31))
        self.pushButtonhcm_9.setStyleSheet("QPushButton {\n"
"    border: 2px solid white;\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    color: yellow;  /* Đổi chữ thành màu vàng khi nhấn */\n"
"}\n"
"")
        self.pushButtonhcm_9.setObjectName("pushButtonhcm_9")
        self.pushButtonhcm_19 = QtWidgets.QPushButton(parent=self.widgethcm)
        self.pushButtonhcm_19.setGeometry(QtCore.QRect(350, 100, 81, 31))
        self.pushButtonhcm_19.setStyleSheet("QPushButton {\n"
"    border: 2px solid white;\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    color: yellow;  /* Đổi chữ thành màu vàng khi nhấn */\n"
"}\n"
"")
        self.pushButtonhcm_19.setObjectName("pushButtonhcm_19")
        self.pushButtonhcm_14 = QtWidgets.QPushButton(parent=self.widgethcm)
        self.pushButtonhcm_14.setGeometry(QtCore.QRect(240, 100, 81, 31))
        self.pushButtonhcm_14.setStyleSheet("QPushButton {\n"
"    border: 2px solid white;\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    color: yellow;  /* Đổi chữ thành màu vàng khi nhấn */\n"
"}\n"
"")
        self.pushButtonhcm_14.setObjectName("pushButtonhcm_14")
        self.pushButtonhcm_23 = QtWidgets.QPushButton(parent=self.widgethcm)
        self.pushButtonhcm_23.setGeometry(QtCore.QRect(460, 100, 81, 31))
        self.pushButtonhcm_23.setStyleSheet("QPushButton {\n"
"    border: 2px solid white;\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    color: yellow;  /* Đổi chữ thành màu vàng khi nhấn */\n"
"}\n"
"")
        self.pushButtonhcm_23.setObjectName("pushButtonhcm_23")
        self.label_13 = QtWidgets.QLabel(parent=self.frame)
        self.label_13.setGeometry(QtCore.QRect(220, 1010, 551, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(30)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.widgetseat = QtWidgets.QWidget(parent=self.frame)
        self.widgetseat.setGeometry(QtCore.QRect(220, 1080, 561, 291))
        self.widgetseat.setObjectName("widgetseat")
        self.labelTotal = QtWidgets.QLabel(parent=self.widgetseat)
        self.labelTotal.setGeometry(QtCore.QRect(10, 10, 551, 51))
        self.labelTotal.setStyleSheet("background-color: rgb(105, 0, 157,150);")
        self.labelTotal.setText("")
        self.labelTotal.setObjectName("labelTotal")
        self.pushButtoncf = QtWidgets.QPushButton(parent=self.widgetseat)
        self.pushButtoncf.setGeometry(QtCore.QRect(440, 20, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtoncf.setFont(font)
        self.pushButtoncf.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"color: rgb(0, 0, 0);\n"
"    border-radius: 10px;\n"
"    padding: 5px")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("E:\\Personal Projects\\___Pycharm___\\FN1\\ui\\../images/ic_ticket.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtoncf.setIcon(icon2)
        self.pushButtoncf.setIconSize(QtCore.QSize(30, 30))
        self.pushButtoncf.setObjectName("pushButtoncf")
        self.label_14 = QtWidgets.QLabel(parent=self.widgetseat)
        self.label_14.setGeometry(QtCore.QRect(0, 80, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.lineEditUsn = QtWidgets.QLineEdit(parent=self.widgetseat)
        self.lineEditUsn.setGeometry(QtCore.QRect(60, 80, 211, 31))
        self.lineEditUsn.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"color: rgb(0, 0, 0);\n"
"    border-radius: 10px;\n"
"    padding: 5px")
        self.lineEditUsn.setObjectName("lineEditUsn")
        self.label_15 = QtWidgets.QLabel(parent=self.widgetseat)
        self.label_15.setGeometry(QtCore.QRect(290, 80, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.lineEditPhone = QtWidgets.QLineEdit(parent=self.widgetseat)
        self.lineEditPhone.setGeometry(QtCore.QRect(340, 80, 211, 31))
        self.lineEditPhone.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"color: rgb(0, 0, 0);\n"
"    border-radius: 10px;\n"
"    padding: 5px")
        self.lineEditPhone.setObjectName("lineEditPhone")
        self.labelType = QtWidgets.QLabel(parent=self.frame)
        self.labelType.setGeometry(QtCore.QRect(520, 100, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(15)
        self.labelType.setFont(font)
        self.labelType.setText("")
        self.labelType.setObjectName("labelType")
        self.labelDu = QtWidgets.QLabel(parent=self.frame)
        self.labelDu.setGeometry(QtCore.QRect(540, 160, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(15)
        self.labelDu.setFont(font)
        self.labelDu.setText("")
        self.labelDu.setObjectName("labelDu")
        self.comboBoxSelect2 = QtWidgets.QComboBox(parent=self.frame)
        self.comboBoxSelect2.setGeometry(QtCore.QRect(210, 640, 86, 16))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBoxSelect2.setFont(font)
        self.comboBoxSelect2.setStyleSheet("border:none\n"
"")
        self.comboBoxSelect2.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContents)
        self.comboBoxSelect2.setObjectName("comboBoxSelect2")
        self.comboBoxSelect2.addItem("")
        self.comboBoxSelect2.addItem("")
        self.comboBoxSelect2.addItem("")
        self.comboBoxSelect2.addItem("")
        self.comboBoxSelect2.addItem("")
        self.comboBoxSelect2.setItemText(4, "")
        self.comboBoxSelect2.addItem("")
        self.comboBoxSelect2.setItemText(5, "")
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
        icon3.addPixmap(QtGui.QPixmap("E:\\Personal Projects\\___Pycharm___\\FN1\\ui\\../images/home.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonHome.setIcon(icon3)
        self.pushButtonHome.setIconSize(QtCore.QSize(30, 30))
        self.pushButtonHome.setAutoRepeat(False)
        self.pushButtonHome.setAutoExclusive(False)
        self.pushButtonHome.setAutoRepeatDelay(250)
        self.pushButtonHome.setAutoRepeatInterval(250)
        self.pushButtonHome.setObjectName("pushButtonHome")
        self.comboBoxSelect1 = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBoxSelect1.setGeometry(QtCore.QRect(20, 75, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBoxSelect1.setFont(font)
        self.comboBoxSelect1.setStyleSheet("border:none\n"
"")
        self.comboBoxSelect1.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContents)
        self.comboBoxSelect1.setObjectName("comboBoxSelect1")
        self.comboBoxSelect1.addItem("")
        self.comboBoxSelect1.addItem("")
        self.comboBoxSelect1.addItem("")
        self.comboBoxSelect1.addItem("")
        self.comboBoxSelect1.addItem("")
        self.comboBoxSelect1.setItemText(4, "")
        self.comboBoxSelect1.addItem("")
        self.comboBoxSelect1.setItemText(5, "")
        self.pushButtonShowtime = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonShowtime.setGeometry(QtCore.QRect(160, 70, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonShowtime.setFont(font)
        self.pushButtonShowtime.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 0);\n"
"\n"
"    border: none")
        self.pushButtonShowtime.setObjectName("pushButtonShowtime")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1010, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Nhà Gia Tiên"))
        self.pushButtonDiscounts.setText(_translate("MainWindow", "Discounts"))
        self.pushButtonAboutUs.setText(_translate("MainWindow", "About Us"))
        self.label_42.setText(_translate("MainWindow", "WE MAKE MOVIES BETTER"))
        self.label_43.setText(_translate("MainWindow", "© Copyright 2025 GFlix Theatres"))
        self.label_44.setText(_translate("MainWindow", "CONTACT US"))
        self.pushButtonfb.setText(_translate("MainWindow", "Facebook"))
        self.label.setText(_translate("MainWindow", "Nhà Gia Tiên"))
        self.label_2.setText(_translate("MainWindow", "Type:"))
        self.label_3.setText(_translate("MainWindow", "Duration:"))
        self.groupBox.setTitle(_translate("MainWindow", "Description:"))
        self.label_6.setText(_translate("MainWindow", "SHOWTIMES"))
        self.label_7.setText(_translate("MainWindow", "Cinema GFlix UEL:"))
        self.label_8.setText(_translate("MainWindow", "Located at 669 QL1A, khu phố 6, Thủ Đức, Hồ Chí Minh"))
        self.label_9.setText(_translate("MainWindow", "Standard"))
        self.pushButtonUel_12.setText(_translate("MainWindow", "12:15"))
        self.pushButtonUel_9.setText(_translate("MainWindow", "9:00"))
        self.pushButtonUel_19.setText(_translate("MainWindow", "19:00"))
        self.pushButtonUel_14.setText(_translate("MainWindow", "14:20"))
        self.pushButtonUel_23.setText(_translate("MainWindow", "23:00"))
        self.label_10.setText(_translate("MainWindow", "Cinema GFlix HCM:"))
        self.label_11.setText(_translate("MainWindow", "Located at 19 Nguyễn Trãi, Phường Nguyễn Cư Trinh, Quận 1, Thành Phố Hồ Chí Minh"))
        self.label_12.setText(_translate("MainWindow", "Standard"))
        self.pushButtonhcm_12.setText(_translate("MainWindow", "12:15"))
        self.pushButtonhcm_9.setText(_translate("MainWindow", "9:00"))
        self.pushButtonhcm_19.setText(_translate("MainWindow", "19:00"))
        self.pushButtonhcm_14.setText(_translate("MainWindow", "14:20"))
        self.pushButtonhcm_23.setText(_translate("MainWindow", "23:00"))
        self.label_13.setText(_translate("MainWindow", "SELECT SEAT"))
        self.pushButtoncf.setText(_translate("MainWindow", "CONFIRM"))
        self.label_14.setText(_translate("MainWindow", "username:"))
        self.label_15.setText(_translate("MainWindow", "Email :"))
        self.comboBoxSelect2.setItemText(0, _translate("MainWindow", "SELECT THEATER   "))
        self.comboBoxSelect2.setItemText(1, _translate("MainWindow", "UEL"))
        self.comboBoxSelect2.setItemText(2, _translate("MainWindow", "HỒ CHÍ MINH"))
        self.comboBoxSelect2.setItemText(3, _translate("MainWindow", "Comming...soom"))
        self.pushButtonHome.setText(_translate("MainWindow", "HOME"))
        self.comboBoxSelect1.setItemText(0, _translate("MainWindow", "ALL THEATER"))
        self.comboBoxSelect1.setItemText(1, _translate("MainWindow", "UEL"))
        self.comboBoxSelect1.setItemText(2, _translate("MainWindow", "HỒ CHÍ MINH"))
        self.comboBoxSelect1.setItemText(3, _translate("MainWindow", "Comming...soom"))
        self.pushButtonShowtime.setText(_translate("MainWindow", "Showtimes"))

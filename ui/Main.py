# Form implementation generated from reading ui file 'E:\Personal Projects\___Pycharm___\FN5\ui\Main.ui'
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
        MainWindow.resize(1003, 600)
        font = QtGui.QFont()
        font.setPointSize(10)
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
        self.pushButtonShwtm = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonShwtm.setGeometry(QtCore.QRect(160, 60, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonShwtm.setFont(font)
        self.pushButtonShwtm.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 0);\n"
"    border: none")
        self.pushButtonShwtm.setObjectName("pushButtonShwtm")
        self.pushButtonDiscounts = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonDiscounts.setGeometry(QtCore.QRect(780, 60, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonDiscounts.setFont(font)
        self.pushButtonDiscounts.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"    border: none")
        self.pushButtonDiscounts.setObjectName("pushButtonDiscounts")
        self.pushButtonAboutUs = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonAboutUs.setGeometry(QtCore.QRect(900, 60, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -871, 988, 1512))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.frame.setMinimumSize(QtCore.QSize(100, 1500))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.frame.setFont(font)
        self.frame.setStyleSheet("    border: none")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.frame)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 50, 981, 301))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_2 = QtWidgets.QLabel(parent=self.page)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 961, 291))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("E:\\Personal Projects\\___Pycharm___\\FN5\\ui\\../images/nhagiat.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label = QtWidgets.QLabel(parent=self.page_2)
        self.label.setGeometry(QtCore.QRect(0, 0, 981, 301))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("E:\\Personal Projects\\___Pycharm___\\FN5\\ui\\../images/quynhaptrang.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.page_2)
        self.label_3 = QtWidgets.QLabel(parent=self.frame)
        self.label_3.setGeometry(QtCore.QRect(310, -10, 381, 61))
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
        self.label_4.setGeometry(QtCore.QRect(60, 390, 221, 311))
        self.label_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.label_4.setText("")
        self.label_4.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_4.setPixmap(QtGui.QPixmap("E:\\Personal Projects\\___Pycharm___\\FN5\\ui\\../images/quy-nhap-trang-poster.webp"))
        self.label_4.setScaledContents(True)
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.frame)
        self.label_5.setGeometry(QtCore.QRect(370, 390, 231, 311))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("E:\\Personal Projects\\___Pycharm___\\FN5\\ui\\../images/nha-gia-tien-sneak.webp"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.frame)
        self.label_6.setGeometry(QtCore.QRect(700, 390, 221, 311))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("E:\\Personal Projects\\___Pycharm___\\FN5\\ui\\../images/little-emma.webp"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.frame)
        self.label_7.setGeometry(QtCore.QRect(0, 700, 341, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: transparent;\n"
"    border: none")
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.frame)
        self.label_8.setGeometry(QtCore.QRect(380, 700, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: transparent;\n"
"    border: none")
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=self.frame)
        self.label_9.setGeometry(QtCore.QRect(700, 700, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: transparent;\n"
"    border: none")
        self.label_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.pushButtonTrlQNT = QtWidgets.QPushButton(parent=self.frame)
        self.pushButtonTrlQNT.setGeometry(QtCore.QRect(40, 750, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.pushButtonTrlQNT.setFont(font)
        self.pushButtonTrlQNT.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"    border: none")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("E:\\Personal Projects\\___Pycharm___\\FN5\\ui\\../images/ic_trailer.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonTrlQNT.setIcon(icon1)
        self.pushButtonTrlQNT.setIconSize(QtCore.QSize(20, 20))
        self.pushButtonTrlQNT.setObjectName("pushButtonTrlQNT")
        self.pushButtonQNT = QtWidgets.QPushButton(parent=self.frame)
        self.pushButtonQNT.setGeometry(QtCore.QRect(170, 750, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonQNT.setFont(font)
        self.pushButtonQNT.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"color: rgb(0, 0, 0);\n"
"    border-radius: 5px;\n"
"    padding: 5px")
        self.pushButtonQNT.setObjectName("pushButtonQNT")
        self.pushButtonNGT = QtWidgets.QPushButton(parent=self.frame)
        self.pushButtonNGT.setGeometry(QtCore.QRect(490, 750, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonNGT.setFont(font)
        self.pushButtonNGT.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"color: rgb(0, 0, 0);\n"
"    border-radius: 5px;\n"
"    padding: 5px")
        self.pushButtonNGT.setObjectName("pushButtonNGT")
        self.pushButtonEMMA = QtWidgets.QPushButton(parent=self.frame)
        self.pushButtonEMMA.setGeometry(QtCore.QRect(810, 750, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonEMMA.setFont(font)
        self.pushButtonEMMA.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"color: rgb(0, 0, 0);\n"
"    border-radius: 5px;\n"
"    padding: 5px")
        self.pushButtonEMMA.setObjectName("pushButtonEMMA")
        self.pushButtonTrlNGT = QtWidgets.QPushButton(parent=self.frame)
        self.pushButtonTrlNGT.setGeometry(QtCore.QRect(360, 750, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.pushButtonTrlNGT.setFont(font)
        self.pushButtonTrlNGT.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"    border: none")
        self.pushButtonTrlNGT.setIcon(icon1)
        self.pushButtonTrlNGT.setIconSize(QtCore.QSize(20, 20))
        self.pushButtonTrlNGT.setObjectName("pushButtonTrlNGT")
        self.pushButtonTrEmma = QtWidgets.QPushButton(parent=self.frame)
        self.pushButtonTrEmma.setGeometry(QtCore.QRect(690, 750, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.pushButtonTrEmma.setFont(font)
        self.pushButtonTrEmma.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"    border: none")
        self.pushButtonTrEmma.setIcon(icon1)
        self.pushButtonTrEmma.setIconSize(QtCore.QSize(20, 20))
        self.pushButtonTrEmma.setObjectName("pushButtonTrEmma")
        self.label_19 = QtWidgets.QLabel(parent=self.frame)
        self.label_19.setGeometry(QtCore.QRect(380, 1160, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("background-color: transparent;\n"
"    border: none")
        self.label_19.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(parent=self.frame)
        self.label_20.setGeometry(QtCore.QRect(700, 1160, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("background-color: transparent;\n"
"    border: none")
        self.label_20.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(parent=self.frame)
        self.label_21.setGeometry(QtCore.QRect(370, 850, 231, 311))
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap("E:\\Personal Projects\\___Pycharm___\\FN5\\ui\\../images/nghe-sieu-kho-noi.webp"))
        self.label_21.setScaledContents(True)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(parent=self.frame)
        self.label_22.setGeometry(QtCore.QRect(700, 850, 221, 311))
        self.label_22.setText("")
        self.label_22.setPixmap(QtGui.QPixmap("E:\\Personal Projects\\___Pycharm___\\FN5\\ui\\../images/nghi-le-truc-quy.webp"))
        self.label_22.setScaledContents(True)
        self.label_22.setObjectName("label_22")
        self.pushButtonTrlexor = QtWidgets.QPushButton(parent=self.frame)
        self.pushButtonTrlexor.setGeometry(QtCore.QRect(90, 1220, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.pushButtonTrlexor.setFont(font)
        self.pushButtonTrlexor.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"    border: none")
        self.pushButtonTrlexor.setIcon(icon1)
        self.pushButtonTrlexor.setIconSize(QtCore.QSize(20, 20))
        self.pushButtonTrlexor.setObjectName("pushButtonTrlexor")
        self.pushButtonTrdominion = QtWidgets.QPushButton(parent=self.frame)
        self.pushButtonTrdominion.setGeometry(QtCore.QRect(740, 1210, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.pushButtonTrdominion.setFont(font)
        self.pushButtonTrdominion.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"    border: none")
        self.pushButtonTrdominion.setIcon(icon1)
        self.pushButtonTrdominion.setIconSize(QtCore.QSize(20, 20))
        self.pushButtonTrdominion.setObjectName("pushButtonTrdominion")
        self.pushButtonTrlfairytale = QtWidgets.QPushButton(parent=self.frame)
        self.pushButtonTrlfairytale.setGeometry(QtCore.QRect(410, 1210, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.pushButtonTrlfairytale.setFont(font)
        self.pushButtonTrlfairytale.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"    border: none")
        self.pushButtonTrlfairytale.setIcon(icon1)
        self.pushButtonTrlfairytale.setIconSize(QtCore.QSize(20, 20))
        self.pushButtonTrlfairytale.setObjectName("pushButtonTrlfairytale")
        self.label_23 = QtWidgets.QLabel(parent=self.frame)
        self.label_23.setGeometry(QtCore.QRect(60, 850, 221, 311))
        self.label_23.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.label_23.setText("")
        self.label_23.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_23.setPixmap(QtGui.QPixmap("E:\\Personal Projects\\___Pycharm___\\FN5\\ui\\../images/tru-ta-ky.webp"))
        self.label_23.setScaledContents(True)
        self.label_23.setWordWrap(False)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(parent=self.frame)
        self.label_24.setGeometry(QtCore.QRect(0, 1170, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("background-color: transparent;\n"
"    border: none")
        self.label_24.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_24.setWordWrap(True)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(parent=self.frame)
        self.label_25.setGeometry(QtCore.QRect(150, 790, 691, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("background-color: transparent;\n"
"    border: none")
        self.label_25.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(400, 1380, 141, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: transparent;\n"
"\n"
"    border: none")
        self.pushButton_4.setText("")
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_42 = QtWidgets.QLabel(parent=self.frame)
        self.label_42.setGeometry(QtCore.QRect(260, 1420, 441, 61))
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
        self.label_43.setGeometry(QtCore.QRect(270, 1450, 411, 61))
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
        self.label_44.setGeometry(QtCore.QRect(280, 1280, 381, 71))
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
        self.line_2.setGeometry(QtCore.QRect(-10, 1290, 1001, 1))
        self.line_2.setMaximumSize(QtCore.QSize(16777215, 1))
        self.line_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.pushButtonfb = QtWidgets.QPushButton(parent=self.frame)
        self.pushButtonfb.setGeometry(QtCore.QRect(410, 1340, 121, 31))
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("E:\\Personal Projects\\___Pycharm___\\FN5\\ui\\../images/fb.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonfb.setIcon(icon2)
        self.pushButtonfb.setIconSize(QtCore.QSize(30, 30))
        self.pushButtonfb.setAutoRepeatDelay(305)
        self.pushButtonfb.setObjectName("pushButtonfb")
        self.verticalLayout.addWidget(self.frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 60, 1001, 1))
        self.line.setMaximumSize(QtCore.QSize(16777215, 1))
        self.line.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.comboBoxSelect1 = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBoxSelect1.setGeometry(QtCore.QRect(20, 80, 76, 16))
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
        self.pushButtonLogOut = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonLogOut.setGeometry(QtCore.QRect(860, 20, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonLogOut.setFont(font)
        self.pushButtonLogOut.setStyleSheet("background-color: rgb(73, 34, 127);\n"
"color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"    padding: 5px")
        self.pushButtonLogOut.setObjectName("pushButtonLogOut")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1003, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HOME"))
        self.pushButtonShwtm.setText(_translate("MainWindow", "Showtimes"))
        self.pushButtonDiscounts.setText(_translate("MainWindow", "Discounts"))
        self.pushButtonAboutUs.setText(_translate("MainWindow", "About Us"))
        self.label_3.setText(_translate("MainWindow", "NOW SHOWING"))
        self.label_7.setText(_translate("MainWindow", "QUỶ NHẬP TRÀNG (T18)"))
        self.label_8.setText(_translate("MainWindow", "NHÀ GIA TIÊN (T18)"))
        self.label_9.setText(_translate("MainWindow", "LITTLE EMMA (T18)"))
        self.pushButtonTrlQNT.setText(_translate("MainWindow", "Watch Trailer"))
        self.pushButtonQNT.setText(_translate("MainWindow", "BUY TICKETS"))
        self.pushButtonNGT.setText(_translate("MainWindow", "BUY TICKETS"))
        self.pushButtonEMMA.setText(_translate("MainWindow", "BUY TICKETS"))
        self.pushButtonTrlNGT.setText(_translate("MainWindow", "Watch Trailer"))
        self.pushButtonTrEmma.setText(_translate("MainWindow", "Watch Trailer"))
        self.label_19.setText(_translate("MainWindow", "FORBIDDEN FAIRYTALE"))
        self.label_20.setText(_translate("MainWindow", "DOMINION OF DARKNESS"))
        self.pushButtonTrlexor.setText(_translate("MainWindow", "Watch Trailer"))
        self.pushButtonTrdominion.setText(_translate("MainWindow", "Watch Trailer"))
        self.pushButtonTrlfairytale.setText(_translate("MainWindow", "Watch Trailer"))
        self.label_24.setText(_translate("MainWindow", "EXORCISM CHRONICLES: THE BEGINNING (T13)"))
        self.label_25.setText(_translate("MainWindow", "COMMING SOON"))
        self.label_42.setText(_translate("MainWindow", "WE MAKE MOVIES BETTER"))
        self.label_43.setText(_translate("MainWindow", "© Copyright 2025 GFlix Theatres"))
        self.label_44.setText(_translate("MainWindow", "CONTACT US"))
        self.pushButtonfb.setText(_translate("MainWindow", "Facebook"))
        self.comboBoxSelect1.setItemText(0, _translate("MainWindow", "ALL THEATER"))
        self.comboBoxSelect1.setItemText(1, _translate("MainWindow", "UEL"))
        self.comboBoxSelect1.setItemText(2, _translate("MainWindow", "HỒ CHÍ MINH"))
        self.comboBoxSelect1.setItemText(3, _translate("MainWindow", "COMING SOON..."))
        self.pushButtonLogOut.setText(_translate("MainWindow", "LOG OUT"))

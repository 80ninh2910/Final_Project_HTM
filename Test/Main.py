from PyQt6.QtWidgets import QApplication, QMainWindow

from ui.MainEx import MainEx

app=QApplication([])
mainwindow=QMainWindow()
myui=MainEx()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()
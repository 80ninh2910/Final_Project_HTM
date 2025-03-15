from PyQt6 import QtWidgets, uic
from libs.DataConnector import DataConnector
from ui.QNT import Ui_MainWindow

class SeatSelectionWindow(QtWidgets.QDialog):

    def __init__(self, theater, showtime, parent=None):
        super().__init__(parent)
        self.setWindowTitle(f"Chọn Ghế - {theater} ({showtime})")
        self.theater = theater
        self.showtime = showtime
        self.selected_seats = set()

        # Layout chính
        layout = QtWidgets.QVBoxLayout(self)

        # Widget ghế ngồi
        self.widgetseat = QtWidgets.QWidget(self)
        self.grid_layout = QtWidgets.QGridLayout(self.widgetseat)
        self.create_seat_buttons()
        layout.addWidget(self.widgetseat)

        # Nút xác nhận
        self.ok_button = QtWidgets.QPushButton("OK", self)
        self.ok_button.clicked.connect(self.accept)
        layout.addWidget(self.ok_button)

    def create_seat_buttons(self):

        rows, cols = 4, 5
        self.seat_buttons = {}

        for row in range(rows):
            for col in range(cols):
                seat_number = f"{chr(65+row)}{col+1}"
                btn = QtWidgets.QPushButton(seat_number)
                btn.setCheckable(True)
                btn.setFixedSize(75, 50)
                btn.setStyleSheet("background-color: white; color: purple; border-radius: 10px;")
                btn.clicked.connect(lambda checked, b=btn: self.toggle_seat(b))
                self.grid_layout.addWidget(btn, row, col)
                self.seat_buttons[seat_number] = btn

    def toggle_seat(self, btn):

        seat_number = btn.text()
        if btn.isChecked():
            self.selected_seats.add(seat_number)
            btn.setStyleSheet("background-color: yellow; color: black; border-radius: 10px;")
        else:
            self.selected_seats.discard(seat_number)
            btn.setStyleSheet("background-color: white; color: purple; border-radius: 10px;")

    def get_selected_seats(self):

        return self.selected_seats

class QTNEx(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dc = DataConnector()

        self.selected_seats = set()
        self.theater = None
        self.showtime = None

        # Kết nối sự kiện chọn suất chiếu
        self.pushButtonhcm_9.clicked.connect(lambda: self.select_showtime("HCM", "9:00"))
        self.pushButtonhcm_12.clicked.connect(lambda: self.select_showtime("HCM", "12:15"))
        self.pushButtonhcm_14.clicked.connect(lambda: self.select_showtime("HCM", "14:20"))
        self.pushButtonhcm_19.clicked.connect(lambda: self.select_showtime("HCM", "19:00"))
        self.pushButtonhcm_23.clicked.connect(lambda: self.select_showtime("HCM", "23:00"))

        self.pushButtonUel_9.clicked.connect(lambda: self.select_showtime("UEL", "9:00"))
        self.pushButtonUel_12.clicked.connect(lambda: self.select_showtime("UEL", "12:15"))
        self.pushButtonUel_14.clicked.connect(lambda: self.select_showtime("UEL", "14:20"))
        self.pushButtonUel_19.clicked.connect(lambda: self.select_showtime("UEL", "19:00"))
        self.pushButtonUel_23.clicked.connect(lambda: self.select_showtime("UEL", "23:00"))

        self.comboBoxSelect2.currentTextChanged.connect(self.show_theater)
        self.comboBoxSelect1.currentTextChanged.connect(self.show_theater)

        self.labelTotal.setVisible(False)
        self.pushButtoncf.setVisible(False)
        self.pushButtoncf.clicked.connect(self.confirm_seats)

        self.displaymovie()

    def show_theater(self, text):

        self.comboBoxSelect2.setCurrentText(text)
        self.comboBoxSelect1.setCurrentText(text)

        if text == "ALL THEATER":
            self.widgethcm.setVisible(True)
            self.widgetuel.setVisible(True)
        elif text == "UEL":
            self.widgethcm.setVisible(False)
            self.widgetuel.setVisible(True)
        elif text == "HCM":
            self.widgethcm.setVisible(True)
            self.widgetuel.setVisible(False)



    def select_showtime(self, theater, showtime):

        seat_window = SeatSelectionWindow(theater, showtime, self)
        if seat_window.exec():  # Nếu người dùng bấm OK
            self.selected_seats = seat_window.get_selected_seats()
            self.theater = theater
            self.showtime = showtime
            self.labelTotal.setText(f"Rạp: {self.theater} | Giờ: {self.showtime} | Ghế đã chọn: {len(self.selected_seats)} | Ghế: {', '.join(self.selected_seats)}")
            self.labelTotal.setVisible(True)
            self.pushButtoncf.setVisible(True)

    def confirm_seats(self):
        if self.selected_seats:
            QtWidgets.QMessageBox.information(self, "Thành công", f"Rạp: {self.theater}\nGiờ: {self.showtime}\nBạn đã chọn: {', '.join(self.selected_seats)}")
            self.pushButtoncf.setVisible(False)
        else:
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Vui lòng chọn ít nhất một ghế!")

    def displaymovie(self):
        for i in self.dc.movie:
            if i.MTitle == "QUỶ NHẬP TRÀNG":
                movie = i
        self.labelType.setText(movie.MType)
        self.labelDu.setText(movie.dur)
        self.labelDes.setText(movie.des)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QTNEx()
    window.show()
    sys.exit(app.exec())
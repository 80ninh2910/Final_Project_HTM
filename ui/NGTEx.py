import sys

from PyQt6 import QtWidgets
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QDesktopServices
from librarys.CartManager import CartManager
from librarys.DataConnector import DataConnector
from librarys.UserSession import UserSession
from ui.NGT import Ui_MainWindow

class SeatSelectionWindow(QtWidgets.QDialog):
    def __init__(self, theater, showtime, parent=None):
        super().__init__(parent)
        self.seat_buttons = None
        self.ok_button = None
        self.grid_layout = None
        self.widgetseat = None
        self.setWindowTitle(f"Chọn Ghế - {theater} ({showtime})")
        self.theater = theater
        self.showtime = showtime
        self.selected_seats = set()

        self.initUI()

    def initUI(self):
        """Khởi tạo giao diện chọn ghế"""
        layout = QtWidgets.QVBoxLayout(self)
        self.widgetseat = QtWidgets.QWidget(self)
        self.grid_layout = QtWidgets.QGridLayout(self.widgetseat)
        self.create_seat_buttons()
        layout.addWidget(self.widgetseat)

        self.ok_button = QtWidgets.QPushButton("OK", self)
        self.ok_button.clicked.connect(self.accept)
        layout.addWidget(self.ok_button)

    def create_seat_buttons(self):
        """Tạo các nút chọn ghế"""
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
        """Xử lý chọn/bỏ chọn ghế"""
        seat_number = btn.text()
        if btn.isChecked():
            self.selected_seats.add(seat_number)
            btn.setStyleSheet("background-color: yellow; color: black; border-radius: 10px;")
        else:
            self.selected_seats.discard(seat_number)
            btn.setStyleSheet("background-color: white; color: purple; border-radius: 10px;")

    def get_selected_seats(self):
        """Trả về danh sách ghế đã chọn"""
        return self.selected_seats

class NGTEx(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.mainwindow = None
        self.popcorn_window = None
        self.setupUi(self)
        self.dc = DataConnector()
        self.cart = CartManager()
        self.selected_seats = set()
        self.theater = None
        self.showtime = None
        self.film = "NHÀ GIA TIÊN"

        self.setup_connections()
        self.display_movie_details()

        self.us=UserSession()
        self.display_user()

    def setup_connections(self):
        """Kết nối các nút với sự kiện tương ứng"""
        self.pushButtonfb.clicked.connect(self.open_facebook)
        self.pushButtoncf.clicked.connect(self.confirm_seats)
        self.pushButtoncf.setVisible(False)
        self.labelTotal.setVisible(False)
        self.pushButtonDiscounts.clicked.connect(self.open_discount)
        self.pushButtonAboutUs.clicked.connect(self.open_aboutus)
        self.pushButtonHome.clicked.connect(self.home)

        # Kết nối nút chọn suất chiếu
        showtime_buttons = {
            "HCM": [self.pushButtonhcm_9, self.pushButtonhcm_12, self.pushButtonhcm_14, self.pushButtonhcm_19, self.pushButtonhcm_23],
            "UEL": [self.pushButtonUel_9, self.pushButtonUel_12, self.pushButtonUel_14, self.pushButtonUel_19, self.pushButtonUel_23]
        }

        showtime_hours = ["9:00", "12:15", "14:20", "19:00", "23:00"]
        for theater, buttons in showtime_buttons.items():
            for button, hour in zip(buttons, showtime_hours):
                button.clicked.connect(lambda _, t=theater, h=hour: self.select_showtime(t, h))

    def select_showtime(self, theater, showtime):
        """Xử lý chọn suất chiếu và chọn ghế"""
        seat_window = SeatSelectionWindow(theater, showtime, self)
        if seat_window.exec():
            self.selected_seats = seat_window.get_selected_seats()
            self.theater = theater
            self.showtime = showtime
            for seat in self.selected_seats:
                row, col = seat[0], seat[1:]
                self.cart.add_seat(row, col, self.theater, self.showtime)
            self.labelTotal.setText(f"Phim: {self.film} | Rạp: {self.theater} | Giờ: {self.showtime} | Ghế: {', '.join(self.selected_seats)}")
            self.labelTotal.setVisible(True)
            self.pushButtoncf.setVisible(True)

    def confirm_seats(self):
        """Xác nhận ghế đã chọn và chuyển sang màn hình mua bắp rang"""
        if self.selected_seats:
            QtWidgets.QMessageBox.information(self, "Thành công", f"Rạp: {self.theater}\nGiờ: {self.showtime}\nBạn đã chọn: {', '.join(self.selected_seats)}")
            self.pushButtoncf.setVisible(False)
            from BuyPopcornEx import BuyPopcornEx
            self.popcorn_window = BuyPopcornEx()
            self.popcorn_window.show()
            self.hide()
        else:
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Vui lòng chọn ít nhất một ghế!")

    def display_movie_details(self):
        """Hiển thị thông tin phim"""
        for i in self.dc.movie:
            if i.MTitle =="NHÀ GIA TIÊN":
                movie=i
            self.labelType.setText(movie.MType)
            self.labelDu.setText(movie.dur)
            self.labelDes.setText(movie.des)

    def display_user(self):
        info=self.us.get_user()
        self.lineEditUsn.setText(str(info["username"]))
        self.lineEditPhone.setText(str(info["email"]))

    @staticmethod
    def open_facebook():
        """Mở trang Facebook"""
        QDesktopServices.openUrl(QUrl("https://www.facebook.com/profile.php?id=61573908070943"))

    def open_discount(self):
        from ui.Discount.DiscountEx import DiscountEx
        if self.mainwindow is None:
            self.mainwindow = DiscountEx()
        self.mainwindow.show()
        self.close()

    def open_aboutus(self):
        from ui.AboutUs.AboutUsEx import AboutUsEx
        if self.mainwindow is None:
            self.mainwindow = AboutUsEx()
        self.mainwindow.show()
        self.close()
    def home(self):
        from ui.MainEx import MainEx

        if self.mainwindow is None:
            self.mainwindow = MainEx()

        self.mainwindow.show()
        self.close()
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    signup_window = NGTEx()
    signup_window.show()
    sys.exit(app.exec())
from PyQt6 import QtWidgets, uic

from libs.DataConnector import DataConnector
from ui.QNT import Ui_MainWindow

class QTNEx(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dc=DataConnector()

        # Ẩn màn hình chọn ghế mặc định
        self.widgetseat.setVisible(False)

        # Gán sự kiện cho các button chọn giờ (đúng với file QNT.py)
        self.pushButtonhcm_9.clicked.connect(lambda: self.select_showtime_hcm("HCM1"))
        self.pushButtonUel_9.clicked.connect(lambda: self.select_showtime_uel("UEL1"))
        self.comboBoxSelect2.currentTextChanged.connect(self.show_theater)
        self.comboBoxSelect1.currentTextChanged.connect(self.show_theater)

        # Tạo ghế động trong widgetseat
        self.create_seat_buttons()

        # Ô hiển thị tổng số ghế đã chọn
          # Xóa nội dung ban đầu

        # Tạo nút xác nhận ghế
        self.labelTotal.setVisible(False)
        self.pushButtoncf.setVisible(False)  # Ẩn ban đầu
        self.pushButtoncf.clicked.connect(self.confirm_seats)

        self.displaymovie()
    def show_theater(self,text):
        self.comboBoxSelect2.setCurrentText(text)
        self.comboBoxSelect1.setCurrentText(text)
        if text=="ALL THEATER":
            self.widgethcm.setVisible(True)
            self.widgetuel.setVisible(True)
        elif text=="UEL":
            self.widgethcm.setVisible(False)
            self.widgetuel.setVisible(True)
        else:
            self.widgetuel.setVisible(False)
            self.widgethcm.setVisible(True)
    def create_seat_buttons(self):
        grid_layout = QtWidgets.QGridLayout(self.widgetseat)
        self.selected_seats = set()
        rows, cols = 4, 5  # Số hàng và số cột ghế
        for row in range(rows):
            for col in range(cols):
                seat_number = f"{chr(65+row)}{col+1}"  # A1, A2,... B1, B2, ...
                btn = QtWidgets.QPushButton(seat_number)
                btn.setCheckable(True)
                btn.setFixedSize(75, 50)
                btn.setStyleSheet("background-color: white; color: purple; border-radius: 10px;")
                btn.clicked.connect(lambda checked, b=btn: self.toggle_seat(b))
                grid_layout.addWidget(btn, row, col)

    def select_showtime_uel(self, theater):
        """Ẩn rạp còn lại và mở màn hình chọn ghế"""
        self.widgethcm.setVisible(False)
        self.widgetseat.setVisible(True)  # Hiện màn hình chọn ghế
        self.pushButtoncf.setVisible(True)  # Hiện nút xác nhận ghế
        self.labelTotal.setVisible(True)
        self.comboBoxSelect2.setCurrentText("UEL")
        self.comboBoxSelect1.setCurrentText("UEL")
    def select_showtime_hcm(self, theater):
        """Ẩn rạp còn lại và mở màn hình chọn ghế"""
        self.widgetuel.setVisible(False)
        self.widgetseat.setVisible(True)  # Hiện màn hình chọn ghế
        self.pushButtoncf.setVisible(True)  # Hiện nút xác nhận ghế
        self.labelTotal.setVisible(True)
        self.comboBoxSelect2.setCurrentText("HỒ CHÍ MINH")
        self.comboBoxSelect1.setCurrentText("HỒ CHÍ MINH")
    def toggle_seat(self, btn):
        """Chọn hoặc bỏ chọn ghế"""
        seat_number = btn.text()
        if btn.isChecked():
            self.selected_seats.add(seat_number)
            btn.setStyleSheet(
                "background-color: yellow; color: black; border-radius: 10px;")  # Khi chọn, nền vàng chữ đen
        else:
            self.selected_seats.discard(seat_number)
            btn.setStyleSheet("background-color: white; color: purple;border-radius: 10px;")  # Khi bỏ chọn, nền trắng chữ tím

        # Cập nhật tổng số ghế đã chọn vào labelTotal
        self.labelTotal.setText(f"Số ghế đã chọn: {len(self.selected_seats)} | Ghế: {', '.join(self.selected_seats)}")

    def confirm_seats(self):
        """Xác nhận ghế đã chọn"""
        if self.selected_seats:
            QtWidgets.QMessageBox.information(self, "Thành công", "Bạn đã chọn: " + ", ".join(self.selected_seats))
            self.widgetseat.setVisible(False)  # Ẩn màn hình chọn ghế
            self.pushButtoncf.setVisible(False)  # Ẩn nút xác nhận ghế
        else:
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Vui lòng chọn ít nhất một ghế!")

    def displaymovie(self):
        for i in self.dc.movie:
            if i.MTitle =="QUỶ NHẬP TRÀNG":
                movie=i
        self.labelType.setText(movie.MType)
        self.labelDu.setText(movie.dur)
        self.labelDes.setText(movie.des)


# Chạy ứng dụng
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QTNEx()
    window.show()
    sys.exit(app.exec())

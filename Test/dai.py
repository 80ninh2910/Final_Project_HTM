from PyQt6 import QtWidgets

class CinemaBooking(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Tạo layout chính
        self.layout = QtWidgets.QVBoxLayout(self)

        # Nút chọn giờ chiếu
        self.time_buttons = []
        showtimes = ["09:00", "11:30", "13:00", "15:00"]
        for time in showtimes:
            btn = QtWidgets.QPushButton(time)
            btn.clicked.connect(self.show_cinema_list)
            self.layout.addWidget(btn)
            self.time_buttons.append(btn)

        # Combo box chọn rạp
        self.cinema_combo = QtWidgets.QComboBox()
        self.cinema_combo.addItem("Chọn rạp")  # Mục mặc định
        self.cinema_combo.addItems(["Cinestar Quoc Thanh", "Cinestar Hai Ba Trung"])
        self.cinema_combo.currentTextChanged.connect(self.show_seat_selection)
        self.layout.addWidget(self.cinema_combo)
        self.cinema_combo.hide()  # Ẩn ban đầu

        # Màn hình chọn ghế (Ẩn mặc định)
        self.seat_selection = QtWidgets.QGroupBox("Chọn Ghế Ngồi")
        self.seat_selection_layout = QtWidgets.QGridLayout()
        self.seat_selection.setLayout(self.seat_selection_layout)
        self.seat_selection.hide()

        # Tạo danh sách ghế
        self.selected_seats = []
        rows = "ABCDEFGH"
        self.seat_buttons = []
        for i, row in enumerate(rows):
            row_buttons = []
            for j in range(10):  # 10 cột ghế
                seat_name = f"{row}{j+1}"
                btn = QtWidgets.QPushButton(seat_name)
                btn.setCheckable(True)  # Cho phép chọn ghế
                btn.clicked.connect(lambda checked, name=seat_name: self.select_seat(name, checked))
                self.seat_selection_layout.addWidget(btn, i, j)
                row_buttons.append(btn)
            self.seat_buttons.append(row_buttons)

        # Nút xác nhận đặt ghế
        self.confirm_button = QtWidgets.QPushButton("Xác nhận")
        self.confirm_button.clicked.connect(self.confirm_selection)
        self.seat_selection_layout.addWidget(self.confirm_button, len(rows), 0, 1, 10)

        self.layout.addWidget(self.seat_selection)

        # Ô hiển thị tổng số ghế đã chọn
        self.selected_seats_info = QtWidgets.QLineEdit()
        self.selected_seats_info.setPlaceholderText("Số ghế đã chọn: 0 | Ghế: ")
        self.selected_seats_info.setReadOnly(True)
        self.layout.addWidget(self.selected_seats_info)

    def show_cinema_list(self):
        """Hiển thị danh sách rạp khi chọn giờ chiếu"""
        self.cinema_combo.show()

    def show_seat_selection(self, text):

        """Hiển thị màn hình chọn ghế khi chọn rạp"""
        if text=="Cinestar Quoc Thanh":  # Chỉ mở nếu chọn rạp hợp lệ
            self.seat_selection.show()
            return

    def select_seat(self, seat_name, checked):
        """Cập nhật danh sách ghế khi chọn"""
        if checked:
            self.selected_seats.append(seat_name)
        else:
            self.selected_seats.remove(seat_name)

        # Cập nhật ô LineEdit
        self.selected_seats_info.setText(f"Số ghế đã chọn: {len(self.selected_seats)} | Ghế: {', '.join(self.selected_seats)}")

    def confirm_selection(self):
        """Xác nhận và ẩn màn hình chọn ghế, đồng thời lưu tên rạp"""
        if self.selected_seats:
            selected_cinema = self.cinema_combo.currentText()  # Lấy tên rạp
            seat_info = f"Số ghế đã chọn: {len(self.selected_seats)} | Ghế: {', '.join(self.selected_seats)}"
            final_info = f"Rạp: {selected_cinema}\n{seat_info}"

            # Hiển thị thông báo xác nhận
            QtWidgets.QMessageBox.information(self, "Thành công", final_info)

            # Lưu vào QLineEdit
            self.selected_seats_info.setText(final_info)

            # Ẩn màn hình chọn ghế
            self.seat_selection.hide()
        else:
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Vui lòng chọn ít nhất một ghế!")

    def toggle_seat_selection(self, seat_number):
        """Xử lý chọn hoặc bỏ chọn ghế"""
        if seat_number in self.selected_seats:
            self.selected_seats.remove(seat_number)  # Hủy chọn ghế
        else:
            self.selected_seats.append(seat_number)  # Chọn ghế

        self.update_selected_info()

    def update_selected_info(self):
        """Cập nhật thông tin ghế và rạp vào QLineEdit"""
        selected_cinema = self.cinema_combo.currentText()  # Lấy tên rạp
        seat_info = f"Số ghế đã chọn: {len(self.selected_seats)} | Ghế: {', '.join(self.selected_seats)}"
        final_info = f"Rạp: {selected_cinema}\n{seat_info}"

        self.selected_seats_info.setText(final_info)  # Cập nhật UI


# Chạy ứng dụng
app = QtWidgets.QApplication([])
window = CinemaBooking()
window.show()
app.exec()

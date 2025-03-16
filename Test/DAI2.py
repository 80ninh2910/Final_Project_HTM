from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QGridLayout, QDialog
import sys


class SeatSelection(QDialog):
    seat_data = {}  # Lưu trạng thái ghế cho từng suất chiếu

    def __init__(self, cinema, time, parent):
        super().__init__(parent)
        self.setWindowTitle(f"Chọn ghế - {cinema} - {time}")
        self.setGeometry(100, 100, 400, 350)
        self.parent = parent
        self.cinema = cinema
        self.time = time

        if (cinema, time) not in SeatSelection.seat_data:
            SeatSelection.seat_data[(cinema, time)] = set()

        layout = QVBoxLayout()
        layout.addWidget(QLabel(f"Chọn ghế cho suất chiếu: {cinema} - {time}"))

        grid = QGridLayout()
        self.buttons = {}
        for row in range(5):
            for col in range(6):
                seat_label = f"{chr(65 + row)}{col + 1}"
                btn = QPushButton(seat_label)
                if seat_label in SeatSelection.seat_data[(cinema, time)]:
                    btn.setStyleSheet("background-color: green; color: white;")
                    btn.setEnabled(False)
                btn.clicked.connect(self.select_seat)
                grid.addWidget(btn, row, col)
                self.buttons[seat_label] = btn

        layout.addLayout(grid)

        self.confirm_button = QPushButton("Xác nhận")
        self.confirm_button.clicked.connect(self.confirm_selection)
        layout.addWidget(self.confirm_button)

        self.setLayout(layout)

    def select_seat(self):
        sender = self.sender()
        sender.setStyleSheet("background-color: green; color: white;")
        sender.setEnabled(False)
        SeatSelection.seat_data[(self.cinema, self.time)].add(sender.text())

    def confirm_selection(self):
        self.accept()
        self.parent.update_selected_seats()
        self.parent.reset_to_main()


class CinemaApp(QWidget):
    from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QGridLayout, QDialog
    import sys

    class SeatSelection(QDialog):
        seat_data = {}  # Lưu trạng thái ghế cho từng suất chiếu

        def __init__(self, cinema, time, parent):
            super().__init__(parent)
            self.setWindowTitle(f"Chọn ghế - {cinema} - {time}")
            self.setGeometry(100, 100, 400, 350)
            self.parent = parent
            self.cinema = cinema
            self.time = time

            if (cinema, time) not in SeatSelection.seat_data:
                SeatSelection.seat_data[(cinema, time)] = set()

            layout = QVBoxLayout()
            layout.addWidget(QLabel(f"Chọn ghế cho suất chiếu: {cinema} - {time}"))

            grid = QGridLayout()
            self.buttons = {}
            for row in range(5):
                for col in range(6):
                    seat_label = f"{chr(65 + row)}{col + 1}"
                    btn = QPushButton(seat_label)
                    if seat_label in SeatSelection.seat_data[(cinema, time)]:
                        btn.setStyleSheet("background-color: green; color: white;")
                        btn.setEnabled(False)
                    btn.clicked.connect(self.select_seat)
                    grid.addWidget(btn, row, col)
                    self.buttons[seat_label] = btn

            layout.addLayout(grid)

            self.confirm_button = QPushButton("Xác nhận")
            self.confirm_button.clicked.connect(self.confirm_selection)
            layout.addWidget(self.confirm_button)

            self.setLayout(layout)

        def select_seat(self):
            sender = self.sender()
            sender.setStyleSheet("background-color: green; color: white;")
            sender.setEnabled(False)
            SeatSelection.seat_data[(self.cinema, self.time)].add(sender.text())

        def confirm_selection(self):
            self.parent.update_selected_seats()
            self.parent.reset_to_main()
            self.accept()

    class CinemaApp(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Hệ thống đặt vé rạp chiếu phim")
            self.setGeometry(100, 100, 400, 350)

            self.layout = QVBoxLayout()
            self.selected_seats_label = QLabel("Ghế đã chọn: Chưa có")
            self.layout.addWidget(self.selected_seats_label)

            self.init_main_screen()
            self.setLayout(self.layout)

        def init_main_screen(self):
            self.layout.addWidget(QLabel("Chọn rạp:"))

            self.cinema_buttons = []
            self.cinemas = {"Rạp A": ["10:00", "13:00", "16:00"], "Rạp B": ["11:00", "14:00", "17:00"]}

            for cinema in self.cinemas.keys():
                btn = QPushButton(cinema)
                btn.clicked.connect(lambda checked, c=cinema: self.show_times(c))
                self.layout.addWidget(btn)
                self.cinema_buttons.append(btn)

        def show_times(self, cinema):
            self.clear_layout()
            self.layout.addWidget(QLabel(f"Chọn giờ chiếu tại {cinema}:"))
            for time in self.cinemas[cinema]:
                btn = QPushButton(time)
                btn.clicked.connect(lambda checked, c=cinema, t=time: self.open_seat_selection(c, t))
                self.layout.addWidget(btn)

        def open_seat_selection(self, cinema, time):
            self.seat_window = SeatSelection(cinema, time, self)
            self.seat_window.exec()

        def update_selected_seats(self):
            selected_info = []
            for (cinema, time), seats in SeatSelection.seat_data.items():
                if seats:
                    selected_info.append(f"{cinema} - {time}: {', '.join(seats)}")
            if selected_info:
                self.selected_seats_label.setText("Ghế đã chọn: " + " | ".join(selected_info))
            else:
                self.selected_seats_label.setText("Ghế đã chọn: Chưa có")

        def reset_to_main(self):
            self.clear_layout()
            self.init_main_screen()

        def clear_layout(self):
            while self.layout.count():
                item = self.layout.takeAt(0)
                if item.widget():
                    item.widget().deleteLater()

    if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = CinemaApp()
        window.show()
        sys.exit(app.exec())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CinemaApp()
    window.show()
    sys.exit(app.exec())

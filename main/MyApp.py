from PyQt6.QtWidgets import QApplication

from ui.SignUpEx import SignUpEx

app = QApplication([])
signup_window = SignUpEx()
signup_window.show()
app.exec()
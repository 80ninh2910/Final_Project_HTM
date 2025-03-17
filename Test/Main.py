import sys
from PyQt6.QtWidgets import QApplication

from ui.MainEx import MainEx

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainEx()
    main_window.show()
    sys.exit(app.exec()) # ✅ Chạy event loop của PyQt

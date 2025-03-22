from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem
from librarys.CartManager import CartManager
from librarys.DataConnector import DataConnector
from ui.BuyPopcorn import Ui_MainWindow

class BuyPopcornEx(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupSignalAndSlots()
        self.mainwindow = None
        self.data_connector = DataConnector()
        self.beverages = self.data_connector.bev  # Lấy danh sách đồ uống
        self.popcorns = self.data_connector.pop  # Lấy danh sách bắp rang
        self.combos = self.data_connector.com  # Lấy danh sách combo
        self.cm = CartManager()  # Giỏ hàng
        self.setup_cart()

    def showWindow(self):
        """Hiển thị cửa sổ"""
        self.show()

    def setupSignalAndSlots(self):
        """Kết nối các nút bấm với các chức năng tương ứng"""
        self.pushButtonHome.clicked.connect(self.home)
        self.pushButtonAboutUs.clicked.connect(self.open_aboutus)
        self.pushButtonDiscounts.clicked.connect(self.open_discount)

        product_buttons = {
            "Coca Cola": (self.pushButton_7, self.pushButton_6),
            "Sprite": (self.pushButton_9, self.pushButton_8),
            "Fanta": (self.pushButton_11, self.pushButton_10),
            "Original": (self.pushButton_15, self.pushButton_14),
            "Cheese": (self.pushButton_17, self.pushButton_16),
            "Caramel": (self.pushButton_13, self.pushButton_12),
            "Combo Solo": (self.pushButton_2, self.pushButton),
            "Combo Couple": (self.pushButton_5, self.pushButton_4)
        }

        # Thiết lập sự kiện tăng/giảm số lượng sản phẩm
        for product, (increase_btn, decrease_btn) in product_buttons.items():
            increase_btn.clicked.connect(lambda _, p=product: self.updateQuantity(p, 1))
            decrease_btn.clicked.connect(lambda _, p=product: self.updateQuantity(p, -1))

        self.pushButtonPayment.clicked.connect(self.payment)

    def payment(self):
        """Chuyển sang màn hình thanh toán"""
        from PaymentEx import PaymentEx
        self.payment_window = PaymentEx()
        self.payment_window.show()
        self.close()

    def home(self):
        """Chuyển về màn hình chính và làm mới giỏ hàng"""
        self.cm.clear()
        from ui.MainEx import MainEx
        self.mainwindow = MainEx()
        self.mainwindow.show()
        self.close()

    def open_aboutus(self):
        """Mở cửa sổ 'Giới thiệu'"""
        from ui.AboutUs.AboutUsEx import AboutUsEx
        self.mainwindow = AboutUsEx()
        self.mainwindow.show()
        self.close()

    def open_discount(self):
        """Mở cửa sổ 'Khuyến mãi'"""
        from ui.Discount.DiscountEx import DiscountEx
        self.mainwindow = DiscountEx()
        self.mainwindow.show()
        self.close()

    def setup_cart(self):
        """Thiết lập giỏ hàng với tất cả các sản phẩm có sẵn"""
        for product in self.beverages + self.popcorns + self.combos:
            self.cm.add_product(product.Name, 0)
        self.updateTable()

    def updateQuantity(self, product_name, change):
        """Cập nhật số lượng sản phẩm trong giỏ hàng"""
        if change > 0:
            self.cm.add_product(product_name, change)
        else:
            self.cm.delete_product(product_name)

        quantity = self.cm.cart["products"].get(product_name, 0)
        self.updateTable()

        # Cập nhật số lượng hiển thị trên giao diện
        label_map = {
            "Coca Cola": self.labelCoke,
            "Sprite": self.labelSprite,
            "Fanta": self.labelFanta,
            "Original": self.labelOriginal,
            "Cheese": self.labelCheese,
            "Caramel": self.labelCaramel,
            "Combo Solo": self.labelSolo,
            "Combo Couple": self.labelCouple
        }
        if product_name in label_map:
            label_map[product_name].setText(str(quantity))

    def updateTable(self):
        """Cập nhật bảng hiển thị giỏ hàng"""
        self.tableWidget.clear()
        self.tableWidget.setRowCount(len(self.cm.cart["products"]) + 1)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels( ["Name", "Quantity", "Price", "Total"])
        total_price = 0
        row = 0

        # Thêm các sản phẩm vào bảng
        for product, quantity in self.cm.cart["products"].items():
            if quantity > 0:
                price = next((p.Price for p in self.beverages + self.popcorns + self.combos if p.Name == product), 0)
                total_item_price = quantity * price
                self.tableWidget.setItem(row, 0, QTableWidgetItem(product))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(str(quantity)))
                self.tableWidget.setItem(row, 2, QTableWidgetItem(f"{price} VND"))
                self.tableWidget.setItem(row, 3, QTableWidgetItem(f"{total_item_price} VND"))
                total_price += total_item_price
                row += 1

        # Thêm tổng giá trị vào dòng cuối cùng
        self.tableWidget.setItem(row, 0, QTableWidgetItem("Total"))
        self.tableWidget.setItem(row, 3, QTableWidgetItem(f"{total_price} VND"))
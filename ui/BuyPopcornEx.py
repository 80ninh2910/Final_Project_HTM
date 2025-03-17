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
        self.beverages = self.data_connector.bev
        self.popcorns = self.data_connector.pop
        self.combos = self.data_connector.com


        self.cm = CartManager()

        self.setup_cart()
    def showWindow(self):
        self.show()
    def setupSignalAndSlots(self):
        self.pushButtonHome.clicked.connect(self.home)

        #tang
        self.pushButton_7.clicked.connect(lambda: self.updateQuantity("Coca Cola", 1))
        self.pushButton_9.clicked.connect(lambda: self.updateQuantity("Sprite", 1))
        self.pushButton_11.clicked.connect(lambda: self.updateQuantity("Fanta", 1))
        self.pushButton_15.clicked.connect(lambda: self.updateQuantity("Original", 1))
        self.pushButton_17.clicked.connect(lambda: self.updateQuantity("Cheese", 1))
        self.pushButton_13.clicked.connect(lambda: self.updateQuantity("Caramel", 1))
        self.pushButton_2.clicked.connect(lambda: self.updateQuantity("Combo Solo", 1))
        self.pushButton_5.clicked.connect(lambda: self.updateQuantity("Combo Couple", 1))

        #giam
        self.pushButton_6.clicked.connect(lambda: self.updateQuantity("Coca Cola", -1))
        self.pushButton_8.clicked.connect(lambda: self.updateQuantity("Sprite", -1))
        self.pushButton_10.clicked.connect(lambda: self.updateQuantity("Fanta", -1))
        self.pushButton_14.clicked.connect(lambda: self.updateQuantity("Original", -1))
        self.pushButton_16.clicked.connect(lambda: self.updateQuantity("Cheese", -1))
        self.pushButton_12.clicked.connect(lambda: self.updateQuantity("Caramel", -1))
        self.pushButton.clicked.connect(lambda: self.updateQuantity("Combo Solo", -1))
        self.pushButton_4.clicked.connect(lambda: self.updateQuantity("Combo Couple", -1))

        self.pushButtonPayment.clicked.connect(self.payment)

    def payment(self):
        from PaymentEx import PaymentEx  # ✅ Import PaymentEx tại đây để tránh lỗi vòng lặp import
        self.payment_window = PaymentEx()  # ✅ Tạo cửa sổ thanh toán
        self.payment_window.show()  # ✅ Hiển thị cửa sổ thanh toán
        self.close()
    def home(self):
        self.cm.clear()
        from ui.MainEx import MainEx
        self.mainwindow = MainEx()
        self.mainwindow.show()
        self.close()  # ✅ Đóng chính cửa sổ này

    def setup_cart(self):

        for product in self.beverages + self.popcorns + self.combos:
            self.cm.add_product(product.Name,0)
        self.updateTable()

    def updateQuantity(self, product_name, change):
        if change > 0:
            self.cm.add_product(product_name, change)
        else:
            self.cm.delete_product(product_name)

        quantity = self.cm.cart["products"].get(product_name, 0)


        self.updateTable()
        if product_name == "Coca Cola":
            self.labelCoke.setText(str(quantity))
        elif product_name == "Sprite":
            self.labelSprite.setText(str(quantity))
        elif product_name == "Fanta":
            self.labelFanta.setText(str(quantity))
        elif product_name == "Original":
            self.labelOriginal.setText(str(quantity))
        elif product_name == "Cheese":
            self.labelCheese.setText(str(quantity))
        elif product_name == "Caramel":
            self.labelCaramel.setText(str(quantity))
        elif product_name == "Combo Solo":
            self.labelSolo.setText(str(quantity))
        elif product_name == "Combo Couple":
            self.labelCouple.setText(str(quantity))

    def updateTable(self):
        self.tableWidget.clear()
        self.tableWidget.setRowCount(len(self.cm.cart["products"]) + 1)  # ✅ Đúng
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(["Sản phẩm", "Số lượng", "Đơn giá", "Thành tiền"])

        total_price = 0
        row = 0

        for product, quantity in self.cm.cart["products"].items():  # ✅ Đúng
            if quantity > 0:
                price = next((p.Price for p in self.beverages + self.popcorns + self.combos if p.Name == product), 0)
                total_item_price = quantity * price

                self.tableWidget.setItem(row, 0, QTableWidgetItem(product))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(str(quantity)))
                self.tableWidget.setItem(row, 2, QTableWidgetItem(f"{price} VND"))
                self.tableWidget.setItem(row, 3, QTableWidgetItem(f"{total_item_price} VND"))

                total_price += total_item_price
                row += 1

        # 🔹 Thêm dòng Total vào cuối bảng
        self.tableWidget.setItem(row, 0, QTableWidgetItem("Total"))
        self.tableWidget.setItem(row, 3, QTableWidgetItem(f"{total_price} VND"))



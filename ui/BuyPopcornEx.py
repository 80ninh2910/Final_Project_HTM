from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem
from libs.DataConnector import DataConnector
from models.CONCESSION.Concession import CON
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


        self.cart = {}
        self.setup_cart()

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

    def home(self):

        from ui.MainEx import MainEx
        self.mainwindow = MainEx()
        self.mainwindow.show()
        self.close()  # ✅ Đóng chính cửa sổ này

    def setup_cart(self):

        for product in self.beverages + self.popcorns + self.combos:
            self.cart[product.Name] = {"price": product.Price, "quantity": 0}
        self.updateTable()

    def updateQuantity(self, product_name, change):

        if product_name in self.cart:
            self.cart[product_name]["quantity"] += change
            if self.cart[product_name]["quantity"] < 0:
                self.cart[product_name]["quantity"] = 0
                print(f"✅ {product_name}: {self.cart[product_name]['quantity']}")
        self.updateTable()
        if product_name == "Coca Cola":
            self.labelCoke.setText(str(self.cart[product_name]["quantity"]))
        elif product_name == "Sprite":
            self.labelSprite.setText(str(self.cart[product_name]["quantity"]))
        elif product_name == "Fanta":
            self.labelFanta.setText(str(self.cart[product_name]["quantity"]))
        elif product_name == "Original":
            self.labelOriginal.setText(str(self.cart[product_name]["quantity"]))
        elif product_name == "Cheese":
            self.labelCheese.setText(str(self.cart[product_name]["quantity"]))
        elif product_name == "Caramel":
            self.labelCaramel.setText(str(self.cart[product_name]["quantity"]))
        elif product_name == "Combo Solo":
            self.labelSolo.setText(str(self.cart[product_name]["quantity"]))
        elif product_name == "Combo Couple":
            self.labelCouple.setText(str(self.cart[product_name]["quantity"]))

    def updateTable(self):

        self.tableWidget.clear()
        self.tableWidget.setRowCount(len(self.cart) + 1)  # Thêm 1 dòng cho Total
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(["Sản phẩm", "Số lượng", "Đơn giá", "Thành tiền"])

        total_price = 0
        row = 0

        for product, data in self.cart.items():
            if data["quantity"] > 0:
                self.tableWidget.setItem(row, 0, QTableWidgetItem(product))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(str(data["quantity"])))
                self.tableWidget.setItem(row, 2, QTableWidgetItem(f"{data['price']} VND"))
                total_item_price = data["quantity"] * data["price"]
                self.tableWidget.setItem(row, 3, QTableWidgetItem(f"{total_item_price} VND"))

                total_price += total_item_price
                row += 1

        # 🔹 Thêm dòng Total vào cuối bảng
        self.tableWidget.setItem(row, 0, QTableWidgetItem("Total"))  # Cột Sản phẩm: "Total"
        self.tableWidget.setItem(row, 3, QTableWidgetItem(f"{total_price} VND"))  # Cột Thành tiền: Tổng tiền


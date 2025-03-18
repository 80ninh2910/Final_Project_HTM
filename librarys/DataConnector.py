from librarys.JSON_File_Factory import JsonFileFactory
from models.BOX.Movie import Movie
from models.CONCESSION.Beverage import Beverage
from models.CONCESSION.Combo import Combo
from models.CONCESSION.Concession import CON
from models.CONCESSION.Popcorn import Popcorn
from models.Customer import Customer

class DataConnector:
    def __init__(self):
        """Khởi tạo DataConnector và tải dữ liệu từ JSON"""
        self.cus = []
        self.con = []
        self.pop = []
        self.bev = []
        self.com = []
        self.movie = []
        self.get_data()

    def get_data(self):
        """Đọc dữ liệu từ các tệp JSON vào danh sách tương ứng"""
        jff = JsonFileFactory()
        self.cus = jff.read_data("../database/Customers.json", Customer)
        self.con = jff.read_data("../database/Concession.json", CON)
        self.pop = jff.read_data("../database/Popcorn.json", Popcorn)
        self.bev = jff.read_data("../database/Beverage.json", Beverage)
        self.com = jff.read_data("../database/Combo.json", Combo)
        self.movie = jff.read_data("../database/Movies.json", Movie)

    def login(self, email_username, pw):
        """Xác thực đăng nhập bằng email hoặc username và password"""
        for c in self.cus:
            if (c.email == email_username or c.username == email_username) and c.password == pw:
                return c
        return None

    def get_product_list(self, category):
        """Lấy danh sách sản phẩm theo loại"""
        if category == "Beverage":
            return self.bev
        elif category == "Popcorn":
            return self.pop
        elif category == "Combo":
            return self.com

    def save_transaction(self, transaction):
        """Lưu giao dịch vào danh sách và cập nhật vào tệp JSON"""
        self.con.append(transaction)
        jff = JsonFileFactory()
        jff.write_data(self.con, "Concession.json")

    def get_price(self, product_name):
        """Lấy giá của một sản phẩm dựa trên tên"""
        for product in self.bev + self.pop + self.com:
            if product.Name == product_name:
                return product.Price
        return 0
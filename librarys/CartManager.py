import json

class CartManager:
    """
    CartManager sử dụng Singleton Pattern để đảm bảo chỉ có một giỏ hàng
    được dùng chung trong các cửa sổ khác nhau của ứng dụng.
    """

    _instance = None  # Biến private lưu trữ instance duy nhất của class

    def __new__(cls) :
        """
        Khởi tạo instance duy nhất của CartManager nếu chưa có.
        """
        if cls._instance is None:
            cls._instance = super(CartManager, cls).__new__(cls)
            # Khởi tạo cart là một dict với 2 keys: seats và products
            cls._instance.cart = {"seats": {}, "products": {},"movie":[]}
        return cls._instance

    def add_seat(self, row: int, col: int, theater: str, showtime: str):
        """
        Thêm một ghế đã chọn vào giỏ hàng.

        Args:
            row (int): Số hàng ghế.
            col (int): Số cột ghế.
            theater (str): Tên rạp chiếu phim.
            showtime (str): Thời gian chiếu phim.
        """
        seat_id = f"{row}{col}"
        if seat_id not in self.cart["seats"]:
            self.cart["seats"][seat_id] = {"theater": theater, "showtime": showtime}

    def add_product(self, product: str, quantity: int):
        """
        Thêm sản phẩm vào giỏ hàng.

        Args:
            product (str): Tên sản phẩm.
            quantity (int): Số lượng sản phẩm.
        """
        if product in self.cart["products"]:
            self.cart["products"][product] += quantity
        else:
            self.cart["products"][product] = quantity

    def get_seats(self) -> dict:
        """Trả danh sách ghế đã chọn."""
        return self.cart["seats"]

    def get_products(self) -> list:
        """Trả danh sách tên các sản phẩm trong giỏ hàng."""
        return list(self.cart["products"].keys())

    def delete_seat(self, row: int, col: int):
        """Xóa ghế khỏi giỏ hàng."""
        seat_id = f"{row}{col}"
        if seat_id in self.cart["seats"]:
            del self.cart["seats"][seat_id]

    def delete_product(self, product: str):
        """Xóa sản phẩm khỏi giỏ hàng."""
        if product in self.cart["products"]:
            del self.cart["products"][product]

    def clear(self):
        """Làm mới giỏ hàng khi chạy màn hình đặt vé mới."""
        self.cart = {"seats": {}, "products": {}}

    def clear_cart(self):
        self.cart = {"products": {}, "seats": {}}  # Reset giỏ hàng

    def add_move(self,movie):
        self.cart["movie"]=movie

class PricingManager:
    def __init__(self):
        self.price_list = {}
        self.load_data_json()

    def load_data_json(self):
        """Load dữ liệu từ các tệp JSON và lưu vào price_list."""
        files = ["Combo.json", "Baverage.json", "Popcorn.json"]
        try:
            for file_name in files:
                with open(f'../database/{file_name}', 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    for item in data:
                        self.price_list[item["Name"]] = item["Price"]

        except FileNotFoundError as e:
            print(f"Error loading JSON files: {e}")

    def get_price(self, product_name):
        """Trả về giá của sản phẩm dựa vào tên sản phẩm."""
        return self.price_list.get(product_name, 0)  # Trả về 0 nếu sản phẩm không có trong danh sách

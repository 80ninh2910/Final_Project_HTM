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
            cls._instance.cart = {"seats": {}, "products": {}}
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

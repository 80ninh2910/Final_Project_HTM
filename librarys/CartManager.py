class CartManager:
    _instance=None
    def __new__(cls):
        if cls._instance==None:
            cls._instance= super(CartManager,cls).__new__(cls)
            cls._instance.cart={ "seats":{} , "products":{}}
        return cls._instance
    def add_seat(self,row,col,theater,showtime):
        id=f"{row}{col}"
        if id not in self.cart["seats"]:

            self.cart["seats"][id] = {"theater": theater, "showtime": showtime}

    def add_product(self,product,quantity):
        if product in self.cart["products"]:
            self.cart["products"][product] += quantity
        else:
            self.cart["products"][product] = quantity

    def get_seats(self):
        return self.cart["seats"]

    def get_products(self):
        return list(self.cart["products"].keys())

    def delete_seat(self,row,col):
        id=f"{row}{col}"
        if id in self.cart["seats"]:
            del self.cart["seats"][id]

    def delete_product(self,product):
        if product in self.cart["products"]:
            del self.cart["products"][product]

    def clear(self):
        self.cart={ "seats":{} , "products":{}}

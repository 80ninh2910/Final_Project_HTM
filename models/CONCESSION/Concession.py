class CON:
    def __init__(self, CId, popcorn=None, beverage=None, combo=None, Pquantity=0, Bquantity=0, Cquantity=0):
        self.CId = CId
        self.popcorn = popcorn
        self.beverage = beverage
        self.combo = combo
        self.Pquantity = Pquantity
        self.Bquantity = Bquantity
        self.Cquantity = Cquantity

    def total_price(self, Pprice, Bprice, Cprice):
        """Tính tổng giá trị đơn hàng"""
        return (self.Pquantity * Pprice) + (self.Bquantity * Bprice) + (self.Cquantity * Cprice)

    def __str__(self):
        """Trả về chuỗi mô tả đơn hàng"""
        return (
            f"Concession ID: {self.CId}\n"
            f"Popcorn: {self.popcorn} (Qty: {self.Pquantity})\n"
            f"Beverage: {self.beverage} (Qty: {self.Bquantity})\n"
            f"Combo: {self.combo} (Qty: {self.Cquantity})"
        )

class CON:
    def __init__(self,CId, popcorn=None,beverage=None,combo=None,Pquantity=None, Bquantity=None, Cquantity=None):
        self.CId=CId
        self.popcorn = popcorn
        self.beverage = beverage
        self.combo = combo
        self.Pquantity=Pquantity
        self.Bquantity=Bquantity
        self.Cquantity=Cquantity
    def total_price(self,Pprice,Bprice,Cprice):
        return self.Pquantity*Pprice + self.Bquantity*Bprice + self.Cquantity*Cprice
    def __str__(self):

        return f"Popcorn: {self.popcorn} (Qty: {self.Pquantity}), Beverage: {self.beverage} (Qty: {self.Bquantity}), Combo: {self.combo} (Qty: {self.Cquantity})"
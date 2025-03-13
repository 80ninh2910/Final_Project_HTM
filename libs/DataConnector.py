from libs.JSON_File_Factory import JsonFileFactory
from models.BOX.Movie import Movie
from models.CONCESSION.Beverage import Beverage
from models.CONCESSION.Combo import Combo
from models.CONCESSION.Concession import CON
from models.CONCESSION.Popcorn import Popcorn
from models.Customer import Customer


class DataConnector:
    def __init__(self):
        self.cus=[]
        self.con=[]
        self.pop=[]
        self.bev=[]
        self.com=[]
        self.movie=[]
        self.get_data()
    def get_data(self):
        jff=JsonFileFactory()
        self.cus=jff.read_data("../database/Customers.json",Customer)
        self.con=jff.read_data("../database/Concession.json",CON)
        self.pop=jff.read_data("../database/Popcorn.json",Popcorn)
        self.bev=jff.read_data("../database/Beverage.json",Beverage)
        self.com=jff.read_data("../database/Combo.json",Combo)
        self.movie=jff.read_data("../database/Movies.json",Movie)
    def login(self,email_username,pw):
        for c in self.cus:
            if (c.email==email_username or c.username==email_username) and c.password==pw:
                return c
        return None



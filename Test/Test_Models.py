from models.BOX.Movie import Movie
from models.BOX.Showtime import Showtime
from models.BOX.Theater import Theater
from models.CONCESSION.Concession import CON
from models.CONCESSION.Beverage import Beverage
from models.CONCESSION.Combo import Combo
from models.CONCESSION.Popcorn import Popcorn

movie1 = Movie("Hello", "T18", "109", "jgugferuygreyfgheufbwjcsjgwyucgeaufgaeugauycgwuyaejycgsejycgesucsejycgjdysvbjdyvfsyg")
theater1=Theater("1","CAMPUCHIA","258")
st=Showtime("1",movie1,theater1,"23","F1")

print(st)

pop=Popcorn("Cheese","2","50000")
print(pop)
bev=Beverage("Coke",2,"37000")
com=Combo("0","0","0")
bill= CON( pop,bev,com,"10000")
print(bill)

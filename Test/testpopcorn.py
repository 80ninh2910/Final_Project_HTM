from librarys.JSON_File_Factory import JsonFileFactory
from models.CONCESSION.Popcorn import Popcorn

pops=[]
p1=Popcorn("Original",50000)
p2=Popcorn("Cheese",60000)
p3=Popcorn("Caramel",60000)
pops.extend([p1,p2,p3])
jff=JsonFileFactory()
jff.write_data(pops,"../database/Popcorn.json")
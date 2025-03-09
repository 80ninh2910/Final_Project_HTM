from libs.JSON_File_Factory import JsonFileFactory
from models.CONCESSION.Beverage import Beverage

names=["Coca Cola","Sprite","Fanta"]
list_be=[]
for i in range(3):
    b=Beverage(names[i],37000)
    list_be.append(b)
jff=JsonFileFactory()
jff.write_data(list_be,"../database/Beverage.json")
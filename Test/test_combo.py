from librarys.JSON_File_Factory import JsonFileFactory
from models.CONCESSION.Combo import Combo

combos=[]
c1=Combo("Combo Solo",90000)
c2=Combo("Combo Couple",110000)
combos.extend([c1,c2])

jff=JsonFileFactory()
jff.write_data(combos,"../database/Combo.json")
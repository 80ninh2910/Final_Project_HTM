import json
import random

from libs.JSON_File_Factory import JsonFileFactory
from models.CONCESSION.Beverage import Beverage
from models.CONCESSION.Combo import Combo
from models.CONCESSION.Concession import CON
from models.CONCESSION.Popcorn import Popcorn
from models.Customer import Customer


# Load JSON data
def load_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)
jff=JsonFileFactory()
customers = jff.read_data("../database/customers.json",Customer)
popcorns = jff.read_data("../database/Popcorn.json",Popcorn)
beverages = jff.read_data("../database/Beverage.json",Beverage)
combos= jff.read_data("../database/Combo.json",Combo)



concessions = []
for i in range(100):
    customer = random.choice(customers)
    choice_type = random.choice(["combo", "individual", "single"])

    if choice_type == "combo":
        combo = random.choice(combos)
        concession = CON(
            CId=customer.CId,
            popcorn=None,
            beverage=None,
            combo=combo.CbName,
            Pquantity=0,
            Bquantity=0,
            Cquantity=random.randint(1, 2)
        )
    elif choice_type == "individual":
        popcorn = random.choice(popcorns)
        beverage = random.choice(beverages)
        concession = CON(
            CId=customer.CId,
            popcorn=popcorn.PName,
            beverage=beverage.BName,
            combo=None,
            Pquantity=random.randint(1, 3),
            Bquantity=random.randint(1, 3),
            Cquantity=0
        )
    else:  # "single" case
        if random.choice([True, False]):
            popcorn = random.choice(popcorns)
            concession = CON(
                CId=customer.CId,
                popcorn=popcorn.PName,
                beverage=None,
                combo=None,
                Pquantity=random.randint(1, 3),
                Bquantity=0,
                Cquantity=0
            )
        else:
            beverage = random.choice(beverages)
            concession = CON(
                CId=customer.CId,
                popcorn=None,
                beverage=beverage.BName,
                combo=None,
                Pquantity=0,
                Bquantity=random.randint(1, 3),
                Cquantity=0
            )

    concessions.append(concession)

# Print first 10 results
for concession in concessions[:10]:
    print(concession)



jff.write_data(concessions,"../database/Concession.json")

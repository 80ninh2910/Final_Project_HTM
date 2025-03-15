import random
import string

from librarys.JSON_File_Factory import JsonFileFactory
from models.Customer import Customer

name_parts = ["cool", "funny", "happy", "chill", "epic", "wild", "crazy", "swift", "fierce", "lucky"]
chars = string.ascii_lowercase + string.digits

customers = []
for i in range(1, 101):
    name=random.choice(name_parts)
    email = f"{name}@gmail.com"
    username = name + str(random.randint(10, 99))
    password = ''.join(random.sample(chars, 6))
    customers.append(Customer(email, username, password))

for customer in customers:
    print(customer)
jff=JsonFileFactory()
jff.write_data(customers,"../database/Customers.json")
import random

from libs.JSON_File_Factory import JsonFileFactory
from models.Customer import Customer

names = [
    "Nguyen Van An", "Tran Thi Bich", "Le Minh Duc", "Pham Thao Nhi", "Hoang Gia Huy",
    "Do Hoang Nam", "Bui Huu Phuoc", "Vu Hai Yen", "Ngo Thanh Tung", "Duong Quynh Anh",
    "Phan Khanh Linh", "Ly Dinh Bao", "Ta Hong Nhung", "Dinh Trong Hieu", "Cao Tuan Kiet",
    "Dang Thi Mai", "Trinh Ngoc Bao", "Ton Nu Diem My", "Ha Anh Tuan", "Lam Chi Thanh",
    "Phung Bao Chau", "Hua Ngoc Tram", "Kieu Minh Tuan", "Tong Thao Vi", "Chau Ngoc Bich"
]


phone_prefixes = ["090", "091", "092", "093", "094", "096", "097", "098", "099", "032", "033", "034", "035", "036", "037", "038", "039"]


customers = []
for i in range(1, 101):
    CId = f"{i:04d}"
    CName = random.choice(names)
    Phone = random.choice(phone_prefixes) + str(random.randint(1000000, 9999999))
    Mail = CName.lower().replace(" ", "") + "@gmail.com"
    DOB = f"{random.randint(1, 28)}/{random.randint(1, 12)}/{random.randint(1960, 2005)}"
    customers.append(Customer(CId, CName, Phone, Mail, DOB))

jff=JsonFileFactory()
jff.write_data(customers,"../database/customers.json")
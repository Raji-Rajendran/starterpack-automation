from random import randint

import barnum
from barnum import gen_data


class Config:
    base_url = 'https://qa.starterpack.2base.in/'


class AdminsConfig:
    name = barnum.create_name()
    first_name = name[0]
    last_name = name[1]
    email = f"{first_name}.{last_name}@yopmail.com"
    phone = randint(1000000000, 9999999999)
    role = "Admin"

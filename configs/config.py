import os
import random
from random import randint

import barnum
from barnum import gen_data
from dotenv import load_dotenv


# Function to load environment variables and get credentials
def get_credentials():
    load_dotenv()  # Load environment variables from .env file
    credentials = {
        'existing_email': os.getenv('EXISTING_EMAIL'),
    }
    return credentials


class Config:
    base_url = 'https://qa.starterpack.2base.in/'


class AdminsConfig:
    credentials = get_credentials()  # Call the function to get credentials
    name = barnum.create_name()
    first_name = name[0]
    middle_name = gen_data.create_name()[1]
    last_name = name[1]
    email = f"{first_name}.{last_name}@yopmail.com"
    new_email = f"{first_name}.{last_name}{randint(10, 99)}@yopmail.com"
    phone = randint(1000000000, 9999999999)
    role = "Admin"

    email_1 = "admin"
    email_2 = "admin123@"
    email_3 = "gmail.com"
    email_4 = "admin123@gmail"

    existing_email = credentials['existing_email']  # Access existing_email from credentials

    filter_status = "Admin"
    filter_role = "Active"


class UsersConfig:
    emails = ['alvera39@gmail.com', 'ufranecki@runolfsson.com', 'bgrant@stokes.info', 'kamron.heathcote@mueller.com',
              'hulda.franecki@hotmail.com', 'urice@dietrich.net', 'qmarquardt@hirthe.com', 'kirstin.veum@gmail.com',
              'kristoffer.thiel@simonis.com', 'augustine65@rutherford.com']
    email = random.choice(emails)

    filter_status = "Active"


class RolesConfig:
    role_names = ['Employee', 'Supervisor', 'Team Lead', 'Developer', 'Consultant', 'Coordinator', 'Specialist', 'Executive', 'Director', 'Team Member', 'Project Manager', 'Assistant', 'Associate', 'Senior Manager', 'Junior Manager', 'Senior Developer', 'Junior Developer', 'Senior Analyst', 'Junior Analyst', 'Senior Consultant', 'Junior Consultant', 'Senior Coordinator', 'Junior Coordinator', 'Senior Specialist', 'Junior Specialist', 'Senior Executive', 'Junior Executive', 'Chief Executive Officer', 'Chief Operating Officer', 'Chief Financial Officer', 'Chief Technology Officer', 'Chief Marketing Officer', 'Chief Human Resources Officer', 'Chief Information Officer', 'Senior Supervisor', 'Junior Supervisor', 'Senior Team Lead', 'Junior Team Lead', 'Lead Developer', 'Lead Analyst']
    role_name = random.choice(role_names)


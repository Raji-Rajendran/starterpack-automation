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


def generate_random_role():
    # Define patterns or rules for generating role names
    prefixes = ['Super', 'Admin', 'Manager', 'Agency', 'Employee', 'Supervisor', 'Team', 'Developer', 'Analyst',
                'Consultant', 'Coordinator', 'Specialist', 'Executive', 'Director', 'Project', 'Assistant', 'Associate',
                'Senior', 'Junior', 'Lead', 'Chief', 'Regional', 'National', 'Global', 'Product', 'Sales', 'Marketing',
                'Finance', 'Operations', 'Human Resources', 'Information Technology', 'Technical', 'Customer', 'Client',
                'Quality', 'Research', 'Data', 'Business', 'Strategic', 'Creative', 'Content', 'Public Relations',
                'Training', 'Customer Success', 'Account', 'Procurement', 'Supply Chain', 'Logistics', 'Warehouse',
                'Inventory', 'Purchasing', 'Risk', 'Compliance', 'Legal', 'Security', 'Health', 'Safety',
                'Environmental', 'Sustainability', 'Engineering', 'Architecture', 'Design', 'User Experience',
                'User Interface', 'Network', 'System', 'Cloud', 'Database', 'Web', 'Mobile', 'Frontend', 'Backend',
                'Fullstack', 'UI/UX', 'Software', 'Hardware', 'QA', 'Testing', 'Automation', 'Performance', 'Agile',
                'Scrum', 'Waterfall', 'DevOps', 'Cyber', 'Information', 'Technology', 'Productivity', 'Innovation',
                'Leadership', 'Management', 'Entrepreneur', 'Operations', 'Growth']
    suffixes = ['Admin', 'Manager', 'Employee', 'Supervisor', 'Lead', 'Developer', 'Analyst', 'Consultant',
                'Coordinator', 'Specialist', 'Executive', 'Director', 'Officer', 'Engineer', 'Architect', 'Designer',
                'Consulting', 'Operations', 'Analyst', 'Specialist', 'Expert', 'Advisor', 'Strategist', 'Planner',
                'Coordinator', 'Leader', 'Facilitator', 'Coach', 'Mentor', 'Guru', 'Evangelist', 'Champion', 'Pioneer',
                'Innovator', 'Trailblazer', 'Ambassador', 'Representative', 'Advocate', 'Agent', 'Broker', 'Trader',
                'Provider', 'Supplier', 'Vendor', 'Partner', 'Associate', 'Collaborator', 'Contributor', 'Member',
                'Participant', 'Supporter', 'Assistant', 'Aide', 'Counselor', 'Secretary', 'Administrator', 'Operator',
                'Technician', 'Expert', 'Professional', 'Master', 'Guru', 'Wizard', 'Ninja', 'Champion', 'Hero',
                'Legend', 'Rockstar', 'Maven', 'Whiz', 'Prodigy', 'Virtuoso', 'Maestro', 'Savant', 'Einstein',
                'Scholar', 'Genius', 'Pundit', 'Sage', 'Savvy', 'Savant', 'Prodigy', 'Expert', 'Whiz', 'Guru',
                'Maestro', 'Virtuoso', 'Scholar', 'Pundit', 'Sage', 'Einstein', 'Genius', 'Legend']

    # Randomly select a prefix and suffix and concatenate them
    prefix = random.choice(prefixes)
    suffix = random.choice(suffixes)
    return prefix + ' ' + suffix


class RolesConfig:
    # Generate and print a random role name
    role_name = generate_random_role()
    new_role_name = generate_random_role()

    admin_first_name = barnum.create_name()[0]
    admin_last_name = barnum.create_name()[1]
    admin_email = f"{admin_first_name}.{admin_last_name}@yopmail.com"
    admin_phone = randint(1000000000, 9999999999)

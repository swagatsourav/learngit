import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()
from first_app.models import Assigned_Role, Role_Master, User_Accounts, User_Master
from faker import Faker
import random
fake = Faker()
desingnations = ['Consultant', 'Supervisor', 'Operator', 'Architecht']



def populate_Data(n=5):
    for i in range(n):

        # Creates the initial entry in User_Accounts
        fake_first_name = fake.first_name()
        fake_user_name = fake_first_name + '_1234'
        while User_Accounts.objects.filter(user_name=fake_user_name).count() != 0:
            fake_first_name = fake.first_name()
            fake_user_name = fake_first_name + '_1234'

        fake_email_id = fake.email()
        while User_Accounts.objects.filter(email_id=fake_email_id).count() != 0:
            fake_email_id = fake.email()
        # picks a date between today and next 1 year.
        fake_pwd_exp_date = fake.date_between(
            start_date='today', end_date='+1y')
        pwd = "Swagat@123"
        ua_obj = User_Accounts(user_name=fake_user_name, password=pwd,email_id=fake_email_id, pwd_exp_date=fake_pwd_exp_date)
        ua_obj.save()
        print(f"User \"{fake_first_name}\" inserted.")
        # Create entry in User_Master
        fake_last_name = fake.last_name()
        ran_desingnation = random.choice(desingnations)
        # fake_dob = datetime.datetime(1992,7,18)
        fake_dob = fake.date_between(start_date='-30y', end_date='-18y')
        um_obj = User_Master(user_id=ua_obj, first_name=fake_first_name, last_name=fake_last_name,desingnation=ran_desingnation, dob=fake_dob, user_status='A', created_by=fake.name())
        um_obj.save()
        print(f"User \"{fake_first_name}\" master date inserted.")

populate_Data(3)

from first_app.models import Assigned_Role, Role_Master, User_Accounts, User_Master
from faker import Faker
import random
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')
django.setup()
fake = Faker()


def populate_Data(n=5):
    for i in range(n):
        # user_id = models.AutoField(primary_key=True)
        # user_name = models.CharField(unique=True, max_length=30)
        # password = models.CharField(max_length=20)
        # email_id = models.EmailField(max_length=80, unique=True)
        # pwd_exp_date = models.DateField()
    fake_user_name = fake.first_name() + '_1234'
    fake_email_id = fake.email()
    pwd_exp_date =
    User_Master.objects.create()


# FAKE POP SCRIPT

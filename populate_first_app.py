import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')
import django
django.setup()
from first_app.models import Assigned_Role, Role_Master, User_Accounts, User_Master
from faker import Faker
import random
fake = Faker()
desingnations = ['Consultant', 'Supervisor', 'Operator', 'Architecht']
roles = ['Operator', 'Sub-Operator', 'Supervisor', 'Manager','op-admin','Jr.operator']
role_details = {'Operator':'Machine-operator', 'Sub-Operator':'Asks Operator', 'Supervisor':'Observers Operator', 'Manager':'Manages Everything','op-admin':'Controls the system','Jr.operator':'Junior OPerator'}
from django.utils import timezone
from sys import argv


########### Create user details #############################
def populate_Data(n=2):
    print("\nCreating the users.\n-------------------")
    global value
    value = n
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



###### Creates Role details  #####################

print("\nCreating the roles.\n------------------------------")
rm_all=Role_Master.objects.all()
role_add = list(filter(lambda x:rm_all.filter(role_name=x).count() == 0, roles))
if len(role_add):
    for i in role_add:
        new_role_name = i
        new_role_details= role_details[i]
        rm_obj=Role_Master(role_name=new_role_name, role_details=new_role_details, role_status='A')
        rm_obj.save()
        print(f"Rule \"{new_role_name}\" inserted.")
else:
    print("No new roles found to be added.")

##### Creating the User_Accounts and the User_Master details.

try:
    val=argv[1]
    populate_Data(int(val))
    print(f"\nTotal {value} user's data inserted.")

except:
    populate_Data()
    print(f"\nTotal {value} user's data inserted.")





###### Assigning the roles to the users , users with no roles will be given two roles and users with one role will be given one role.
rm_all=Role_Master.objects.all()
um_all=User_Master.objects.all()
#finding the users who has role_asssigned i.e to select the users for which the roles assigned in Role_Master table ifmain assigned_users field via through table Assigned_Roles
um_have_roles=um_all.filter(role_master__in=rm_all)
#IN this db or may be in Django the above returns all as many users having roles assigned repeatedly. i.e if a user has two role it retuns same user twice.

# unique_um_have_roles=list(set(um_all.filter(role_master__in=Role_Master.objects.all())))

#Now let's count the no of users which are retuned once.
um_have_one_role=list(filter(lambda x:list(um_have_roles).count(x)==1,list(um_have_roles)))
#Below will provide the no of users for which no role is assigned.
um_have_no_role=um_all.filter(role_master=None)
roles_list=list(rm_all)

print("\nAssigning roles for users having no roles.\n-----------------------------------")
for i in um_have_no_role:
    # returns a list of any two different Role_master objects form role_list.
    roles_to_add=random.sample(roles_list,k=2)
    #setting these two roles to User_Master Element i via the through table .
    i.role_master_set.set(roles_to_add,through_defaults={'assignment_date':timezone.now(),'assignment_status':random.choice(['A','D'])})
    print(f'Assigned roles to user "{i}": {roles_to_add[0]}, {roles_to_add[1]}')

print("\nAssigning another role to users having only one role\n-----------------------------------")
if len(um_have_one_role):
    for i in um_have_one_role:

        roles_to_add=random.choice(list(set(roles_list) - set(i.role_master_set.all())))
        i.role_master_set.add(roles_to_add,through_defaults={'assignment_date':timezone.now(),'assignment_status':random.choice(['A','D'])})
        print(f'Assigned role to user "{i}": {roles_to_add}')
else:
    print("No such user's found.")




##################  END  #################

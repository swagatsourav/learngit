from django.db import models

# Create your models here.


class User_Accounts(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(unique=True, max_length=30)
    password = models.CharField(max_length=20)
    email_id = models.EmailField(max_length=80, unique=True)
    pwd_exp_date = models.DateField()

    def __str__(self):
        return str(self.user_name)


class User_Master(models.Model):
    user_id = models.OneToOneField(
        User_Accounts, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, null=True)
    desingnation = models.CharField(max_length=30, null=True)
    dob = models.DateField(verbose_name="Date of birth")
    user_status = models.CharField(max_length=1)
    creation_date = models.DateTimeField()
    created_by = models.CharField(max_length=30)
    expired_date = models.DateTimeField(null=True, blank=True)
    expired_by = models.CharField(max_length=30, null=True, blank=True)
    no_of_expiry = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.first_name


class Role_Master(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=30)
    role_details = models.CharField(max_length=30)
    role_status = models.CharField(max_length=1)
    assigned_users = models.ManyToManyField(
        User_Master, through='Assigned_Role')

    def __str__(self):
        return self.role_name


class Assigned_Role(models.Model):
    user_id = models.ForeignKey(
        User_Master, on_delete=models.CASCADE)
    role_id = models.ForeignKey(
        Role_Master, on_delete=models.CASCADE)
    assignment_date = models.DateTimeField()
    assignment_status = models.CharField(max_length=1)

    class Meta:
        unique_together = (("user_id", "role_id"),)

    def __str__(self):
        return str(self.role_id) + '------>' + str(self.user_id)

# Generated by Django 3.0.3 on 2020-05-04 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0020_auto_20200420_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role_master',
            name='assigned_users',
            field=models.ManyToManyField(
                through='first_app.Assigned_Role', to='first_app.User_Master'),
        ),
        migrations.AlterField(
            model_name='user_master',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

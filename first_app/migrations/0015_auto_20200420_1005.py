# Generated by Django 3.0.3 on 2020-04-20 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0014_auto_20200420_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role_master',
            name='assigned_users',
            field=models.ManyToManyField(through='first_app.Assigned_Role', to='first_app.User_Master'),
        ),
    ]

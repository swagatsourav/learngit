# Generated by Django 3.0.3 on 2020-05-04 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0026_auto_20200505_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role_master',
            name='assigned_users',
            field=models.ManyToManyField(through='first_app.Assigned_Role', to='first_app.User_Master'),
        ),
    ]

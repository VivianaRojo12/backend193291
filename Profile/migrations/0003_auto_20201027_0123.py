# Generated by Django 3.1.2 on 2020-10-27 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0002_profiletwo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profiletwo',
            old_name='user',
            new_name='profileModel',
        ),
    ]

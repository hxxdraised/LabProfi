# Generated by Django 4.2.5 on 2023-09-24 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_users', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
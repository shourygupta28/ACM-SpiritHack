# Generated by Django 3.0.7 on 2021-03-20 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_user_contact_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]

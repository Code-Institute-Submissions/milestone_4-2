# Generated by Django 3.0.8 on 2020-08-26 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_userprofile_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='user',
            new_name='username',
        ),
    ]
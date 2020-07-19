# Generated by Django 3.0.8 on 2020-07-19 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='total',
            new_name='order_total',
        ),
        migrations.AddField(
            model_name='order',
            name='full_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

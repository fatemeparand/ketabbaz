# Generated by Django 4.1.3 on 2023-01-04 12:51

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_order_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='phone number'),
        ),
    ]

# Generated by Django 4.1.3 on 2023-01-04 12:49

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_order_is_paid_alter_order_order_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, unique=True, verbose_name='phone number'),
        ),
    ]

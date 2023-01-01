# Generated by Django 4.1.3 on 2023-01-01 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_notes',
            field=models.CharField(blank=True, max_length=700, verbose_name='note'),
        ),
    ]

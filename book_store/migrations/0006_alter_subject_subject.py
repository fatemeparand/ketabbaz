# Generated by Django 4.1.3 on 2022-12-11 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_store', '0005_alter_book_publisher_alter_book_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='subject',
            field=models.CharField(max_length=200, verbose_name='subject'),
        ),
    ]

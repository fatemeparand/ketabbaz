# Generated by Django 4.1.3 on 2023-01-03 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_store', '0022_alter_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to='book_cover/', verbose_name='book image'),
        ),
    ]
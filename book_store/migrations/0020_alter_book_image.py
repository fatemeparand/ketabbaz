# Generated by Django 4.1.3 on 2022-12-24 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_store', '0019_alter_book_description_alter_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='book_cover/', verbose_name='book image'),
        ),
    ]

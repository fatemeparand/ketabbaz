# Generated by Django 4.1.3 on 2023-01-03 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_store', '0020_alter_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(default=1, upload_to='book_cover/', verbose_name='book image'),
            preserve_default=False,
        ),
    ]
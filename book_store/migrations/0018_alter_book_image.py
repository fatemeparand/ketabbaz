# Generated by Django 4.1.3 on 2022-12-23 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_store', '0017_comment_recommend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='book_cover/', verbose_name='book image'),
        ),
    ]

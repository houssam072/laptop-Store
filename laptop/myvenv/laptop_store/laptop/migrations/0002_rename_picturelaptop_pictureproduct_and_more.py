# Generated by Django 5.0.1 on 2024-01-20 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('laptop', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PictureLaptop',
            new_name='PictureProduct',
        ),
        migrations.RenameModel(
            old_name='Laptop',
            new_name='Product',
        ),
    ]

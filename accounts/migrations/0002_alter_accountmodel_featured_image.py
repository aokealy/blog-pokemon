# Generated by Django 3.2.20 on 2023-07-15 17:10

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountmodel',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='default.jpg', max_length=255),
        ),
    ]

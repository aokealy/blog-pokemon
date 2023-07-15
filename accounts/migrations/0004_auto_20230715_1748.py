# Generated by Django 3.2.20 on 2023-07-15 17:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_accountmodel_featured_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accountmodel',
            name='featured_image',
        ),
        migrations.AddField(
            model_name='accountmodel',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='account', validators=[django.core.validators.FileExtensionValidator(['jpg', 'png'])]),
        ),
    ]

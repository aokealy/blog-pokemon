# Generated by Django 3.2.20 on 2023-07-17 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_accountmodel_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accountmodel',
            name='image',
        ),
    ]

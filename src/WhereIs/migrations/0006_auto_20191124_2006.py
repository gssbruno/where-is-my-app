# Generated by Django 2.2.5 on 2019-11-24 22:06

import WhereIs.models._validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WhereIs', '0005_auto_20191124_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servidormodel',
            name='ip',
            field=models.CharField(max_length=16, unique=True, validators=[WhereIs.models._validators.validate_ip]),
        ),
    ]

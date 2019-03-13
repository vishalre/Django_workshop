# Generated by Django 2.0.1 on 2018-03-14 06:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challengica_app', '0003_auto_20180314_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='contestant',
            name='year',
            field=models.IntegerField(default=None, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]
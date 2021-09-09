# Generated by Django 3.2.5 on 2021-08-29 16:06

import dealer.cars.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0014_alter_car_view_for_statistic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='view_for_statistic',
            field=models.JSONField(blank=True, default=dealer.cars.models.get_default_view_statistic, null=True),
        ),
    ]

# Generated by Django 3.0.1 on 2020-03-08 15:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0028_auto_20200222_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='reservation_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 8, 16, 12, 59, 801958)),
        ),
    ]

# Generated by Django 3.0.4 on 2020-04-05 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0046_auto_20200404_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='thumbnail',
            field=models.ImageField(default='', upload_to='media'),
        ),
    ]
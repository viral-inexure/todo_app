# Generated by Django 3.2.6 on 2021-09-03 07:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo_app', '0010_auto_20210903_0710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 3, 7, 24, 6, 251399)),
        ),
        migrations.AlterField(
            model_name='todo',
            name='deadline_time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 9, 3, 7, 24, 6, 251399)),
        ),
    ]
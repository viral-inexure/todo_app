# Generated by Django 3.2.6 on 2021-09-05 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo_app', '0014_alter_user_mobile_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='deadline_time',
            field=models.DateTimeField(),
        ),
    ]

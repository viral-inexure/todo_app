# Generated by Django 3.2.6 on 2021-09-01 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo_app', '0004_auto_20210901_0459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='create_time',
            field=models.DateTimeField(verbose_name='2021-09-01T16.58'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='deadline_time',
            field=models.DateTimeField(verbose_name='2021-09-01T16.58'),
        ),
    ]
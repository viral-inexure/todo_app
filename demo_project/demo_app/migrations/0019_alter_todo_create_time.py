# Generated by Django 3.2.6 on 2021-09-06 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo_app', '0018_alter_todo_update_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='create_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
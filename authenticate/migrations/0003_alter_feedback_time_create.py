# Generated by Django 4.1.3 on 2022-11-20 11:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0002_feedback_time_create_alter_feedback_messages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='time_create',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 20, 18, 8, 15, 379561)),
        ),
    ]

# Generated by Django 3.0.4 on 2020-03-26 01:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200326_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 26, 1, 54, 16, 287831, tzinfo=utc)),
        ),
    ]

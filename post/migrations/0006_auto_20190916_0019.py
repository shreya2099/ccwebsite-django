# Generated by Django 2.2.3 on 2019-09-15 18:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20190916_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_on_date',
            field=models.DateField(default=datetime.datetime(2019, 9, 15, 18, 49, 28, 469668, tzinfo=utc)),
        ),
    ]

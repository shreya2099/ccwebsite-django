# Generated by Django 2.2.3 on 2019-09-13 11:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20190913_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_on_date',
            field=models.DateField(default=datetime.datetime(2019, 9, 13, 11, 33, 37, 280117, tzinfo=utc)),
        ),
    ]

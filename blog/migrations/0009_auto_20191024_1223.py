# Generated by Django 2.2.6 on 2019-10-24 10:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20191024_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posta',
            name='sortutako_data',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 24, 10, 23, 30, 379149, tzinfo=utc)),
        ),
    ]

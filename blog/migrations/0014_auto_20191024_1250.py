# Generated by Django 2.2.6 on 2019-10-24 10:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20191024_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posta',
            name='sortutako_data',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 24, 10, 50, 36, 982352, tzinfo=utc)),
        ),
    ]

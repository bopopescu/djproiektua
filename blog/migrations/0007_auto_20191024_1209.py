# Generated by Django 2.2.6 on 2019-10-24 10:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20191024_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posta',
            name='sortutako_data',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 24, 10, 9, 56, 840698, tzinfo=utc)),
        ),
    ]
# Generated by Django 2.2.6 on 2019-11-06 09:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20191024_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posta',
            name='image',
            field=models.FileField(null=True, upload_to='img', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='posta',
            name='sortutako_data',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 6, 9, 45, 29, 519308, tzinfo=utc)),
        ),
    ]
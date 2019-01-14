# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-12 18:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [("forum", "0009_auto_20180108_1841")]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="date_created",
            field=models.DateTimeField(
                verbose_name=datetime.datetime(
                    2018, 1, 12, 18, 20, 28, 300989, tzinfo=utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="date_created",
            field=models.DateTimeField(
                verbose_name=datetime.datetime(
                    2018, 1, 12, 18, 20, 28, 299333, tzinfo=utc
                )
            ),
        ),
    ]

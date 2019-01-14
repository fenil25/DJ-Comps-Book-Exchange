# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-06 11:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [("forum", "0005_auto_20180106_1717")]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="date_created",
            field=models.DateTimeField(
                verbose_name=datetime.datetime(
                    2018, 1, 6, 11, 49, 14, 679088, tzinfo=utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="date_created",
            field=models.DateTimeField(
                verbose_name=datetime.datetime(
                    2018, 1, 6, 11, 49, 14, 679088, tzinfo=utc
                )
            ),
        ),
    ]

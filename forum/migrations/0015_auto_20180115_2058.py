# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-15 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("forum", "0014_auto_20180113_2204")]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="date_created",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="date_created",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

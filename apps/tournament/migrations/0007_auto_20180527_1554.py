# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-27 20:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0006_auto_20180527_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='kind',
            field=models.CharField(max_length=20),
        ),
    ]

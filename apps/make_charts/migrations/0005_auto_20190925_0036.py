# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-09-25 00:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('make_charts', '0004_auto_20190925_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='strategy',
            name='points_of_failure',
            field=models.ManyToManyField(related_name='strategies', to='make_charts.Fail'),
        ),
    ]

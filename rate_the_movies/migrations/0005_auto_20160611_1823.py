# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-11 18:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rate_the_movies', '0004_auto_20160611_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topmovie',
            name='avg_rating',
            field=models.FloatField(),
        ),
    ]

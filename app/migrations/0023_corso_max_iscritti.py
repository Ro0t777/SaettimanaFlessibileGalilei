# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-03 13:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_iscrizione_aule'),
    ]

    operations = [
        migrations.AddField(
            model_name='corso',
            name='max_iscritti',
            field=models.IntegerField(default=0),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 06:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20171031_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='iscrizione',
            name='corso',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.Corso'),
        ),
    ]

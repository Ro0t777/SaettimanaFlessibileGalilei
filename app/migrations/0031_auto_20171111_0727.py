# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-11 07:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_auto_20171108_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='corso',
            name='f9',
        ),
        migrations.RemoveField(
            model_name='iscrizione',
            name='corso9',
        ),
    ]

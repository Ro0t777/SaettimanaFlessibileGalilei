# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 15:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20171101_1539'),
    ]

    operations = [
        migrations.RenameField(
            model_name='corso',
            old_name='ripetuto',
            new_name='progressivo',
        ),
    ]
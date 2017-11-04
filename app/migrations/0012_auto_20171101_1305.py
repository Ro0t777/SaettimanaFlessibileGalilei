# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 13:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20171101_1010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='iscrizione',
            name='lunedi1',
        ),
        migrations.RemoveField(
            model_name='iscrizione',
            name='lunedi2',
        ),
        migrations.RemoveField(
            model_name='iscrizione',
            name='lunedi3',
        ),
        migrations.RemoveField(
            model_name='iscrizione',
            name='martedi1',
        ),
        migrations.RemoveField(
            model_name='iscrizione',
            name='martedi2',
        ),
        migrations.RemoveField(
            model_name='iscrizione',
            name='martedi3',
        ),
        migrations.RemoveField(
            model_name='iscrizione',
            name='mercoledi1',
        ),
        migrations.RemoveField(
            model_name='iscrizione',
            name='mercoledi2',
        ),
        migrations.RemoveField(
            model_name='iscrizione',
            name='mercoledi3',
        ),
        migrations.AddField(
            model_name='iscrizione',
            name='fascie',
            field=models.ManyToManyField(to='app.Fascia'),
        ),
    ]

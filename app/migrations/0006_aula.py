# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 18:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20171030_2036'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aule', models.CharField(max_length=100)),
            ],
        ),
    ]
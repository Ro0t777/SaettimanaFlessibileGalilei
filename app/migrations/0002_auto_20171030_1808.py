# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 18:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fascia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ripetuto', models.BooleanField(default=False)),
                ('lunedi1', models.BooleanField(default=False)),
                ('lunedi2', models.BooleanField(default=False)),
                ('lunedi3', models.BooleanField(default=False)),
                ('martedi1', models.BooleanField(default=False)),
                ('martedi2', models.BooleanField(default=False)),
                ('martedi3', models.BooleanField(default=False)),
                ('mercoledi1', models.BooleanField(default=False)),
                ('mercoledi2', models.BooleanField(default=False)),
                ('mercoledi3', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Iscrizione',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='corso',
            name='lunedi1',
        ),
        migrations.RemoveField(
            model_name='corso',
            name='lunedi2',
        ),
        migrations.RemoveField(
            model_name='corso',
            name='lunedi3',
        ),
        migrations.RemoveField(
            model_name='corso',
            name='martedi1',
        ),
        migrations.RemoveField(
            model_name='corso',
            name='martedi2',
        ),
        migrations.RemoveField(
            model_name='corso',
            name='martedi3',
        ),
        migrations.RemoveField(
            model_name='corso',
            name='mercoledi1',
        ),
        migrations.RemoveField(
            model_name='corso',
            name='mercoledi2',
        ),
        migrations.RemoveField(
            model_name='corso',
            name='mercoledi3',
        ),
        migrations.RemoveField(
            model_name='corso',
            name='ripetuto',
        ),
        migrations.AddField(
            model_name='fascia',
            name='corso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Corso'),
        ),
    ]

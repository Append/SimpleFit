# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-11 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0042_auto_20161211_1322'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllExercises',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=30)),
            ],
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-11 02:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_auto_20161211_0108'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientprofile',
            name='dietitianpending',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dietitianpending', to='api.DietitianProfile'),
        ),
        migrations.AlterField(
            model_name='clientprofile',
            name='dietitian',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dietitian', to='api.DietitianProfile'),
        ),
    ]

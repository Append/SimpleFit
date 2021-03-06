# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-30 05:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0015_auto_20161130_0449'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientprofile',
            name='service',
        ),
        migrations.RemoveField(
            model_name='clientprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='dietitianprofile',
            name='service',
        ),
        migrations.RemoveField(
            model_name='dietitianprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='trainerprofile',
            name='service',
        ),
        migrations.RemoveField(
            model_name='trainerprofile',
            name='user',
        ),
        migrations.AddField(
            model_name='basicprofile',
            name='member_type',
            field=models.CharField(choices=[('trainer', 'trainer'), ('dietitian', 'dietitian'), ('client', 'client')], default='client', max_length=30),
        ),
        migrations.AddField(
            model_name='basicprofile',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

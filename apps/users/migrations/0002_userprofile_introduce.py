# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-16 09:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='introduce',
            field=models.TextField(default='', verbose_name='\u4e2a\u4eba\u4ecb\u7ecd'),
        ),
    ]
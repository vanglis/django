# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-28 14:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['update_time'], 'verbose_name': '部署php环境', 'verbose_name_plural': '部署php环境'},
        ),
    ]
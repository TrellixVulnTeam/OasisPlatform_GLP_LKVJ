# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-05 12:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_files', '0004_remove_datafile_linked_models'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datafile',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='datafile',
            name='filename',
        ),
    ]

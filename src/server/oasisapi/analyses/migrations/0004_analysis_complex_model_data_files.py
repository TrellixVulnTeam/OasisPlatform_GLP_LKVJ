# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-07-04 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_files', '0002_auto_20190704_1403'),
        ('analyses', '0003_auto_20190625_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysis',
            name='complex_model_data_files',
            field=models.ManyToManyField(blank=True, related_name='complex_model_files_analyses', to='data_files.DataFile'),
        ),
    ]

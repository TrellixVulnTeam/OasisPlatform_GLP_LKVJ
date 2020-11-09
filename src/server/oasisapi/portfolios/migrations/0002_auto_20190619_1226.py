# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-19 12:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0002_auto_20190109_1715'),
        ('portfolios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='reinsurance_source_file',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='reinsurance_scope_file',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reinsurance_scope_file_portfolios', to='files.RelatedFile'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-07-22 18:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20160607_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='documentation',
            field=models.URLField(blank=True, null=True),
        ),
    ]

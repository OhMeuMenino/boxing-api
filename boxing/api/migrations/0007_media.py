# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-06-03 22:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20160603_2109'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('path', models.FileField(upload_to='%Y/%m/%d/')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-11 18:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iFood', '0002_auto_20190311_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dishes',
            name='name',
            field=models.CharField(max_length=128),
        ),
    ]

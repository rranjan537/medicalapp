# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-06 05:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AvayaApp', '0008_auto_20170506_0452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='Password',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='patient',
            name='UserName',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
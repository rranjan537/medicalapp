# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 08:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AvayaApp', '0003_auto_20170505_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='Password',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='UserName',
            field=models.CharField(max_length=250),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 10:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AvayaApp', '0004_auto_20170505_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='HospitalId',
            field=models.TextField(null=True),
        ),
    ]

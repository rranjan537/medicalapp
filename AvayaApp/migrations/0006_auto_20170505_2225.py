# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-05 22:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AvayaApp', '0005_auto_20170505_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='Age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='HospitalId',
            field=models.TextField(blank=True, null=True),
        ),
    ]

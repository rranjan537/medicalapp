# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 13:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AvayaApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='Age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='AgeGroup',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='UID',
            field=models.BigIntegerField(max_length=12, unique=True),
        ),
    ]

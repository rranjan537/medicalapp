# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-06 08:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AvayaApp', '0011_hospital_specialization'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='Distance',
            field=models.IntegerField(null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-14 18:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracao', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagefile',
            name='message_id',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]

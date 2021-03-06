# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-21 20:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administracao', '0003_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_id', models.IntegerField(blank=True, null=True, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='messagefile',
            name='message_id',
        ),
        migrations.AddField(
            model_name='message',
            name='message_file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracao.MessageFile'),
        ),
    ]

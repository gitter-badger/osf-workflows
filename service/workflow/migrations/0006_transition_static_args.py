# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-12 14:18
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0005_arc_net'),
    ]

    operations = [
        migrations.AddField(
            model_name='transition',
            name='static_args',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]
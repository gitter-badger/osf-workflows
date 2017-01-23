# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-20 22:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='context',
            name='inherit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='heirs', to='workflow.Context'),
        ),
        migrations.AlterField(
            model_name='context',
            name='workflows',
            field=models.ManyToManyField(blank=True, related_name='ctxs', to='workflow.Workflow'),
        ),
    ]
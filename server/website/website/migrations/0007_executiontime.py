# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-24 00:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_session_hyperparameters'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExecutionTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module', models.CharField(max_length=32)),
                ('function', models.CharField(max_length=32)),
                ('tag', models.CharField(blank=True, default='', max_length=64)),
                ('start_time', models.DateTimeField()),
                ('execution_time', models.FloatField()),
                ('result', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.Result')),
            ],
        ),
    ]

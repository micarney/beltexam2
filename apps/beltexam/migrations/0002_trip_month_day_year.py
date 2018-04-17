# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-17 17:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('beltexam', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='month_day_year',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='%m %d %Y'),
            preserve_default=False,
        ),
    ]

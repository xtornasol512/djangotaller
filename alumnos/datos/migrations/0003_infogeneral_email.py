# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-11 19:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datos', '0002_infogeneral_estatura'),
    ]

    operations = [
        migrations.AddField(
            model_name='infogeneral',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
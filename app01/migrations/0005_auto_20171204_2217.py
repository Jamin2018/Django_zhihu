# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 14:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='user',
            new_name='u',
        ),
    ]

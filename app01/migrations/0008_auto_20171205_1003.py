# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 02:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0007_auto_20171205_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='p',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app01.Post'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='u',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app01.User'),
        ),
    ]

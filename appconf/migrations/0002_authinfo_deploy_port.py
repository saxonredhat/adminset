# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-27 02:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appconf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authinfo',
            name='deploy_port',
            field=models.IntegerField(default=22, verbose_name='\u7aef\u53e3'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-07 19:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extuser', '0005_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-07 22:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('extuser', '0006_remove_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='represent',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

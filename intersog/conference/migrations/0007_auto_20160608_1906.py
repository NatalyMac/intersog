# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-08 19:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0006_auto_20160608_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='representer',
            name='representer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='\u041f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u0438\u0442\u0435\u043b\u044c'),
        ),
    ]

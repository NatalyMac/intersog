# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-08 11:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extuser', '0009_auto_20160608_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('member', '\u0423\u0447\u0430\u0441\u0442\u043d\u0438\u043a'), ('sponsor', '\u0421\u043f\u043e\u043d\u043e\u0441\u043e\u0440')], default='member', max_length=15, verbose_name='\u0420\u043e\u043b\u044c'),
        ),
    ]

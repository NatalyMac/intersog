# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-08 18:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('conference', '0005_auto_20160608_1820'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='memberconference',
            options={'verbose_name': '\u0423\u0447\u0430\u0441\u0442\u043d\u0438\u043a \u043a\u043e\u043d\u0444\u0435\u0440\u0435\u043d\u0446\u0438\u0438', 'verbose_name_plural': '\u0423\u0447\u0430\u0441\u0442\u043d\u0438\u043a\u0438 \u043a\u043e\u043d\u0444\u0435\u0440\u0435\u043d\u0446\u0438\u0438'},
        ),
        migrations.AlterModelOptions(
            name='representer',
            options={'verbose_name': '\u041f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u0438\u0442\u0435\u043b\u044c \u0441\u043f\u043e\u043d\u0441\u043e\u0440\u0430', 'verbose_name_plural': '\u041f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u0438\u0442\u0435\u043b\u0438 \u0441\u043f\u043e\u043d\u0441\u043e\u0440\u0430'},
        ),
        migrations.RemoveField(
            model_name='representer',
            name='representer',
        ),
        migrations.AddField(
            model_name='representer',
            name='representer',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u041f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u0438\u0442\u0435\u043b\u044c'),
            preserve_default=False,
        ),
    ]

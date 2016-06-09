# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-07 22:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('conference', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Representer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('representer', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='\u041f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u0438\u0442\u0435\u043b\u044c')),
            ],
        ),
    ]

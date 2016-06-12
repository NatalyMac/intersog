# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-10 12:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import swampdragon.models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('done', models.BooleanField(default=False)),
                ('text', models.CharField(max_length=100)),
            ],
            bases=(swampdragon.models.SelfPublishModel, models.Model),
        ),
        migrations.CreateModel(
            name='ChatList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            bases=(swampdragon.models.SelfPublishModel, models.Model),
        ),
        migrations.AddField(
            model_name='chatitem',
            name='chat_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.ChatList'),
        ),
    ]
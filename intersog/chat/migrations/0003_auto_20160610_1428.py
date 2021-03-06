# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-10 14:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import swampdragon.models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20160610_1221'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('done', models.BooleanField(default=False)),
                ('text', models.CharField(max_length=100)),
            ],
            bases=(swampdragon.models.SelfPublishModel, models.Model),
        ),
        migrations.RenameModel(
            old_name='ChatList',
            new_name='TodoList',
        ),
        migrations.RemoveField(
            model_name='chatitem',
            name='chat_list',
        ),
        migrations.DeleteModel(
            name='ChatItem',
        ),
        migrations.AddField(
            model_name='todoitem',
            name='todo_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.TodoList'),
        ),
    ]

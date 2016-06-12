# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20160610_1428'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todoitem',
            name='todo_list',
        ),
        migrations.DeleteModel(
            name='TodoItem',
        ),
        migrations.DeleteModel(
            name='TodoList',
        ),
    ]

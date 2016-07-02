# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbt', '0046_auto_20160622_0350'),
    ]

    operations = [
        migrations.AddField(
            model_name='search_activity',
            name='based_on_album',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='search_activity',
            name='based_on_producer',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='search_activity',
            name='based_on_song',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='search_activity',
            name='is_result_empty',
            field=models.BooleanField(default=False),
        ),
    ]

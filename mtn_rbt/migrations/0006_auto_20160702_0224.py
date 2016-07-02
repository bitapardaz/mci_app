# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mtn_rbt', '0005_mtn_search_activity'),
    ]

    operations = [
        migrations.AddField(
            model_name='mtn_search_activity',
            name='based_on_album',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='mtn_search_activity',
            name='based_on_producer',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='mtn_search_activity',
            name='based_on_song',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='mtn_search_activity',
            name='location',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='mtn_search_activity',
            name='mobile_number',
            field=models.CharField(default=0, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='mtn_search_activity',
            name='result_has_album',
            field=models.NullBooleanField(default=False),
        ),
    ]

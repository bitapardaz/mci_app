# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbt', '0050_auto_20160701_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search_activity',
            name='based_on_album',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='search_activity',
            name='based_on_producer',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='search_activity',
            name='based_on_song',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='search_activity',
            name='mobile_number',
            field=models.CharField(default=0, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='search_activity',
            name='result_has_album',
            field=models.NullBooleanField(default=False),
        ),
    ]

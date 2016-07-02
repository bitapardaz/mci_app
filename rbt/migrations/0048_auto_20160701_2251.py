# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbt', '0047_auto_20160701_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='search_activity',
            name='location',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='search_activity',
            name='mobile_number',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]

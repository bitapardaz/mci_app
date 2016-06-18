# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rbt', '0039_search_activity'),
    ]

    operations = [
        migrations.AddField(
            model_name='search_activity',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 18, 6, 38, 5, 70504, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]

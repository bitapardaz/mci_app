# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rbt', '0009_auto_20160221_0727'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 21, 14, 38, 34, 713533, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]

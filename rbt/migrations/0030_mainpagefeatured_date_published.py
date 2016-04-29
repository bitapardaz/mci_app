# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rbt', '0029_mainpagefeatured'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainpagefeatured',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 29, 6, 1, 7, 635179, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]

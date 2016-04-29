# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rbt', '0034_category_featured_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='category_featured',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 29, 10, 25, 23, 250509, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]

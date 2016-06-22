# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mtn_rbt', '0003_auto_20160622_0259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mtn_album',
            name='pseudo_producer',
        ),
    ]

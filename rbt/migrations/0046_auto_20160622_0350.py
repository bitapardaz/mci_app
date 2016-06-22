# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbt', '0045_auto_20160620_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='download_link',
            field=models.URLField(max_length=500),
        ),
    ]

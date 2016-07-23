# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('download_center', '0009_auto_20160722_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='download_link',
            field=models.URLField(max_length=500, null=True, blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbt', '0019_auto_20160327_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='category',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='producer',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
    ]

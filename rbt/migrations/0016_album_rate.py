# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbt', '0015_song_confirmed'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='rate',
            field=models.IntegerField(default=0),
        ),
    ]

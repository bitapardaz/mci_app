# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbt', '0014_song_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
    ]

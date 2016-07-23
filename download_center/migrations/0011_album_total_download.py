# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('download_center', '0010_track_download_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='total_download',
            field=models.IntegerField(default=0),
        ),
    ]

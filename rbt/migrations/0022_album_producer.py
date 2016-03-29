# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbt', '0021_album_wide_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='producer',
            field=models.ForeignKey(blank=True, to='rbt.Producer', null=True),
        ),
    ]

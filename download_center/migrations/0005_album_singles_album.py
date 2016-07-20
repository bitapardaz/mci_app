# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('download_center', '0004_remove_singer_singles_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='singles_album',
            field=models.OneToOneField(null=True, blank=True, to='download_center.Singer'),
        ),
    ]

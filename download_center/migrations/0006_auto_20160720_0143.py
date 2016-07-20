# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('download_center', '0005_album_singles_album'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='singles_album',
            new_name='singer',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0018_auto_20160630_0238'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='track',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='track',
            name='album',
        ),
        migrations.DeleteModel(
            name='AlbumTest',
        ),
        migrations.DeleteModel(
            name='Track',
        ),
    ]

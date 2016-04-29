# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbt', '0033_remove_category_featured_song'),
    ]

    operations = [
        migrations.AddField(
            model_name='category_featured',
            name='album',
            field=models.ForeignKey(default=None, to='rbt.Album'),
            preserve_default=False,
        ),
    ]

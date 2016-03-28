# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbt', '0017_remove_song_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='date_published',
        ),
        migrations.AddField(
            model_name='album',
            name='category',
            field=models.ForeignKey(blank=True, to='rbt.Category', null=True),
        ),
        migrations.AddField(
            model_name='album',
            name='date_published',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]

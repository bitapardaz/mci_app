# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbt', '0004_song_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='category',
            field=models.ForeignKey(to='rbt.Category'),
        ),
    ]

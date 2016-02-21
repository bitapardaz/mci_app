# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbt', '0008_auto_20160215_0057'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='farsi_title',
            field=models.CharField(default='farsi_title', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
    ]

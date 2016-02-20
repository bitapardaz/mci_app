# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_auto_20160215_0057'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='imei',
            field=models.CharField(default='imei_default', max_length=32),
            preserve_default=False,
        ),
    ]

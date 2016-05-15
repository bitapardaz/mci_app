# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbt', '0036_auto_20160501_0100'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'ordering': ['farsi_name']},
        ),
    ]

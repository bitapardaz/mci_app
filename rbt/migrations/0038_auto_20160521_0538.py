# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbt', '0037_auto_20160515_0004'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producer',
            options={'ordering': ['name']},
        ),
    ]

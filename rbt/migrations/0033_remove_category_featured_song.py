# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbt', '0032_auto_20160429_0451'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category_featured',
            name='song',
        ),
    ]

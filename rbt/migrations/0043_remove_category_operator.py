# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbt', '0042_category_operator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='operator',
        ),
    ]

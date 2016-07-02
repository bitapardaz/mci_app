# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbt', '0048_auto_20160701_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search_activity',
            name='mobile_number',
            field=models.CharField(default=0, max_length=20),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbt', '0018_auto_20160327_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='category',
            field=models.ForeignKey(to='rbt.Category'),
        ),
        migrations.AlterField(
            model_name='album',
            name='date_published',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbt', '0003_auto_20160213_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='category',
            field=models.ForeignKey(to='rbt.Category', null=True),
        ),
    ]

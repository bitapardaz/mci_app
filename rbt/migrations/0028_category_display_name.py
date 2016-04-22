# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbt', '0027_category_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='display_name',
            field=models.CharField(default='display_name', max_length=200),
            preserve_default=False,
        ),
    ]

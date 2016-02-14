# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbt', '0006_category_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]

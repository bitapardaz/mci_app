# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbt', '0035_category_featured_date_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catadvert',
            name='album',
            field=models.ForeignKey(blank=True, to='rbt.Album', null=True),
        ),
        migrations.AlterField(
            model_name='catadvert',
            name='category',
            field=models.ForeignKey(blank=True, to='rbt.Category', null=True),
        ),
    ]

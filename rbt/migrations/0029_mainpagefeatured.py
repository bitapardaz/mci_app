# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbt', '0028_category_display_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainPageFeatured',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('album', models.ForeignKey(to='rbt.Album')),
            ],
        ),
    ]

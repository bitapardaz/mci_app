# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbt', '0023_auto_20160329_1135'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatAdvert',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('album', models.ForeignKey(to='rbt.Album')),
                ('category', models.ForeignKey(to='rbt.Category')),
            ],
        ),
    ]

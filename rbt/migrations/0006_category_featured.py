# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbt', '0005_auto_20160213_2113'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category_Featured',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.ForeignKey(to='rbt.Category')),
                ('song', models.ForeignKey(to='rbt.Song')),
            ],
        ),
    ]

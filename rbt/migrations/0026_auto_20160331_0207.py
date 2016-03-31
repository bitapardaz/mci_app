# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbt', '0025_mainadverts'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainAdvert',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('miscellaneous', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('url', models.URLField(null=True, blank=True)),
                ('album', models.ForeignKey(blank=True, to='rbt.Album', null=True)),
                ('category', models.ForeignKey(blank=True, to='rbt.Category', null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='mainadverts',
            name='album',
        ),
        migrations.RemoveField(
            model_name='mainadverts',
            name='category',
        ),
        migrations.DeleteModel(
            name='MainAdverts',
        ),
    ]

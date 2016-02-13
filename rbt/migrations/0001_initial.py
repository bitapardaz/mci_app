# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('song_name', models.CharField(default=b'name', max_length=200)),
                ('activation_code', models.IntegerField(default=0)),
                ('download_link', models.URLField(max_length=400)),
                ('rate', models.IntegerField(default=0)),
                ('activated', models.IntegerField(default=0)),
                ('producer', models.ForeignKey(blank=True, to='rbt.Producer', null=True)),
            ],
        ),
    ]

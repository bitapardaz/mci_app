# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mtn_rbt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MTN_MusicStudio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='mtn_song',
            name='tone_id',
            field=models.CharField(default=b'id', max_length=20),
        ),
        migrations.AddField(
            model_name='mtn_album',
            name='music_studio',
            field=models.ForeignKey(blank=True, to='mtn_rbt.MTN_MusicStudio', null=True),
        ),
        migrations.AddField(
            model_name='mtn_song',
            name='music_studio',
            field=models.ForeignKey(blank=True, to='mtn_rbt.MTN_MusicStudio', null=True),
        ),
    ]

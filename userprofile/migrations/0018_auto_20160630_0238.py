# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0017_auto_20160630_0236'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('album_name', models.CharField(max_length=100)),
                ('artist', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('duration', models.IntegerField()),
                ('album', models.ForeignKey(related_name='tracks', to='userprofile.AlbumTest')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='track',
            unique_together=set([('album', 'order')]),
        ),
    ]

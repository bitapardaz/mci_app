# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('download_center', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainAdvert',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('miscellaneous', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('url', models.URLField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='MusicStudio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'name', max_length=200)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='TopChart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='banner_image',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AddField(
            model_name='album',
            name='date_published',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='album',
            name='dj_image',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AddField(
            model_name='album',
            name='expert_opinion',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='album',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AddField(
            model_name='album',
            name='title',
            field=models.CharField(default=b'title', max_length=100),
        ),
        migrations.AddField(
            model_name='album',
            name='view',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='singer',
            name='image',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AddField(
            model_name='singer',
            name='name',
            field=models.CharField(default=b'name', max_length=100),
        ),
        migrations.AddField(
            model_name='singer',
            name='singles_album',
            field=models.OneToOneField(null=True, to='download_center.Album'),
        ),
        migrations.AddField(
            model_name='track',
            name='album',
            field=models.ManyToManyField(to='download_center.Album'),
        ),
        migrations.AddField(
            model_name='track',
            name='date_published',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='track',
            name='downloaded',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='track',
            name='liked',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='track',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AddField(
            model_name='track',
            name='played',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='track',
            name='wide_photo',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AddField(
            model_name='topchart',
            name='album',
            field=models.ForeignKey(to='download_center.Album'),
        ),
        migrations.AddField(
            model_name='mainadvert',
            name='album',
            field=models.ForeignKey(blank=True, to='download_center.Album', null=True),
        ),
        migrations.AddField(
            model_name='track',
            name='music_studio',
            field=models.ForeignKey(to='download_center.MusicStudio', null=True),
        ),
    ]

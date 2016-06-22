# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbt', '0043_remove_category_operator'),
    ]

    operations = [
        migrations.CreateModel(
            name='MTN_Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('farsi_name', models.CharField(max_length=200)),
                ('english_name', models.CharField(max_length=200, null=True, blank=True)),
                ('photo', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('wide_photo', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('rate', models.IntegerField(default=0)),
                ('date_published', models.DateTimeField(auto_now=True)),
                ('confirmed', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['farsi_name'],
            },
        ),
        migrations.CreateModel(
            name='MTN_CatAdvert',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('miscellaneous', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('url', models.URLField(null=True, blank=True)),
                ('album', models.ForeignKey(blank=True, to='rbt.MTN_Album', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MTN_Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('farsi_name', models.CharField(max_length=200)),
                ('display_name', models.CharField(max_length=200)),
                ('english_name', models.CharField(max_length=200, null=True, blank=True)),
                ('photo', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('confirmed', models.BooleanField(default=False)),
                ('parent', models.ForeignKey(blank=True, to='rbt.MTN_Category', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MTN_Category_Featured',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_published', models.DateTimeField(auto_now=True)),
                ('album', models.ForeignKey(to='rbt.MTN_Album')),
                ('category', models.ForeignKey(to='rbt.MTN_Category')),
            ],
        ),
        migrations.CreateModel(
            name='MTN_MainAdvert',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('miscellaneous', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('url', models.URLField(null=True, blank=True)),
                ('album', models.ForeignKey(blank=True, to='rbt.MTN_Album', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MTN_MainPageFeatured',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_published', models.DateTimeField(auto_now=True)),
                ('album', models.ForeignKey(to='rbt.MTN_Album')),
            ],
        ),
        migrations.CreateModel(
            name='MTN_Song',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('song_name', models.CharField(default=b'name', max_length=200)),
                ('activation_code', models.IntegerField(default=0)),
                ('download_link', models.URLField(max_length=400)),
                ('rate', models.IntegerField(default=0)),
                ('activated', models.IntegerField(default=0)),
                ('image', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('price', models.IntegerField(default=300)),
                ('confirmed', models.BooleanField(default=False)),
                ('album', models.ForeignKey(blank=True, to='rbt.MTN_Album', null=True)),
                ('producer', models.ForeignKey(blank=True, to='rbt.Producer', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MTN_SongTagAssociation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('song', models.ForeignKey(to='rbt.MTN_Song')),
                ('tag', models.ForeignKey(to='rbt.Tag')),
            ],
        ),
        migrations.AddField(
            model_name='mtn_catadvert',
            name='category',
            field=models.ForeignKey(blank=True, to='rbt.MTN_Category', null=True),
        ),
        migrations.AddField(
            model_name='mtn_album',
            name='category',
            field=models.ForeignKey(to='rbt.MTN_Category'),
        ),
        migrations.AddField(
            model_name='mtn_album',
            name='producer',
            field=models.ForeignKey(blank=True, to='rbt.Producer', null=True),
        ),
        migrations.AddField(
            model_name='mtn_album',
            name='pseudo_producer',
            field=models.ForeignKey(blank=True, to='rbt.PseudoProducer', null=True),
        ),
    ]

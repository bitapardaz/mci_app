# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbt', '0044_auto_20160620_0310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mtn_album',
            name='category',
        ),
        migrations.RemoveField(
            model_name='mtn_album',
            name='producer',
        ),
        migrations.RemoveField(
            model_name='mtn_album',
            name='pseudo_producer',
        ),
        migrations.RemoveField(
            model_name='mtn_catadvert',
            name='album',
        ),
        migrations.RemoveField(
            model_name='mtn_catadvert',
            name='category',
        ),
        migrations.RemoveField(
            model_name='mtn_category',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='mtn_category_featured',
            name='album',
        ),
        migrations.RemoveField(
            model_name='mtn_category_featured',
            name='category',
        ),
        migrations.RemoveField(
            model_name='mtn_mainadvert',
            name='album',
        ),
        migrations.RemoveField(
            model_name='mtn_mainpagefeatured',
            name='album',
        ),
        migrations.RemoveField(
            model_name='mtn_song',
            name='album',
        ),
        migrations.RemoveField(
            model_name='mtn_song',
            name='producer',
        ),
        migrations.RemoveField(
            model_name='mtn_songtagassociation',
            name='song',
        ),
        migrations.RemoveField(
            model_name='mtn_songtagassociation',
            name='tag',
        ),
        migrations.DeleteModel(
            name='MTN_Album',
        ),
        migrations.DeleteModel(
            name='MTN_CatAdvert',
        ),
        migrations.DeleteModel(
            name='MTN_Category',
        ),
        migrations.DeleteModel(
            name='MTN_Category_Featured',
        ),
        migrations.DeleteModel(
            name='MTN_MainAdvert',
        ),
        migrations.DeleteModel(
            name='MTN_MainPageFeatured',
        ),
        migrations.DeleteModel(
            name='MTN_Song',
        ),
        migrations.DeleteModel(
            name='MTN_SongTagAssociation',
        ),
    ]

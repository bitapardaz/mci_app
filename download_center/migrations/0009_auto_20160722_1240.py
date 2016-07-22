# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('download_center', '0008_topadvert'),
    ]

    operations = [
        migrations.CreateModel(
            name='MiddleAdvert',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('miscellaneous', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('url', models.URLField(null=True, blank=True)),
                ('ranking', models.IntegerField(default=0)),
                ('album', models.ForeignKey(blank=True, to='download_center.Album', null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='mainadvert',
            name='album',
        ),
        migrations.DeleteModel(
            name='MainAdvert',
        ),
    ]

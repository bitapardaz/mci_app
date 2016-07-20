# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('download_center', '0002_auto_20160718_0353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singer',
            name='singles_album',
            field=models.OneToOneField(null=True, blank=True, to='download_center.Album'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('download_center', '0003_auto_20160718_0446'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='singer',
            name='singles_album',
        ),
    ]

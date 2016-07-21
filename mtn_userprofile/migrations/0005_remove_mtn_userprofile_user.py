# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mtn_userprofile', '0004_mtn_userprofile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mtn_userprofile',
            name='user',
        ),
    ]

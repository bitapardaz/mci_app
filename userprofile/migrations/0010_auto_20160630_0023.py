# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0009_auto_20160630_0017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activationrequest',
            name='song',
        ),
        migrations.RemoveField(
            model_name='activationrequest',
            name='time_stamp',
        ),
        migrations.RemoveField(
            model_name='activationrequest',
            name='user_profile',
        ),
    ]

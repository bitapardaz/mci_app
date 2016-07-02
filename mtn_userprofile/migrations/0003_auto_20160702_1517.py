# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mtn_userprofile', '0002_mtn_activationrequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mtn_rbt_activation',
            name='song',
        ),
        migrations.RemoveField(
            model_name='mtn_rbt_activation',
            name='user',
        ),
        migrations.DeleteModel(
            name='MTN_RBT_Activation',
        ),
    ]

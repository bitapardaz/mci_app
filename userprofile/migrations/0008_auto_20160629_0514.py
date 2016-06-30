# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0007_activationrequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rbt_activation',
            name='song',
        ),
        migrations.RemoveField(
            model_name='rbt_activation',
            name='user',
        ),
        migrations.DeleteModel(
            name='RBT_Activation',
        ),
    ]

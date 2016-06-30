# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbt', '0046_auto_20160622_0350'),
        ('userprofile', '0011_activationrequest_time_stamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='activationrequest',
            name='song',
            field=models.ForeignKey(to='rbt.Song', null=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0010_auto_20160630_0023'),
    ]

    operations = [
        migrations.AddField(
            model_name='activationrequest',
            name='time_stamp',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]

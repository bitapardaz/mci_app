# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0016_auto_20160630_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activationrequest',
            name='time_stamp',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_userprofile_imei'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='imei',
            field=models.CharField(max_length=36),
        ),
    ]

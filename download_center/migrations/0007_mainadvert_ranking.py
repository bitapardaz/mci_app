# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('download_center', '0006_auto_20160720_0143'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainadvert',
            name='ranking',
            field=models.IntegerField(default=0),
        ),
    ]

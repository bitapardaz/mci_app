# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbt', '0031_remove_mainadvert_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='catadvert',
            name='miscellaneous',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AddField(
            model_name='catadvert',
            name='url',
            field=models.URLField(null=True, blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbt', '0049_auto_20160701_2251'),
    ]

    operations = [
        migrations.RenameField(
            model_name='search_activity',
            old_name='is_result_empty',
            new_name='result_has_album',
        ),
    ]

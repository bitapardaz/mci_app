# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0019_auto_20160630_0318'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activationrequest',
            old_name='WhereAmI',
            new_name='where_am_i',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general_user_profile', '0001_initial'),
        ('mtn_userprofile', '0005_remove_mtn_userprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='mtn_userprofile',
            name='general_profile',
            field=models.ForeignKey(blank=True, to='general_user_profile.GeneralProfile', null=True),
        ),
    ]

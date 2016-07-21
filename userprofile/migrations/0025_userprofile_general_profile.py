# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general_user_profile', '0001_initial'),
        ('userprofile', '0024_remove_userprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='general_profile',
            field=models.ForeignKey(blank=True, to='general_user_profile.GeneralProfile', null=True),
        ),
    ]

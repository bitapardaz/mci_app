# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0013_auto_20160630_0054'),
    ]

    operations = [
        migrations.AddField(
            model_name='activationrequest',
            name='user_profile',
            field=models.ForeignKey(to='userprofile.UserProfile', null=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0014_activationrequest_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activationrequest',
            name='user_profile',
            field=models.ForeignKey(to='userprofile.UserProfile'),
        ),
    ]

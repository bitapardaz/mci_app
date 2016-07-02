# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mtn_rbt', '0006_auto_20160702_0224'),
        ('mtn_userprofile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MTN_ActivationRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time_stamp', models.DateTimeField(auto_now=True, null=True)),
                ('where_i_am', models.CharField(max_length=100, null=True, blank=True)),
                ('activated', models.BooleanField(default=False)),
                ('song', models.ForeignKey(to='mtn_rbt.MTN_Song')),
                ('user_profile', models.ForeignKey(to='mtn_userprofile.MTN_UserProfile')),
            ],
        ),
    ]

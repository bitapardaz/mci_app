# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbt', '0046_auto_20160622_0350'),
        ('userprofile', '0006_remove_userprofile_imei'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivationRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time_stamp', models.DateTimeField(auto_now=True)),
                ('WhereAmI', models.CharField(max_length=100, null=True, blank=True)),
                ('activated', models.BooleanField(default=False)),
                ('song', models.ForeignKey(to='rbt.Song')),
                ('user_profile', models.ForeignKey(to='userprofile.UserProfile')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mtn_rbt', '0005_mtn_search_activity'),
    ]

    operations = [
        migrations.CreateModel(
            name='MTN_RBT_Activation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('song', models.ForeignKey(to='mtn_rbt.MTN_Song')),
            ],
        ),
        migrations.CreateModel(
            name='MTN_UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mobile_number', models.CharField(max_length=20)),
                ('token', models.CharField(max_length=160, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='mtn_rbt_activation',
            name='user',
            field=models.ForeignKey(to='mtn_userprofile.MTN_UserProfile'),
        ),
    ]

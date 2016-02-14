# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbt', '0006_category_featured'),
    ]

    operations = [
        migrations.CreateModel(
            name='RBT_Activation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('song', models.ForeignKey(to='rbt.Song')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mobile_number', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='rbt_activation',
            name='user',
            field=models.ForeignKey(to='userprofile.UserProfile'),
        ),
    ]

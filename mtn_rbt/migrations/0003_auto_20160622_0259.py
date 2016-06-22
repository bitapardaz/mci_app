# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mtn_rbt', '0002_auto_20160622_0007'),
    ]

    operations = [
        migrations.CreateModel(
            name='MTN_Producer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('confirmed', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AlterField(
            model_name='mtn_album',
            name='producer',
            field=models.ForeignKey(blank=True, to='mtn_rbt.MTN_Producer', null=True),
        ),
        migrations.AlterField(
            model_name='mtn_song',
            name='producer',
            field=models.ForeignKey(blank=True, to='mtn_rbt.MTN_Producer', null=True),
        ),
    ]

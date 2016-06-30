# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0012_activationrequest_song'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activationrequest',
            name='song',
            field=models.ForeignKey(to='rbt.Song'),
        ),
    ]

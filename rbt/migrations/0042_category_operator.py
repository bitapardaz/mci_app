# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbt', '0041_operator'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='operator',
            field=models.ForeignKey(to='rbt.Operator', null=True),
        ),
    ]

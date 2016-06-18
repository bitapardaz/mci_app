# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbt', '0038_auto_20160521_0538'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search_Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('search_term', models.CharField(max_length=20)),
            ],
        ),
    ]

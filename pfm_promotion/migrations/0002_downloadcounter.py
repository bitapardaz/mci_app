# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfm_promotion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DownloadCounter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('counter', models.IntegerField(default=0)),
            ],
        ),
    ]

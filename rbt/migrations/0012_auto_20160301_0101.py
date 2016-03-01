# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbt', '0011_remove_category_farsi_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='farsi_name',
        ),
        migrations.AddField(
            model_name='category',
            name='english_name',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='price',
            field=models.IntegerField(default=300),
        ),
    ]

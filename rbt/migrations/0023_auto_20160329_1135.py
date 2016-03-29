# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbt', '0022_album_producer'),
    ]

    operations = [
        migrations.CreateModel(
            name='PseudoProducer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('confirmed', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='pseudo_producer',
            field=models.ForeignKey(blank=True, to='rbt.PseudoProducer', null=True),
        ),
    ]

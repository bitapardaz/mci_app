# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tci_userprofile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MobileDevice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imei', models.CharField(max_length=20)),
                ('token_string', models.CharField(max_length=160, null=True, blank=True)),
                ('sms_verification_code', models.CharField(max_length=10)),
                ('sms_code_expiery', models.DateTimeField()),
                ('user_profile', models.ForeignKey(to='tci_userprofile.UserProfile')),
            ],
        ),
    ]

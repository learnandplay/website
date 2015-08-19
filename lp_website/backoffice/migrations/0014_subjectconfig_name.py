# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0013_exerciseconfig_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjectconfig',
            name='name',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
    ]

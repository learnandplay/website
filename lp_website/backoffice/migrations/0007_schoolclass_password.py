# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0006_auto_20150207_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolclass',
            name='password',
            field=models.CharField(default='password', max_length=50),
            preserve_default=False,
        ),
    ]

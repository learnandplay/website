# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0010_statistics_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='data',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]

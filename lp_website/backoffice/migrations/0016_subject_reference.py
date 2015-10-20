# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0015_exercise_reference'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='reference',
            field=models.CharField(default='', max_length=32),
            preserve_default=False,
        ),
    ]

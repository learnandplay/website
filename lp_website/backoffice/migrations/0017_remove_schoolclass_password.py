# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0016_subject_reference'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schoolclass',
            name='password',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0007_schoolclass_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolclass',
            name='password',
            field=models.CharField(max_length=128),
        ),
    ]

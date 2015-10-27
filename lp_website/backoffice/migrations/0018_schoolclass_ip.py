# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0017_remove_schoolclass_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolclass',
            name='ip',
            field=models.CharField(default=b'', max_length=32),
            preserve_default=True,
        ),
    ]

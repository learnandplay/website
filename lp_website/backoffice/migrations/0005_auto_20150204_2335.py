# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0004_auto_20150204_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lpuser',
            name='avatar',
            field=models.ImageField(default=b'avatars/default.png', null=True, upload_to=b'avatars', blank=True),
        ),
    ]

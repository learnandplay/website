# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0003_lpuser_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lpuser',
            name='avatar',
            field=models.ImageField(upload_to=b'avatars'),
        ),
    ]

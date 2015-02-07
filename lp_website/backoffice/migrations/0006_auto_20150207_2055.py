# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0005_auto_20150204_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lpuser',
            name='avatar',
            field=imagekit.models.fields.ProcessedImageField(default=b'avatars/default.png', null=True, upload_to=b'avatars', blank=True),
        ),
    ]

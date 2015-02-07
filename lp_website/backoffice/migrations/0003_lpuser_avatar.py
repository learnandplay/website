# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0002_auto_20141227_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='lpuser',
            name='avatar',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to=b'avatars', blank=True),
            preserve_default=True,
        ),
    ]

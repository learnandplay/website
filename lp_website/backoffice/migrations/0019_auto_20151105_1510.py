# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0018_schoolclass_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='exerciseconfig',
            name='creation_date',
            field=models.DateTimeField(default=datetime.date(2015, 11, 5), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exerciseconfig',
            name='modification_date',
            field=models.DateTimeField(default=datetime.date(2015, 11, 5), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subjectconfig',
            name='creation_date',
            field=models.DateTimeField(default=datetime.date(2015, 11, 5), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subjectconfig',
            name='modification_date',
            field=models.DateTimeField(default=datetime.date(2015, 11, 5), auto_now=True),
            preserve_default=False,
        ),
    ]

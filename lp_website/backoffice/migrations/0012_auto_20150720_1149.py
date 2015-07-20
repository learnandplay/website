# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0011_subject_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exerciseconfig',
            name='school_class',
            field=models.ForeignKey(blank=True, to='backoffice.SchoolClass', null=True),
        ),
        migrations.AlterField(
            model_name='subjectconfig',
            name='school_class',
            field=models.ForeignKey(blank=True, to='backoffice.SchoolClass', null=True),
        ),
    ]

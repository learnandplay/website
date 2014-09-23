# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('data', models.TextField()),
            ],
            options={
                'db_table': 'lp_exercise',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ExerciseConfig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateTimeField(null=True, blank=True)),
                ('end_date', models.DateTimeField(null=True, blank=True)),
                ('data', models.TextField()),
                ('exercise', models.ForeignKey(to='backoffice.Exercise')),
            ],
            options={
                'db_table': 'lp_exercise_config',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LPUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'lp_user',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SchoolClass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('school_name', models.CharField(max_length=128)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modification_date', models.DateTimeField(auto_now=True)),
                ('data', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'lp_schoolclass',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.TextField()),
                ('exercise', models.ForeignKey(to='backoffice.Exercise')),
            ],
            options={
                'db_table': 'lp_statistics',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'lp_subject',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SubjectConfig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateTimeField(null=True, blank=True)),
                ('end_date', models.DateTimeField(null=True, blank=True)),
                ('data', models.TextField()),
                ('school_class', models.ForeignKey(to='backoffice.SchoolClass')),
                ('subject', models.ForeignKey(to='backoffice.Subject')),
            ],
            options={
                'db_table': 'lp_subject_config',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='statistics',
            name='subject',
            field=models.ForeignKey(to='backoffice.Subject'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='statistics',
            name='user',
            field=models.ForeignKey(to='backoffice.LPUser'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lpuser',
            name='school_class',
            field=models.ManyToManyField(to='backoffice.SchoolClass', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lpuser',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='exerciseconfig',
            name='school_class',
            field=models.ForeignKey(to='backoffice.SchoolClass'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='exercise',
            name='subject',
            field=models.ForeignKey(to='backoffice.Subject'),
            preserve_default=True,
        ),
    ]

#!/usr/bin/env python
from django.contrib.auth.models import Group

teachers = Group.objects.create(name='teachers')
teachers.save()
students = Group.objects.create(name='students')
students.save()

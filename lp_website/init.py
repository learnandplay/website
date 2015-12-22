#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.contrib.auth.models import Group
from backoffice.models import LPUser, SchoolClass, Subject, Exercise, Statistics

##
## Create groups
##

teachers = Group.objects.create(name='teachers')
teachers.save()
students = Group.objects.create(name='students')
students.save()

##
## Create subjects
##

maths = Subject(name='Mathématiques', reference='maths', data='{"accessible": {"value": "bool", "titleMap": ["Autoriser", "Ne pas autoriser"], "title": "Autoriser l\'accès"}}')
maths.save()
fr = Subject(name='Français', reference='fr', data='{"accessible": {"value": "bool", "titleMap": ["Autoriser", "Ne pas autoriser"], "title": "Autoriser l\'accès"}}')
fr.save()

##
## Create Exercises
##

Exercise(name='Compter les pommes', subject=maths, reference='maths-compte-pomme', data='{"accessible": {"value": "bool", "titleMap": ["Autoriser", "Ne pas autoriser"], "title": "Autoriser l\'accès"}}').save()
Exercise(name='Memory', subject=fr, reference='fr-memory', data='{"accessible": {"value": "bool", "titleMap": ["Autoriser", "Ne pas autoriser"], "title": "Autoriser l\'accès"}}').save()
Exercise(name='Reconnaissance des sons', subject=fr, reference='fr-reco-sons', data='{"accessible": {"value": "bool", "titleMap": ["Autoriser", "Ne pas autoriser"], "title": "Autoriser l\'accès"}}').save()

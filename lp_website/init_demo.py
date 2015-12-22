#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.contrib.auth.models import User, Group
from backoffice.models import LPUser, SchoolClass, Subject, Exercise, Statistics

execfile("./init.py")

#password for users is "password"

#password for school classes is "password_class"

##
## Create teachers
##

teachers = []
lp_teachers = []

teachers.append(User(username='teacher1', email='teacher1@domain.com', password='pbkdf2_sha256$12000$d6vlMBAMnAYT$jnnaq7ea4XGw6oIAbEs1F4O+TEZfZABbuaAd6sZw28I=', is_active=True))
teachers[0].save()
teachers[0].groups.add(Group.objects.get(name='teachers'))
lp_teachers.append(LPUser())
lp_teachers[0].user = teachers[0]
lp_teachers[0].save()

teachers.append(User(username='teacher2', email='teacher2@domain.com', password='pbkdf2_sha256$12000$d6vlMBAMnAYT$jnnaq7ea4XGw6oIAbEs1F4O+TEZfZABbuaAd6sZw28I=', is_active=True))
teachers[1].save()
teachers[1].groups.add(Group.objects.get(name='teachers'))
lp_teachers.append(LPUser())
lp_teachers[1].user = teachers[1]
lp_teachers[1].save()

##
## Create School classes
##

school_classes = []

school_classes.append(SchoolClass(name='CP 1', school_name='Ecole Albert Camus'))
school_classes[0].save()
school_classes.append(SchoolClass(name='CP 2', school_name='Ecole Albert Camus'))
school_classes[1].save()
lp_teachers[0].school_class.add(school_classes[0])
lp_teachers[0].school_class.add(school_classes[1])
lp_teachers[1].school_class.add(school_classes[1])

##
## Create students
##

students = []
lp_students = []

# Students for class 0
students.append([])
students[0].append(User(username='Benjamin.Boisset', email='student-dev@domain.com', password='pbkdf2_sha256$12000$d6vlMBAMnAYT$jnnaq7ea4XGw6oIAbEs1F4O+TEZfZABbuaAd6sZw28I=', is_active=True))
students[0][0].save()
students[0][0].groups.add(Group.objects.get(name='students'))
lp_students.append([])
lp_students[0].append(LPUser(data='{"credits":42}'))
lp_students[0][0].user = students[0][0]
lp_students[0][0].save()
lp_students[0][0].school_class.add(school_classes[0])

students[0].append(User(username='Julien.Lefebvre', email='student-dev@domain.com', password='pbkdf2_sha256$12000$d6vlMBAMnAYT$jnnaq7ea4XGw6oIAbEs1F4O+TEZfZABbuaAd6sZw28I=', is_active=True))
students[0][1].save()
students[0][1].groups.add(Group.objects.get(name='students'))
lp_students.append([])
lp_students[0].append(LPUser())
lp_students[0][1].user = students[0][1]
lp_students[0][1].save()
lp_students[0][1].school_class.add(school_classes[0])

students[0].append(User(username='Manon.Durand', email='student-dev@domain.com', password='pbkdf2_sha256$12000$d6vlMBAMnAYT$jnnaq7ea4XGw6oIAbEs1F4O+TEZfZABbuaAd6sZw28I=', is_active=True))
students[0][2].save()
students[0][2].groups.add(Group.objects.get(name='students'))
lp_students.append([])
lp_students[0].append(LPUser())
lp_students[0][2].user = students[0][2]
lp_students[0][2].save()
lp_students[0][2].school_class.add(school_classes[0])

students[0].append(User(username='Pierre.Moreau', email='student-dev@domain.com', password='pbkdf2_sha256$12000$d6vlMBAMnAYT$jnnaq7ea4XGw6oIAbEs1F4O+TEZfZABbuaAd6sZw28I=', is_active=True))
students[0][3].save()
students[0][3].groups.add(Group.objects.get(name='students'))
lp_students.append([])
lp_students[0].append(LPUser())
lp_students[0][3].user = students[0][3]
lp_students[0][3].save()
lp_students[0][3].school_class.add(school_classes[0])

students[0].append(User(username='Marie.Petit', email='student-dev@domain.com', password='pbkdf2_sha256$12000$d6vlMBAMnAYT$jnnaq7ea4XGw6oIAbEs1F4O+TEZfZABbuaAd6sZw28I=', is_active=True))
students[0][4].save()
students[0][4].groups.add(Group.objects.get(name='students'))
lp_students.append([])
lp_students[0].append(LPUser())
lp_students[0][4].user = students[0][4]
lp_students[0][4].save()
lp_students[0][4].school_class.add(school_classes[0])

students[0].append(User(username='Romain.Brunet', email='student-dev@domain.com', password='pbkdf2_sha256$12000$d6vlMBAMnAYT$jnnaq7ea4XGw6oIAbEs1F4O+TEZfZABbuaAd6sZw28I=', is_active=True))
students[0][5].save()
students[0][5].groups.add(Group.objects.get(name='students'))
lp_students.append([])
lp_students[0].append(LPUser())
lp_students[0][5].user = students[0][5]
lp_students[0][5].save()
lp_students[0][5].school_class.add(school_classes[0])

students[0].append(User(username='Lucie.Masson', email='student-dev@domain.com', password='pbkdf2_sha256$12000$d6vlMBAMnAYT$jnnaq7ea4XGw6oIAbEs1F4O+TEZfZABbuaAd6sZw28I=', is_active=True))
students[0][6].save()
students[0][6].groups.add(Group.objects.get(name='students'))
lp_students.append([])
lp_students[0].append(LPUser())
lp_students[0][6].user = students[0][6]
lp_students[0][6].save()
lp_students[0][6].school_class.add(school_classes[0])

students[0].append(User(username='Laura.Moulin', email='student-dev@domain.com', password='pbkdf2_sha256$12000$d6vlMBAMnAYT$jnnaq7ea4XGw6oIAbEs1F4O+TEZfZABbuaAd6sZw28I=', is_active=True))
students[0][7].save()
students[0][7].groups.add(Group.objects.get(name='students'))
lp_students.append([])
lp_students[0].append(LPUser())
lp_students[0][7].user = students[0][7]
lp_students[0][7].save()
lp_students[0][7].school_class.add(school_classes[0])

students[0].append(User(username='Anthony.Payet', email='student-dev@domain.com', password='pbkdf2_sha256$12000$d6vlMBAMnAYT$jnnaq7ea4XGw6oIAbEs1F4O+TEZfZABbuaAd6sZw28I=', is_active=True))
students[0][8].save()
students[0][8].groups.add(Group.objects.get(name='students'))
lp_students.append([])
lp_students[0].append(LPUser())
lp_students[0][8].user = students[0][8]
lp_students[0][8].save()
lp_students[0][8].school_class.add(school_classes[0])

students[0].append(User(username='Lea.Martinez', email='student-dev@domain.com', password='pbkdf2_sha256$12000$d6vlMBAMnAYT$jnnaq7ea4XGw6oIAbEs1F4O+TEZfZABbuaAd6sZw28I=', is_active=True))
students[0][9].save()
students[0][9].groups.add(Group.objects.get(name='students'))
lp_students.append([])
lp_students[0].append(LPUser())
lp_students[0][9].user = students[0][9]
lp_students[0][9].save()
lp_students[0][9].school_class.add(school_classes[0])

# Students for class 1
students.append([])
students[1].append(User(username='Ludovic.Roux', email='student-dev@domain.com', password='pbkdf2_sha256$12000$d6vlMBAMnAYT$jnnaq7ea4XGw6oIAbEs1F4O+TEZfZABbuaAd6sZw28I=', is_active=True))
students[1][0].save()
students[1][0].groups.add(Group.objects.get(name='students'))
lp_students.append([])
lp_students[1].append(LPUser())
lp_students[1][0].user = students[1][0]
lp_students[1][0].save()
lp_students[1][0].school_class.add(school_classes[1])

students[1].append(User(username='Laetita.Marin', email='student-dev@domain.com', password='pbkdf2_sha256$12000$d6vlMBAMnAYT$jnnaq7ea4XGw6oIAbEs1F4O+TEZfZABbuaAd6sZw28I=', is_active=True))
students[1][1].save()
students[1][1].groups.add(Group.objects.get(name='students'))
lp_students.append([])
lp_students[1].append(LPUser())
lp_students[1][1].user = students[1][1]
lp_students[1][1].save()
lp_students[1][1].school_class.add(school_classes[1])

students[1].append(User(username='Lambert.Jourdain', email='student-dev@domain.com', password='pbkdf2_sha256$12000$d6vlMBAMnAYT$jnnaq7ea4XGw6oIAbEs1F4O+TEZfZABbuaAd6sZw28I=', is_active=True))
students[1][2].save()
students[1][2].groups.add(Group.objects.get(name='students'))
lp_students.append([])
lp_students[1].append(LPUser())
lp_students[1][2].user = students[1][2]
lp_students[1][2].save()
lp_students[1][2].school_class.add(school_classes[1])

students[1].append(User(username='Guillaume.Verdier', email='student-dev@domain.com', password='pbkdf2_sha256$12000$d6vlMBAMnAYT$jnnaq7ea4XGw6oIAbEs1F4O+TEZfZABbuaAd6sZw28I=', is_active=True))
students[1][3].save()
students[1][3].groups.add(Group.objects.get(name='students'))
lp_students.append([])
lp_students[1].append(LPUser())
lp_students[1][3].user = students[1][3]
lp_students[1][3].save()
lp_students[1][3].school_class.add(school_classes[1])

students[1].append(User(username='Kevin.Poncet', email='student-dev@domain.com', password='pbkdf2_sha256$12000$d6vlMBAMnAYT$jnnaq7ea4XGw6oIAbEs1F4O+TEZfZABbuaAd6sZw28I=', is_active=True))
students[1][4].save()
students[1][4].groups.add(Group.objects.get(name='students'))
lp_students.append([])
lp_students[1].append(LPUser())
lp_students[1][4].user = students[1][4]
lp_students[1][4].save()
lp_students[1][4].school_class.add(school_classes[1])

students[1].append(User(username='Marine.Duclos', email='student-dev@domain.com', password='pbkdf2_sha256$12000$d6vlMBAMnAYT$jnnaq7ea4XGw6oIAbEs1F4O+TEZfZABbuaAd6sZw28I=', is_active=True))
students[1][5].save()
students[1][5].groups.add(Group.objects.get(name='students'))
lp_students.append([])
lp_students[1].append(LPUser())
lp_students[1][5].user = students[1][5]
lp_students[1][5].save()
lp_students[1][5].school_class.add(school_classes[1])

students[1].append(User(username='Emma.Ricard', email='student-dev@domain.com', password='pbkdf2_sha256$12000$d6vlMBAMnAYT$jnnaq7ea4XGw6oIAbEs1F4O+TEZfZABbuaAd6sZw28I=', is_active=True))
students[1][6].save()
students[1][6].groups.add(Group.objects.get(name='students'))
lp_students.append([])
lp_students[1].append(LPUser())
lp_students[1][6].user = students[1][6]
lp_students[1][6].save()
lp_students[1][6].school_class.add(school_classes[1])

students[1].append(User(username='Johanna.Levasseur', email='student-dev@domain.com', password='pbkdf2_sha256$12000$d6vlMBAMnAYT$jnnaq7ea4XGw6oIAbEs1F4O+TEZfZABbuaAd6sZw28I=', is_active=True))
students[1][7].save()
students[1][7].groups.add(Group.objects.get(name='students'))
lp_students.append([])
lp_students[1].append(LPUser())
lp_students[1][7].user = students[1][7]
lp_students[1][7].save()
lp_students[1][7].school_class.add(school_classes[1])

students[1].append(User(username='Florian.Vacher', email='student-dev@domain.com', password='pbkdf2_sha256$12000$d6vlMBAMnAYT$jnnaq7ea4XGw6oIAbEs1F4O+TEZfZABbuaAd6sZw28I=', is_active=True))
students[1][8].save()
students[1][8].groups.add(Group.objects.get(name='students'))
lp_students.append([])
lp_students[1].append(LPUser())
lp_students[1][8].user = students[1][8]
lp_students[1][8].save()
lp_students[1][8].school_class.add(school_classes[1])

students[1].append(User(username='Alexandre.Tissier', email='student-dev@domain.com', password='pbkdf2_sha256$12000$d6vlMBAMnAYT$jnnaq7ea4XGw6oIAbEs1F4O+TEZfZABbuaAd6sZw28I=', is_active=True))
students[1][9].save()
students[1][9].groups.add(Group.objects.get(name='students'))
lp_students.append([])
lp_students[1].append(LPUser())
lp_students[1][9].user = students[1][9]
lp_students[1][9].save()
lp_students[1][9].school_class.add(school_classes[1])

##
## Create subjects
##

subjects = {}

subjects['maths'] = Subject.objects.get(reference='maths')
subjects['fr'] = Subject.objects.get(reference='fr')
subjects['en'] = Subject(name='Anglais', reference='en', data='{"accessible": {"value": "bool", "titleMap": ["Autoriser", "Ne pas autoriser"], "title": "Autoriser l\'accès"}}')
subjects['en'].save()

##
## Create Exercises
##

exercises = {}

exercises['maths-additions'] = Exercise(name='Additions', subject=subjects['maths'], reference='maths-additions', data='{"accessible": {"value": "bool", "titleMap": ["Autoriser", "Ne pas autoriser"], "title": "Autoriser l\'accès"}}')
exercises['maths-additions'].save()
exercises['maths-soustractions'] = Exercise(name='Soustractions', subject=subjects['maths'], reference='maths-soustractions', data='{"accessible": {"value": "bool", "titleMap": ["Autoriser", "Ne pas autoriser"], "title": "Autoriser l\'accès"}}')
exercises['maths-soustractions'].save()
exercises['maths-geometrie'] = Exercise(name='Géométrie', subject=subjects['maths'], reference='maths-geometrie', data='{"goal": {"value": ["Reconnaissance de formes", "Reconnaissance des tailles"], "title": "Type de questions"}, "allow_retry": {"value": "bool", "titleMap": ["Autoriser", "Ne pas autoriser"], "default": "false", "title": "Autoriser l\'élève à refaire une question"}, "nb_try": {"value": "integer", "title": "Nombre de tentatives"}, "accessible": {"value": "bool", "titleMap": ["Autoriser", "Ne pas autoriser"], "title": "Autoriser l\'accès"}}')
exercises['maths-geometrie'].save()

exercises['fr-lecture'] = Exercise(name='Lecture', subject=subjects['fr'], reference='fr-lecture', data='{"accessible": {"value": "bool", "titleMap": ["Autoriser", "Ne pas autoriser"], "title": "Autoriser l\'accès"}}')
exercises['fr-lecture'].save()

exercises['en-lecture'] = Exercise(name='Lecture', subject=subjects['en'], reference='en-lecture', data='{"accessible": {"value": "bool", "titleMap": ["Autoriser", "Ne pas autoriser"], "title": "Autoriser l\'accès"}}')
exercises['en-lecture'].save()

##
## Create Statistics
##

statistics = []

Statistics(user=lp_students[0][0], exercise=exercises['maths-additions'], data='{"multi":"true","time":"80","success":"7","failure":"3"}').save()
Statistics(user=lp_students[0][0], exercise=exercises['maths-additions'], data='{"multi":"true","time":"78","success":"9","failure":"1"}').save()
Statistics(user=lp_students[0][0], exercise=exercises['maths-additions'], data='{"multi":"true","time":"83","success":"10","failure":"0"}').save()
Statistics(user=lp_students[0][0], exercise=exercises['maths-soustractions'], data='{"multi":"true","time":"100","success":"6","failure":"4"}').save()
Statistics(user=lp_students[0][0], exercise=exercises['maths-geometrie'], data='{"multi":"false","time":"60","success":"4","failure":"6"}').save()
Statistics(user=lp_students[0][0], exercise=exercises['fr-lecture'], data='{"multi":"true","time":"60","success":"7","failure":"3"}').save()
Statistics(user=lp_students[0][0], exercise=exercises['en-lecture'], data='{"multi":"false","time":"156","success":"100","failure":"0"}').save()

Statistics(user=lp_students[0][1], exercise=exercises['maths-additions'], data='{"multi":"true","time":"63","success":"6","failure":"4"}').save()
Statistics(user=lp_students[0][1], exercise=exercises['maths-soustractions'], data='{"multi":"true","time":"98","success":"7","failure":"3"}').save()

Statistics(user=lp_students[0][2], exercise=exercises['maths-additions'], data='{"multi":"true","time":"79","success":"8","failure":"2"}').save()
Statistics(user=lp_students[0][2], exercise=exercises['maths-soustractions'], data='{"multi":"true","time":"127","success":"8","failure":"2"}').save()
Statistics(user=lp_students[0][2], exercise=exercises['maths-geometrie'], data='{"multi":"false","time":"54","success":"9","failure":"1"}').save()
Statistics(user=lp_students[0][2], exercise=exercises['fr-lecture'], data='{"multi":"true","time":"67","success":"6","failure":"4"}').save()
Statistics(user=lp_students[0][2], exercise=exercises['en-lecture'], data='{"multi":"false","time":"601","success":"99","failure":"1"}').save()

Statistics(user=lp_students[0][3], exercise=exercises['maths-additions'], data='{"multi":"false","time":"85","success":"10","failure":"0"}').save()
Statistics(user=lp_students[0][3], exercise=exercises['maths-soustractions'], data='{"multi":"true","time":"112","success":"5","failure":"5"}').save()
Statistics(user=lp_students[0][3], exercise=exercises['maths-geometrie'], data='{"multi":"false","time":"61","success":"6","failure":"4"}').save()
Statistics(user=lp_students[0][3], exercise=exercises['fr-lecture'], data='{"multi":"false","time":"60","success":"7","failure":"3"}').save()
Statistics(user=lp_students[0][3], exercise=exercises['en-lecture'], data='{"multi":"false","time":"151","success":"87","failure":"13"}').save()

Statistics(user=lp_students[0][4], exercise=exercises['maths-additions'], data='{"multi":"true","time":"68","success":"7","failure":"3"}').save()
Statistics(user=lp_students[0][4], exercise=exercises['maths-soustractions'], data='{"multi":"true","time":"127","success":"10","failure":"0"}').save()
Statistics(user=lp_students[0][4], exercise=exercises['maths-geometrie'], data='{"multi":"false","time":"60","success":"8","failure":"2"}').save()
Statistics(user=lp_students[0][4], exercise=exercises['fr-lecture'], data='{"multi":"true","time":"60","success":"4","failure":"6"}').save()
Statistics(user=lp_students[0][4], exercise=exercises['en-lecture'], data='{"multi":"false","time":"212","success":"95","failure":"5"}').save()

Statistics(user=lp_students[0][5], exercise=exercises['maths-additions'], data='{"multi":"true","time":"76","success":"7","failure":"3"}').save()
Statistics(user=lp_students[0][5], exercise=exercises['maths-soustractions'], data='{"multi":"true","time":"107","success":"4","failure":"6"}').save()
Statistics(user=lp_students[0][5], exercise=exercises['maths-geometrie'], data='{"multi":"false","time":"64","success":"5","failure":"5"}').save()
Statistics(user=lp_students[0][5], exercise=exercises['fr-lecture'], data='{"multi":"true","time":"60","success":"7","failure":"3"}').save()
Statistics(user=lp_students[0][5], exercise=exercises['en-lecture'], data='{"multi":"false","time":"103","success":"67","failure":"33"}').save()

Statistics(user=lp_students[0][6], exercise=exercises['maths-additions'], data='{"multi":"true","time":"80","success":"7","failure":"3"}').save()
Statistics(user=lp_students[0][6], exercise=exercises['maths-soustractions'], data='{"multi":"true","time":"104","success":"3","failure":"7"}').save()
Statistics(user=lp_students[0][6], exercise=exercises['maths-geometrie'], data='{"multi":"false","time":"76","success":"6","failure":"4"}').save()
Statistics(user=lp_students[0][6], exercise=exercises['fr-lecture'], data='{"multi":"true","time":"64","success":"10","failure":"0"}').save()
Statistics(user=lp_students[0][6], exercise=exercises['en-lecture'], data='{"multi":"false","time":"164","success":"100","failure":"0"}').save()

Statistics(user=lp_students[0][7], exercise=exercises['maths-additions'], data='{"multi":"true","time":"84","success":"7","failure":"3"}').save()
Statistics(user=lp_students[0][7], exercise=exercises['maths-soustractions'], data='{"multi":"true","time":"107","success":"7","failure":"3"}').save()
Statistics(user=lp_students[0][7], exercise=exercises['maths-geometrie'], data='{"multi":"false","time":"60","success":"7","failure":"3"}').save()
Statistics(user=lp_students[0][7], exercise=exercises['fr-lecture'], data='{"multi":"true","time":"60","success":"6","failure":"4"}').save()
Statistics(user=lp_students[0][7], exercise=exercises['en-lecture'], data='{"multi":"false","time":"321","success":"88","failure":"12"}').save()

Statistics(user=lp_students[0][8], exercise=exercises['maths-additions'], data='{"multi":"true","time":"80","success":"7","failure":"3"}').save()
Statistics(user=lp_students[0][8], exercise=exercises['maths-soustractions'], data='{"multi":"true","time":"100","success":"6","failure":"4"}').save()
Statistics(user=lp_students[0][8], exercise=exercises['maths-geometrie'], data='{"multi":"false","time":"60","success":"5","failure":"5"}').save()
Statistics(user=lp_students[0][8], exercise=exercises['fr-lecture'], data='{"multi":"true","time":"60","success":"7","failure":"3"}').save()
Statistics(user=lp_students[0][8], exercise=exercises['en-lecture'], data='{"multi":"false","time":"165","success":"55","failure":"45"}').save()

Statistics(user=lp_students[0][9], exercise=exercises['maths-additions'], data='{"multi":"true","time":"92","success":"7","failure":"3"}').save()
Statistics(user=lp_students[0][9], exercise=exercises['maths-soustractions'], data='{"multi":"true","time":"107","success":"8","failure":"2"}').save()
Statistics(user=lp_students[0][9], exercise=exercises['maths-geometrie'], data='{"multi":"false","time":"67","success":"6","failure":"4"}').save()
Statistics(user=lp_students[0][9], exercise=exercises['fr-lecture'], data='{"multi":"true","time":"21","success":"1","failure":"9"}').save()
Statistics(user=lp_students[0][9], exercise=exercises['en-lecture'], data='{"multi":"false","time":"287","success":"98","failure":"2"}').save()

Statistics(user=lp_students[1][0], exercise=exercises['maths-additions'], data='{"multi":"true","time":"65","success":"9","failure":"1"}').save()
Statistics(user=lp_students[1][0], exercise=exercises['maths-soustractions'], data='{"multi":"true","time":"87","success":"8","failure":"2"}').save()
Statistics(user=lp_students[1][0], exercise=exercises['maths-geometrie'], data='{"multi":"false","time":"54","success":"10","failure":"0"}').save()
Statistics(user=lp_students[1][0], exercise=exercises['fr-lecture'], data='{"multi":"true","time":"54","success":"9","failure":"1"}').save()
Statistics(user=lp_students[1][0], exercise=exercises['en-lecture'], data='{"multi":"false","time":"123","success":"95","failure":"5"}').save()

Statistics(user=lp_students[1][1], exercise=exercises['maths-additions'], data='{"multi":"true","time":"83","success":"7","failure":"3"}').save()
Statistics(user=lp_students[1][1], exercise=exercises['maths-geometrie'], data='{"multi":"false","time":"60","success":"6","failure":"4"}').save()
Statistics(user=lp_students[1][1], exercise=exercises['fr-lecture'], data='{"multi":"true","time":"75","success":"7","failure":"3"}').save()

Statistics(user=lp_students[1][2], exercise=exercises['fr-lecture'], data='{"multi":"true","time":"64","success":"7","failure":"3"}').save()
Statistics(user=lp_students[1][2], exercise=exercises['en-lecture'], data='{"multi":"false","time":"202","success":"90","failure":"10"}').save()

Statistics(user=lp_students[1][3], exercise=exercises['maths-additions'], data='{"multi":"true","time":"88","success":"6","failure":"4"}').save()
Statistics(user=lp_students[1][3], exercise=exercises['maths-soustractions'], data='{"multi":"true","time":"109","success":"1","failure":"9"}').save()
Statistics(user=lp_students[1][3], exercise=exercises['maths-geometrie'], data='{"multi":"false","time":"69","success":"3","failure":"7"}').save()
Statistics(user=lp_students[1][3], exercise=exercises['fr-lecture'], data='{"multi":"true","time":"63","success":"4","failure":"6"}').save()
Statistics(user=lp_students[1][3], exercise=exercises['en-lecture'], data='{"multi":"false","time":"304","success":"65","failure":"35"}').save()

Statistics(user=lp_students[1][4], exercise=exercises['maths-additions'], data='{"multi":"true","time":"84","success":"7","failure":"3"}').save()
Statistics(user=lp_students[1][4], exercise=exercises['maths-soustractions'], data='{"multi":"true","time":"102","success":"8","failure":"2"}').save()
Statistics(user=lp_students[1][4], exercise=exercises['maths-geometrie'], data='{"multi":"false","time":"57","success":"6","failure":"4"}').save()
Statistics(user=lp_students[1][4], exercise=exercises['fr-lecture'], data='{"multi":"true","time":"63","success":"7","failure":"3"}').save()
Statistics(user=lp_students[1][4], exercise=exercises['en-lecture'], data='{"multi":"false","time":"89","success":"33","failure":"67"}').save()

Statistics(user=lp_students[1][5], exercise=exercises['maths-additions'], data='{"multi":"true","time":"86","success":"6","failure":"4"}').save()
Statistics(user=lp_students[1][5], exercise=exercises['maths-soustractions'], data='{"multi":"true","time":"132","success":"8","failure":"2"}').save()
Statistics(user=lp_students[1][5], exercise=exercises['maths-geometrie'], data='{"multi":"false","time":"57","success":"7","failure":"3"}').save()
Statistics(user=lp_students[1][5], exercise=exercises['fr-lecture'], data='{"multi":"true","time":"59","success":"7","failure":"3"}').save()
Statistics(user=lp_students[1][5], exercise=exercises['en-lecture'], data='{"multi":"false","time":"219","success":"74","failure":"26"}').save()

Statistics(user=lp_students[1][6], exercise=exercises['maths-additions'], data='{"multi":"true","time":"90","success":"4","failure":"6"}').save()
Statistics(user=lp_students[1][6], exercise=exercises['maths-soustractions'], data='{"multi":"true","time":"100","success":"7","failure":"3"}').save()
Statistics(user=lp_students[1][6], exercise=exercises['maths-geometrie'], data='{"multi":"false","time":"61","success":"7","failure":"3"}').save()
Statistics(user=lp_students[1][6], exercise=exercises['fr-lecture'], data='{"multi":"true","time":"87","success":"8","failure":"2"}').save()
Statistics(user=lp_students[1][6], exercise=exercises['en-lecture'], data='{"multi":"false","time":"167","success":"61","failure":"39"}').save()

Statistics(user=lp_students[1][7], exercise=exercises['maths-additions'], data='{"multi":"true","time":"76","success":"10","failure":"0"}').save()
Statistics(user=lp_students[1][7], exercise=exercises['maths-soustractions'], data='{"multi":"true","time":"104","success":"10","failure":"0"}').save()
Statistics(user=lp_students[1][7], exercise=exercises['maths-geometrie'], data='{"multi":"false","time":"65","success":"9","failure":"1"}').save()
Statistics(user=lp_students[1][7], exercise=exercises['fr-lecture'], data='{"multi":"true","time":"57","success":"9","failure":"1"}').save()
Statistics(user=lp_students[1][7], exercise=exercises['en-lecture'], data='{"multi":"false","time":"178","success":"87","failure":"13"}').save()

Statistics(user=lp_students[1][8], exercise=exercises['maths-additions'], data='{"multi":"true","time":"82","success":"7","failure":"3"}').save()
Statistics(user=lp_students[1][8], exercise=exercises['maths-soustractions'], data='{"multi":"true","time":"125","success":"4","failure":"6"}').save()
Statistics(user=lp_students[1][8], exercise=exercises['maths-geometrie'], data='{"multi":"false","time":"61","success":"9","failure":"1"}').save()
Statistics(user=lp_students[1][8], exercise=exercises['fr-lecture'], data='{"multi":"true","time":"64","success":"9","failure":"1"}').save()
Statistics(user=lp_students[1][8], exercise=exercises['en-lecture'], data='{"multi":"false","time":"178","success":"86","failure":"14"}').save()

Statistics(user=lp_students[1][9], exercise=exercises['maths-additions'], data='{"multi":"true","time":"89","success":"4","failure":"6"}').save()
Statistics(user=lp_students[1][9], exercise=exercises['maths-soustractions'], data='{"multi":"true","time":"123","success":"5","failure":"5"}').save()
Statistics(user=lp_students[1][9], exercise=exercises['maths-geometrie'], data='{"multi":"false","time":"60","success":"6","failure":"4"}').save()
Statistics(user=lp_students[1][9], exercise=exercises['fr-lecture'], data='{"multi":"true","time":"69","success":"7","failure":"3"}').save()
Statistics(user=lp_students[1][9], exercise=exercises['en-lecture'], data='{"multi":"false","time":"264","success":"52","failure":"48"}').save()

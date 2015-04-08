#!/usr/bin/env python
from django.contrib.auth.models import User, Group
from backoffice.models import LPUser, SchoolClass

execfile("./init.py")

#password for users is "password"

#password for school classes is "password_class"

##
## Create teachers
##

teachers = []
lp_teachers = []

teachers.append(User(username='teacher-dev', email='teacher-dev@domain.com', password='pbkdf2_sha256$12000$d6vlMBAMnAYT$jnnaq7ea4XGw6oIAbEs1F4O+TEZfZABbuaAd6sZw28I=', is_active=True))
teachers[0].save()
teachers[0].groups.add(Group.objects.get(name='teachers'))
lp_teachers.append(LPUser())
lp_teachers[0].user = teachers[0]
lp_teachers[0].save()

teachers.append(User(username='teacher-dev2', email='teacher-dev2@domain.com', password='pbkdf2_sha256$12000$d6vlMBAMnAYT$jnnaq7ea4XGw6oIAbEs1F4O+TEZfZABbuaAd6sZw28I=', is_active=True))
teachers[1].save()
teachers[1].groups.add(Group.objects.get(name='teachers'))
lp_teachers.append(LPUser())
lp_teachers[1].user = teachers[1]
lp_teachers[1].save()

teachers.append(User(username='teacher-dev3', email='teacher-dev3@domain.com', password='pbkdf2_sha256$12000$d6vlMBAMnAYT$jnnaq7ea4XGw6oIAbEs1F4O+TEZfZABbuaAd6sZw28I=', is_active=True))
teachers[2].save()
teachers[2].groups.add(Group.objects.get(name='teachers'))
lp_teachers.append(LPUser())
lp_teachers[2].user = teachers[2]
lp_teachers[2].save()

##
## Create School classes
##

school_classes = []

school_classes.append(SchoolClass(name='Classe 1', school_name='Ecole primaire Montpellier', password='pbkdf2_sha256$12000$C4jsYralAzH5$64Wv3fsO5ubpaPZX1bQxm4aIFnyrBuw83nzhIpbgb4c='))
school_classes[0].save()
school_classes.append(SchoolClass(name='Classe 2', school_name='Ecole primaire Montpellier', password='pbkdf2_sha256$12000$C4jsYralAzH5$64Wv3fsO5ubpaPZX1bQxm4aIFnyrBuw83nzhIpbgb4c='))
school_classes[1].save()
school_classes.append(SchoolClass(name='Classe 3', school_name='Ecole primaire Montpellier', password='pbkdf2_sha256$12000$C4jsYralAzH5$64Wv3fsO5ubpaPZX1bQxm4aIFnyrBuw83nzhIpbgb4c='))
school_classes[2].save()
school_classes.append(SchoolClass(name='Classe 4', school_name='Ecole primaire Montpellier', password='pbkdf2_sha256$12000$C4jsYralAzH5$64Wv3fsO5ubpaPZX1bQxm4aIFnyrBuw83nzhIpbgb4c='))
school_classes[3].save()
school_classes.append(SchoolClass(name='Classe 5', school_name='Ecole primaire Montpellier', password='pbkdf2_sha256$12000$C4jsYralAzH5$64Wv3fsO5ubpaPZX1bQxm4aIFnyrBuw83nzhIpbgb4c='))
school_classes[4].save()
lp_teachers[0].school_class.add(school_classes[0])
lp_teachers[0].school_class.add(school_classes[2])
lp_teachers[0].school_class.add(school_classes[3])
lp_teachers[0].school_class.add(school_classes[4])
lp_teachers[1].school_class.add(school_classes[0])
lp_teachers[1].school_class.add(school_classes[1])

##
## Create students
##

students = []
lp_students = []

# Students for class 0
students.append([])
students[0].append(User(username='Lorem.Ipsum', email='student-dev@domain.com', password='pbkdf2_sha256$12000$d6vlMBAMnAYT$jnnaq7ea4XGw6oIAbEs1F4O+TEZfZABbuaAd6sZw28I=', is_active=True))
students[0][0].save()
students[0][0].groups.add(Group.objects.get(name='students'))
lp_students.append([])
lp_students[0].append(LPUser())
lp_students[0][0].user = students[0][0]
lp_students[0][0].save()
lp_students[0][0].school_class.add(school_classes[0])

students[0].append(User(username='Larry.Og', email='student-dev@domain.com', password='pbkdf2_sha256$12000$d6vlMBAMnAYT$jnnaq7ea4XGw6oIAbEs1F4O+TEZfZABbuaAd6sZw28I=', is_active=True))
students[0][1].save()
students[0][1].groups.add(Group.objects.get(name='students'))
lp_students.append([])
lp_students[0].append(LPUser())
lp_students[0][1].user = students[0][1]
lp_students[0][1].save()
lp_students[0][1].school_class.add(school_classes[0])

students[0].append(User(username='Lucien.Arthur', email='student-dev@domain.com', password='pbkdf2_sha256$12000$d6vlMBAMnAYT$jnnaq7ea4XGw6oIAbEs1F4O+TEZfZABbuaAd6sZw28I=', is_active=True))
students[0][2].save()
students[0][2].groups.add(Group.objects.get(name='students'))
lp_students.append([])
lp_students[0].append(LPUser())
lp_students[0][2].user = students[0][2]
lp_students[0][2].save()
lp_students[0][2].school_class.add(school_classes[0])

students[0].append(User(username='Abel.Marion', email='student-dev@domain.com', password='pbkdf2_sha256$12000$d6vlMBAMnAYT$jnnaq7ea4XGw6oIAbEs1F4O+TEZfZABbuaAd6sZw28I=', is_active=True))
students[0][3].save()
students[0][3].groups.add(Group.objects.get(name='students'))
lp_students.append([])
lp_students[0].append(LPUser())
lp_students[0][3].user = students[0][3]
lp_students[0][3].save()
lp_students[0][3].school_class.add(school_classes[0])

students[0].append(User(username='Claude.Blanchet', email='student-dev@domain.com', password='pbkdf2_sha256$12000$d6vlMBAMnAYT$jnnaq7ea4XGw6oIAbEs1F4O+TEZfZABbuaAd6sZw28I=', is_active=True))
students[0][4].save()
students[0][4].groups.add(Group.objects.get(name='students'))
lp_students.append([])
lp_students[0].append(LPUser())
lp_students[0][4].user = students[0][4]
lp_students[0][4].save()
lp_students[0][4].school_class.add(school_classes[0])

students[0].append(User(username='Thierry.Colbert', email='student-dev@domain.com', password='pbkdf2_sha256$12000$d6vlMBAMnAYT$jnnaq7ea4XGw6oIAbEs1F4O+TEZfZABbuaAd6sZw28I=', is_active=True))
students[0][5].save()
students[0][5].groups.add(Group.objects.get(name='students'))
lp_students.append([])
lp_students[0].append(LPUser())
lp_students[0][5].user = students[0][5]
lp_students[0][5].save()
lp_students[0][5].school_class.add(school_classes[0])

# Students for class 1
students.append([])
students[1].append(User(username='Marcel.Bonner', email='student-dev@domain.com', password='pbkdf2_sha256$12000$d6vlMBAMnAYT$jnnaq7ea4XGw6oIAbEs1F4O+TEZfZABbuaAd6sZw28I=', is_active=True))
students[1][0].save()
students[1][0].groups.add(Group.objects.get(name='students'))
lp_students.append([])
lp_students[1].append(LPUser())
lp_students[1][0].user = students[1][0]
lp_students[1][0].save()
lp_students[1][0].school_class.add(school_classes[1])

students[1].append(User(username='Ruben.Girard', email='student-dev@domain.com', password='pbkdf2_sha256$12000$d6vlMBAMnAYT$jnnaq7ea4XGw6oIAbEs1F4O+TEZfZABbuaAd6sZw28I=', is_active=True))
students[1][1].save()
students[1][1].groups.add(Group.objects.get(name='students'))
lp_students.append([])
lp_students[1].append(LPUser())
lp_students[1][1].user = students[1][1]
lp_students[1][1].save()
lp_students[1][1].school_class.add(school_classes[1])

# Students for class 2
students.append([])
lp_students.append([])

# Students for class 3
students.append([])
students[3].append(User(username='Pascal.Yount', email='student-dev@domain.com', password='pbkdf2_sha256$12000$d6vlMBAMnAYT$jnnaq7ea4XGw6oIAbEs1F4O+TEZfZABbuaAd6sZw28I=', is_active=True))
students[3][0].save()
students[3][0].groups.add(Group.objects.get(name='students'))
lp_students.append([])
lp_students[3].append(LPUser())
lp_students[3][0].user = students[3][0]
lp_students[3][0].save()
lp_students[3][0].school_class.add(school_classes[3])

students[3].append(User(username='Benoit.Bonhomme', email='student-dev@domain.com', password='pbkdf2_sha256$12000$d6vlMBAMnAYT$jnnaq7ea4XGw6oIAbEs1F4O+TEZfZABbuaAd6sZw28I=', is_active=True))
students[3][1].save()
students[3][1].groups.add(Group.objects.get(name='students'))
lp_students.append([])
lp_students[3].append(LPUser())
lp_students[3][1].user = students[3][1]
lp_students[3][1].save()
lp_students[3][1].school_class.add(school_classes[3])

students[3].append(User(username='Narcisse.Samuel', email='student-dev@domain.com', password='pbkdf2_sha256$12000$d6vlMBAMnAYT$jnnaq7ea4XGw6oIAbEs1F4O+TEZfZABbuaAd6sZw28I=', is_active=True))
students[3][2].save()
students[3][2].groups.add(Group.objects.get(name='students'))
lp_students.append([])
lp_students[3].append(LPUser())
lp_students[3][2].user = students[3][2]
lp_students[3][2].save()
lp_students[3][2].school_class.add(school_classes[3])

# Students for class 4
students.append([])
students[4].append(User(username='Thomas.Fortier', email='student-dev@domain.com', password='pbkdf2_sha256$12000$d6vlMBAMnAYT$jnnaq7ea4XGw6oIAbEs1F4O+TEZfZABbuaAd6sZw28I=', is_active=True))
students[4][0].save()
students[4][0].groups.add(Group.objects.get(name='students'))
lp_students.append([])
lp_students[4].append(LPUser())
lp_students[4][0].user = students[4][0]
lp_students[4][0].save()
lp_students[4][0].school_class.add(school_classes[4])

students[4].append(User(username='Mathis.Larue', email='student-dev@domain.com', password='pbkdf2_sha256$12000$d6vlMBAMnAYT$jnnaq7ea4XGw6oIAbEs1F4O+TEZfZABbuaAd6sZw28I=', is_active=True))
students[4][1].save()
students[4][1].groups.add(Group.objects.get(name='students'))
lp_students.append([])
lp_students[4].append(LPUser())
lp_students[4][1].user = students[4][1]
lp_students[4][1].save()
lp_students[4][1].school_class.add(school_classes[4])

students[4].append(User(username='Corneille.Roche', email='student-dev@domain.com', password='pbkdf2_sha256$12000$d6vlMBAMnAYT$jnnaq7ea4XGw6oIAbEs1F4O+TEZfZABbuaAd6sZw28I=', is_active=True))
students[4][2].save()
students[4][2].groups.add(Group.objects.get(name='students'))
lp_students.append([])
lp_students[4].append(LPUser())
lp_students[4][2].user = students[4][2]
lp_students[4][2].save()
lp_students[4][2].school_class.add(school_classes[4])

students[4].append(User(username='Quentin.Herriot', email='student-dev@domain.com', password='pbkdf2_sha256$12000$d6vlMBAMnAYT$jnnaq7ea4XGw6oIAbEs1F4O+TEZfZABbuaAd6sZw28I=', is_active=True))
students[4][3].save()
students[4][3].groups.add(Group.objects.get(name='students'))
lp_students.append([])
lp_students[4].append(LPUser())
lp_students[4][3].user = students[4][3]
lp_students[4][3].save()
lp_students[4][3].school_class.add(school_classes[4])

students[4].append(User(username='Yannic.Richard', email='student-dev@domain.com', password='pbkdf2_sha256$12000$d6vlMBAMnAYT$jnnaq7ea4XGw6oIAbEs1F4O+TEZfZABbuaAd6sZw28I=', is_active=True))
students[4][4].save()
students[4][4].groups.add(Group.objects.get(name='students'))
lp_students.append([])
lp_students[4].append(LPUser())
lp_students[4][4].user = students[4][4]
lp_students[4][4].save()
lp_students[4][4].school_class.add(school_classes[4])

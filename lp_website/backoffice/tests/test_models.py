# -*- coding: UTF-8 -*-
from django.test import TestCase
from django.contrib.auth.models import User
from backoffice.models import Subject, Exercise, SchoolClass, SubjectConfig, ExerciseConfig, LPUser, Statistics

## Classe SubjectTest\n
# Classe de test pour le model Subject
class SubjectTest(TestCase):
    ## Creation d'un Subject valide
    def setUp(self):
        Subject.objects.create(name='Anglais', data='{}')

    ## Test de récupération et d'affichage de l'objet Subject
    def test_Subject_str(self):
        subject = Subject.objects.get(name='Anglais')
        self.assertEqual(subject.__str__(), 'Anglais')


## Classe ExerciseTest\n
# Classe de test pour le model Exercise
class ExerciseTest(TestCase):
    ## Creation d'un Exercise valide
    def setUp(self):
        subject = Subject.objects.create(name='Anglais', data='{}')
        Exercise.objects.create(name='Lecture', subject=subject, data='{}')

    ## Test de récupération et d'affichage de l'objet Exercise
    def test_Exercise_str(self):
        exercise = Exercise.objects.get(name='Lecture')
        self.assertEqual(exercise.__str__(), 'Lecture')


## Classe SchoolClassTest\n
# Classe de test pour le model SchoolClass
class SchoolClassTest(TestCase):
    ## Creation d'un SchoolClass valide
    def setUp(self):
        SchoolClass.objects.create(name='CP', school_name='Paul Valery', password='password', data='{}')

    ## Test de récupération et d'affichage de l'objet SchoolClass
    def test_SchoolClass_str(self):
        school_class = SchoolClass.objects.get(name='CP')
        self.assertEqual(school_class.__str__(), "Class 'CP' from school 'Paul Valery'")


## Classe SubjectConfigTest\n
# Classe de test pour le model SubjectConfig
class SubjectConfigTest(TestCase):
    ## Creation d'un SubjectConfig valide
    def setUp(self):
        subject = Subject.objects.create(name='Anglais', data='{}')
        school_class = SchoolClass.objects.create(name='CP', school_name='Paul Valery', password='password', data='{}')
        SubjectConfig.objects.create(name='Configuration de test', subject=subject, school_class=school_class, data='{}')

    ## Test de récupération et d'affichage de l'objet SubjectConfig
    def test_SubjectConfig_str(self):
        subject_config = SubjectConfig.objects.get(name='Configuration de test')
        self.assertEqual(subject_config.__str__(), "Config Anglais for Class 'CP' from school 'Paul Valery'")


## Classe ExerciseConfigTest\n
# Classe de test pour le model ExerciseConfig
class ExerciseConfigTest(TestCase):
    ## Creation d'un ExerciseConfig valide
    def setUp(self):
        subject = Subject.objects.create(name='Anglais', data='{}')
        exercise = Exercise.objects.create(name='Lecture', subject=subject, data='{}')
        school_class = SchoolClass.objects.create(name='CP', school_name='Paul Valery', password='password', data='{}')
        ExerciseConfig.objects.create(name='Configuration de test', exercise=exercise, school_class=school_class, data='{}')

    ## Test de récupération et d'affichage de l'objet ExerciseConfig
    def test_ExerciseConfig_str(self):
        exercise_config = ExerciseConfig.objects.get(name='Configuration de test')
        self.assertEqual(exercise_config.__str__(), "Config Lecture for Class 'CP' from school 'Paul Valery'")


## Classe LPUserTest\n
# Classe de test pour le model LPUser
class LPUserTest(TestCase):
    ## Creation d'un LPUser valide
    def setUp(self):
        user = User.objects.create(username='teacher1', email='teacher1@domain.com', password='pbkdf2_sha256$12000$d6vlMBAMnAYT$jnnaq7ea4XGw6oIAbEs1F4O+TEZfZABbuaAd6sZw28I=', is_active=True)
        LPUser.objects.create(user=user, data='{}')

    ## Test de récupération et d'affichage de l'objet LPUser
    def test_LPUser_str(self):
        lp_user = LPUser.objects.get(user__username='teacher1')
        self.assertEqual(lp_user.__str__(), 'teacher1')


## Classe StatisticsTest\n
# Classe de test pour le model Statistics
class StatisticsTest(TestCase):
    ## Creation d'un Statistics valide
    def setUp(self):
        user = User.objects.create(username='teacher1', email='teacher1@domain.com', password='pbkdf2_sha256$12000$d6vlMBAMnAYT$jnnaq7ea4XGw6oIAbEs1F4O+TEZfZABbuaAd6sZw28I=', is_active=True)
        lp_user = LPUser.objects.create(user=user, data='{}')
        subject = Subject.objects.create(name='Anglais', data='{}')
        exercise = Exercise.objects.create(name='Lecture', subject=subject, data='{}')
        Statistics.objects.create(user=lp_user, exercise=exercise, data='{success:true}')

    ## Test de récupération et d'affichage de l'objet Statistics
    def test_Statistics_str(self):
        stat = Statistics.objects.get(user__user__username='teacher1')
        self.assertEqual(stat.__str__(), "Statistics for 'teacher1': {success:true}")

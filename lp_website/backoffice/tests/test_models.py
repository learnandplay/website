# -*- coding: UTF-8 -*-
from django.test import TestCase
from django.contrib.auth.models import User
from backoffice.models import Subject, Exercise, SchoolClass, SubjectConfig, ExerciseConfig, LPUser, Statistics

class SubjectTest(TestCase):
    def setUp(self):
        Subject.objects.create(name='Anglais', data='{}')

    def test_Subject_str(self):
        subject = Subject.objects.get(name='Anglais')
        self.assertEqual(subject.__str__(), 'Anglais')


class ExerciseTest(TestCase):
    def setUp(self):
        subject = Subject.objects.create(name='Anglais', data='{}')
        Exercise.objects.create(name='Lecture', subject=subject, data='{}')

    def test_Exercise_str(self):
        exercise = Exercise.objects.get(name='Lecture')
        self.assertEqual(exercise.__str__(), 'Lecture')


class SchoolClassTest(TestCase):
    def setUp(self):
        SchoolClass.objects.create(name='CP', school_name='Paul Valery', password='password', data='{}')

    def test_SchoolClass_str(self):
        school_class = SchoolClass.objects.get(name='CP')
        self.assertEqual(school_class.__str__(), "Class 'CP' from school 'Paul Valery'")


class SubjectConfigTest(TestCase):
    def setUp(self):
        subject = Subject.objects.create(name='Anglais', data='{}')
        school_class = SchoolClass.objects.create(name='CP', school_name='Paul Valery', password='password', data='{}')
        SubjectConfig.objects.create(name='Configuration de test', subject=subject, school_class=school_class, data='{}')

    def test_SubjectConfig_str(self):
        subject_config = SubjectConfig.objects.get(name='Configuration de test')
        self.assertEqual(subject_config.__str__(), "Config Anglais for Class 'CP' from school 'Paul Valery'")


class ExerciseConfigTest(TestCase):
    def setUp(self):
        subject = Subject.objects.create(name='Anglais', data='{}')
        exercise = Exercise.objects.create(name='Lecture', subject=subject, data='{}')
        school_class = SchoolClass.objects.create(name='CP', school_name='Paul Valery', password='password', data='{}')
        ExerciseConfig.objects.create(name='Configuration de test', exercise=exercise, school_class=school_class, data='{}')

    def test_ExerciseConfig_str(self):
        exercise_config = ExerciseConfig.objects.get(name='Configuration de test')
        self.assertEqual(exercise_config.__str__(), "Config Lecture for Class 'CP' from school 'Paul Valery'")


class LPUserTest(TestCase):
    def setUp(self):
        user = User.objects.create(username='teacher1', email='teacher1@domain.com', password='pbkdf2_sha256$12000$d6vlMBAMnAYT$jnnaq7ea4XGw6oIAbEs1F4O+TEZfZABbuaAd6sZw28I=', is_active=True)
        LPUser.objects.create(user=user, data='{}')

    def test_LPUser_str(self):
        lp_user = LPUser.objects.get(user__username='teacher1')
        self.assertEqual(lp_user.__str__(), 'teacher1')


class StatisticsTest(TestCase):
    def setUp(self):
        user = User.objects.create(username='teacher1', email='teacher1@domain.com', password='pbkdf2_sha256$12000$d6vlMBAMnAYT$jnnaq7ea4XGw6oIAbEs1F4O+TEZfZABbuaAd6sZw28I=', is_active=True)
        lp_user = LPUser.objects.create(user=user, data='{}')
        subject = Subject.objects.create(name='Anglais', data='{}')
        exercise = Exercise.objects.create(name='Lecture', subject=subject, data='{}')
        Statistics.objects.create(user=lp_user, exercise=exercise, data='{success:true}')

    def test_Statistics_str(self):
        stat = Statistics.objects.get(user__user__username='teacher1')
        self.assertEqual(stat.__str__(), "Statistics for 'teacher1': {success:true}")

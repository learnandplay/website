# -*- coding: UTF-8 -*-
from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse
from backoffice.forms import ClassForm

## Classe IndexTest\n
# Classe de test pour la view index
class IndexTest(TestCase):
    fixtures = ['demo_dump.json']
    ## Préparation du client de test et login avec un compte professeur
    def setUp(self):
        self.client = Client()
        self.client.login(username='teacher1', password='password')

    ## Test d'une requete GET valide. Doit renvoyer un code 200
    def test_index(self):
        response = self.client.get(reverse('backoffice:index'))
        self.assertEqual(response.status_code, 200)


## Classe TeachersRequiredTest\n
# Classe de test pour la view teachers_required
class TeachersRequiredTest(TestCase):
    fixtures = ['demo_dump.json']
    ## Préparation du client de test et login avec un compte élève
    def setUp(self):
        self.client = Client()
        self.client.login(username='Benjamin.Boisset', password='password')

    ## Test d'une requete GET valide. Doit renvoyer un code 200
    def test_teachers_required(self):
        response = self.client.get(reverse('backoffice:teachers_required'))
        self.assertEqual(response.status_code, 200)


## Classe MyClassesTest\n
# Classe de test pour la view my_classes
class MyClassesTest(TestCase):
    fixtures = ['demo_dump.json']
    ## Préparation du client de test et login avec un compte professeur
    def setUp(self):
        self.client = Client()
        self.client.login(username='teacher1', password='password')

    ## Test d'une requete GET valide. Doit renvoyer un code 200
    def test_my_classes(self):
        response = self.client.get(reverse('backoffice:my_classes'))
        self.assertEqual(response.status_code, 200)


## Classe EditClassTest\n
# Classe de test pour les views create_class et edit_class
class EditClassTest(TestCase):
    fixtures = ['demo_dump.json']
    ## Préparation du client de test et login avec un compte professeur
    def setUp(self):
        self.client = Client()
        self.client.login(username='teacher1', password='password')

    ## Test d'une requete POST valide pour creer une classe. Doit renvoyer un code 200
    def test_create_class(self):
        pass

    ## Test d'une requete POST valide pour editer une classe. Doit renvoyer un code 200
    def test_edit_class(self):
        pass

    ## Test d'une requete POST invalide: utilisation d'un class_id inexistant. Doit renvoyer un code 400
    def test_edit_class_wrong_id(self):
        class_id = 420
        response = self.client.post(reverse('backoffice:edit_class', kwargs={'id':class_id}))
        self.assertEqual(response.status_code, 400)

## Classe MyStudentsTest\n
# Classe de test pour les views my_students_default et my_students
class MyStudentsTest(TestCase):
    fixtures = ['demo_dump.json']
    ## Préparation du client de test et login avec un compte professeur
    def setUp(self):
        self.client = Client()
        self.client.login(username='teacher1', password='password')

    ## Test d'une requete GET valide pour voir tous les etudiants. Doit renvoyer un code 200
    def test_my_students_default(self):
        response = self.client.get(reverse('backoffice:my_students_default'))
        self.assertEqual(response.status_code, 200)

    ## Test d'une requete GET valide pour voir tous les etudiants d'une classe. Doit renvoyer un code 200
    def test_my_students(self):
        class_id = 1
        response = self.client.get(reverse('backoffice:my_students', kwargs={'class_id':class_id}))
        self.assertEqual(response.status_code, 200)


## Classe EditStudentTest\n
# Classe de test pour les views create_student et edit_student
class EditStudentTest(TestCase):
    fixtures = ['demo_dump.json']
    ## Préparation du client de test et login avec un compte professeur
    def setUp(self):
        self.client = Client()
        self.client.login(username='teacher1', password='password')

    ## Test d'une requete POST valide pour creer un élève. Doit renvoyer un code 200
    def test_create_student(self):
        pass

    ## Test d'une requete POST valide pour éditer un élève. Doit renvoyer un code 200
    def test_edit_student(self):
        pass

    ## Test d'une requete POST invalide: utilisation d'un id inexistant. Doit renvoyer un code 400
    def test_edit_student_wrong_id(self):
        student_id = 420
        class_id = 1
        response = self.client.post(reverse('backoffice:edit_student', kwargs={'id':student_id, 'class_id':class_id}))
        self.assertEqual(response.status_code, 400)


## Classe ClassAdministratorsTest\n
# Classe de test pour la view class_administrators
class ClassAdministratorsTest(TestCase):
    fixtures = ['demo_dump.json']
    ## Préparation du client de test et login avec un compte professeur
    def setUp(self):
        self.client = Client()
        self.client.login(username='teacher1', password='password')

    ## Test d'une requete GET valide. Doit renvoyer un code 200
    def test_class_administrators(self):
        class_id = 1
        response = self.client.get(reverse('backoffice:class_administrators', kwargs={'class_id':class_id}))
        self.assertEqual(response.status_code, 200)

    ## Test d'une requete GET invalide: utilisation d'un class_id inexistant. Doit renvoyer un code 400
    def test_class_administrators_wrong_id(self):
        class_id = 420
        response = self.client.get(reverse('backoffice:class_administrators', kwargs={'class_id':class_id}))
        self.assertEqual(response.status_code, 400)


## Classe EditProfileTest\n
# Classe de test pour la view edit_profile
class EditProfileTest(TestCase):
    fixtures = ['demo_dump.json']
    ## Préparation du client de test et login avec un compte professeur
    def setUp(self):
        self.client = Client()
        self.client.login(username='teacher1', password='password')

    ## Test d'une requete POST valide pour éditer le profil. Doit renvoyer un code 200
    def test_edit_profile(self):
        pass

    ## Test d'une requete POST invalide pour éditer le profil. Doit renvoyer un code 400
    def test_edit_profile_error(self):
        pass


## Classe StatisticsTest\n
# Classe de test pour la view statistics
class StatisticsTest(TestCase):
    fixtures = ['demo_dump.json']
    ## Préparation du client de test et login avec un compte professeur
    def setUp(self):
        self.client = Client()
        self.client.login(username='teacher1', password='password')

    ## Test d'une requete GET valide. Doit renvoyer un code 200
    def test_statistics(self):
        response = self.client.get(reverse('backoffice:statistics'))
        self.assertEqual(response.status_code, 200)

## Classe ConfigurationTest\n
# Classe de test pour la view configuration
class ConfigurationTest(TestCase):
    fixtures = ['demo_dump.json']
    ## Préparation du client de test et login avec un compte professeur
    def setUp(self):
        self.client = Client()
        self.client.login(username='teacher1', password='password')

    ## Test d'une requete GET valide. Doit renvoyer un code 200
    def test_configuration(self):
        response = self.client.get(reverse('backoffice:configuration'))
        self.assertEqual(response.status_code, 200)


## Classe SubjectConfigurationTest\n
# Classe de test pour la view subject_configuration
class SubjectConfigurationTest(TestCase):
    fixtures = ['demo_dump.json']
    ## Préparation du client de test et login avec un compte professeur
    def setUp(self):
        self.client = Client()
        self.client.login(username='teacher1', password='password')

    ## Test d'une requete GET valide. Doit renvoyer un code 200
    def test_subject_configuration(self):
        subject_config_id = 1
        response = self.client.get(reverse('backoffice:subject_configuration', kwargs={'subject_id':subject_config_id}))
        self.assertEqual(response.status_code, 200)

    ## Test d'une requete GET invalide: utilisation d'un subject_id inexistant. Doit renvoyer un code 400
    def test_subject_configuration_wrong_id(self):
        subject_config_id = 420
        response = self.client.get(reverse('backoffice:subject_configuration', kwargs={'subject_id':subject_config_id}))
        self.assertEqual(response.status_code, 400)


## Classe ExerciseConfigurationTest\n
# Classe de test pour la view exercise_configuration
class ExerciseConfigurationTest(TestCase):
    fixtures = ['demo_dump.json']
    ## Préparation du client de test et login avec un compte professeur
    def setUp(self):
        self.client = Client()
        self.client.login(username='teacher1', password='password')

    ## Test d'une requete GET valide. Doit renvoyer un code 200
    def test_exercise_configuration(self):
        exercise_config_id = 1
        response = self.client.get(reverse('backoffice:exercise_configuration', kwargs={'exercise_id':exercise_config_id}))
        self.assertEqual(response.status_code, 200)

    ## Test d'une requete GET invalide: utilisation d'un exercise_id inexistant. Doit renvoyer un code 400
    def test_exercise_configuration_wrong_id(self):
        exercise_config_id = 420
        response = self.client.get(reverse('backoffice:exercise_configuration', kwargs={'exercise_id':exercise_config_id}))
        self.assertEqual(response.status_code, 400)


## Classe MyconfigurationsTest\n
# Classe de test pour la view my_configurations
class MyconfigurationsTest(TestCase):
    fixtures = ['demo_dump.json']
    ## Préparation du client de test et login avec un compte professeur
    def setUp(self):
        self.client = Client()
        self.client.login(username='teacher1', password='password')

    ## Test d'une requete GET valide. Doit renvoyer un code 200
    def test_my_configurations(self):
        response = self.client.get(reverse('backoffice:my_configurations'))
        self.assertEqual(response.status_code, 200)


## Classe ViewProfileTest\n
# Classe de test pour la view view_profile
class ViewProfileTest(TestCase):
    fixtures = ['demo_dump.json']
    ## Préparation du client de test et login avec un compte professeur
    def setUp(self):
        self.client = Client()
        self.client.login(username='teacher1', password='password')

    ## Test d'une requete GET valide. Doit renvoyer un code 200
    def test_view_profile(self):
        response = self.client.get(reverse('backoffice:view_profile', kwargs={'user_id':3}))
        self.assertEqual(response.status_code, 200)

    ## Test d'une requete GET invalide: utilisation d'un user_id invalide. Doit renvoyer un code 400
    def test_view_profile(self):
        response = self.client.get(reverse('backoffice:view_profile', kwargs={'user_id':420}))
        self.assertEqual(response.status_code, 400)

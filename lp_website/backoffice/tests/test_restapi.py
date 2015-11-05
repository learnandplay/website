# -*- coding: UTF-8 -*-
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from django.core.urlresolvers import reverse
import json
from pprint import pprint

apiResponses = {
    'get_classes': '[{"id":1,"name":"CP 1","school_name":"Ecole Albert Camus","ip":""},{"id":2,"name":"CP 2","school_name":"Ecole Albert Camus","ip":""}]',
    'get_students': '[{"id":11,"username":"Anthony.Payet"},{"id":3,"username":"Benjamin.Boisset"},{"id":4,"username":"Julien.Lefebvre"},{"id":10,"username":"Laura.Moulin"},{"id":12,"username":"Lea.Martinez"},{"id":9,"username":"Lucie.Masson"},{"id":5,"username":"Manon.Durand"},{"id":7,"username":"Marie.Petit"},{"id":6,"username":"Pierre.Moreau"},{"id":8,"username":"Romain.Brunet"}]',
    'get_subject_config': '{"id":2,"name":"Maths d\xc3\xa9bloqu\xc3\xa9es","start_date":null,"end_date":null,"data":"{\\"accessible\\": true, \\"config_name\\": \\"Maths d\\\\u00e9bloqu\\\\u00e9es\\", \\"school_class\\": \\"2\\"}","reference":"maths"}',
    'get_exercise_config': '{"id":1,"name":"Config anglais lecture bloqu\xc3\xa9","start_date":null,"end_date":null,"data":"{\\"accessible\\": false, \\"config_name\\": \\"Config anglais lecture bloqu\\\\u00e9\\", \\"school_class\\": \\"2\\"}","reference":"en-lecture"}',
}

## Classe RestApiTokenAuthTest\n
# Classe de test pour la recuperation de token via rest_framework_jwt.views.obtain_jwt_token
class RestApiTokenAuthTest(TestCase):
    fixtures = ['demo_dump.json']
    ## Préparation du client de test
    def setUp(self):
        self.client = APIClient()

    ## Test d'une requete POST valide pour la recuperation du Json Web Token. Doit renvoyer un code 200
    def test_get_token_auth(self):
        response = self.client.post(reverse('backoffice:restapi-token-auth'), json.dumps({'username': 'teacher1', 'password': 'password'}), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    ## Test d'une requete POST invalide pour la recuperation du Json Web Token: Mauvais identifiants. Doit renvoyer un code 400
    def test_token_auth_wrong_credentials(self):
        response = self.client.post(reverse('backoffice:restapi-token-auth'), json.dumps({'username': 'teacher120', 'password': 'password42'}), content_type='application/json')
        self.assertEqual(response.status_code, 400)


## Classe RestApiGetClassesTest\n
# Classe de test pour la view GetClasses
class RestApiGetClassesTest(TestCase):
    fixtures = ['demo_dump.json']
    ## Préparation du client de test
    def setUp(self):
        self.client = APIClient()
        user = User.objects.get(username='teacher1')
        self.client.force_authenticate(user=user)

    ## Test d'une requete GET valide. Doit renvoyer un code 200
    def test_get_classes(self):
        response = self.client.get(reverse('backoffice:restapi-classes'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, apiResponses['get_classes'])

## Classe RestApiGetStudentsTest\n
# Classe de test pour la view GetStudents
class RestApiGetStudentsTest(TestCase):
    fixtures = ['demo_dump.json']
    ## Préparation du client de test
    def setUp(self):
        self.client = APIClient()
        user = User.objects.get(username='teacher1')
        self.client.force_authenticate(user=user)

    ## Test d'une requete GET valide. Doit renvoyer un code 200
    def test_get_students(self):
        class_id = 1
        response = self.client.get(reverse('backoffice:restapi-students', kwargs={'class_id':class_id}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, apiResponses['get_students'])

    ## Test d'une requete GET invalide: Utilisation d'un class_id invalide. Doit renvoyer un code 400
    def test_get_students_invalid_class_id(self):
        class_id = 420
        response = self.client.get(reverse('backoffice:restapi-students', kwargs={'class_id':class_id}))
        self.assertEqual(response.status_code, 400)


## Classe RestApiGetSubjectConfigTest\n
# Classe de test pour la view GetSubjectConfig
class RestApiGetSubjectConfigTest(TestCase):
    fixtures = ['demo_dump.json']
    ## Préparation du client de test
    def setUp(self):
        self.client = APIClient()
        user = User.objects.get(username='teacher1')
        self.client.force_authenticate(user=user)

    ## Test d'une requete GET valide. Doit renvoyer un code 200
    def test_get_subject_config(self):
        class_id = 2
        ref = 'maths'
        response = self.client.get(reverse('backoffice:restapi-subject-config', kwargs={'class_id':class_id,'ref':ref}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, apiResponses['get_subject_config'])

    ## Test d'une requete GET invalide: utilisation d'un class_id invalide. Doit renvoyer un code 400
    def test_get_subject_config_invalid_class_id(self):
        class_id = 420
        ref = 'maths'
        response = self.client.get(reverse('backoffice:restapi-subject-config', kwargs={'class_id':class_id,'ref':ref}))
        self.assertEqual(response.status_code, 400)

    ## Test d'une requete GET invalide: utilisation d'une ref invalide. Doit renvoyer un code 400
    def test_get_subject_config_invalid_ref(self):
        class_id = 2
        ref = 'toto'
        response = self.client.get(reverse('backoffice:restapi-subject-config', kwargs={'class_id':class_id,'ref':ref}))
        self.assertEqual(response.status_code, 400)


## Classe RestApiGetExerciseConfigTest\n
# Classe de test pour la view GetExerciseConfig
class RestApiGetExerciseConfigTest(TestCase):
    fixtures = ['demo_dump.json']
    ## Préparation du client de test
    def setUp(self):
        self.client = APIClient()
        user = User.objects.get(username='teacher1')
        self.client.force_authenticate(user=user)

    ## Test d'une requete GET valide. Doit renvoyer un code 200
    def test_get_exercise_config(self):
        class_id = 2
        ref = 'en-lecture'
        response = self.client.get(reverse('backoffice:restapi-exercise-config', kwargs={'class_id':class_id,'ref':ref}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, apiResponses['get_exercise_config'])

    ## Test d'une requete GET invalide: utilisation d'un class_id invalide. Doit renvoyer un code 400
    def test_get_exercise_config_invalid_class_id(self):
        class_id = 420
        ref = 'en-lecture'
        response = self.client.get(reverse('backoffice:restapi-exercise-config', kwargs={'class_id':class_id,'ref':ref}))
        self.assertEqual(response.status_code, 400)

    ## Test d'une requete GET invalide: utilisation d'une ref invalide. Doit renvoyer un code 400
    def test_get_exercise_config_invalid_ref(self):
        class_id = 2
        ref = 'toto'
        response = self.client.get(reverse('backoffice:restapi-exercise-config', kwargs={'class_id':class_id,'ref':ref}))
        self.assertEqual(response.status_code, 400)

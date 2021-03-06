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
    'get_subject_config': '{"id":1,"name":"Maths d\xc3\xa9bloqu\xc3\xa9es","data":"{\\"accessible\\": true, \\"config_name\\": \\"Maths d\\\\u00e9bloqu\\\\u00e9es\\", \\"school_class\\": \\"2\\"}","reference":"maths"}',
    'get_exercise_config': '{"id":1,"name":"Config anglais lecture bloqu\xc3\xa9","data":"{\\"accessible\\": false, \\"config_name\\": \\"Config anglais lecture bloqu\\\\u00e9\\", \\"school_class\\": \\"2\\"}","reference":"en-lecture"}',
    'post_exercise_stat': '{"result":"success"}',
    'get_if_first_exercise_use_true' : '{"first_use":"true"}',
    'get_if_first_exercise_use_false' : '{"first_use":"false"}',
    'get_if_first_subject_use_true' : '{"first_use":"true"}',
    'get_if_first_subject_use_false' : '{"first_use":"false"}',
    'post_save_ip': '{"result":"success"}',
    'get_user_data': '{"credits":42}',
    'get_user_data_empty': '{}',
    'post_user_datas': '{"result":"success"}'
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

## Classe RestApiPostExerciseStatTest\n
# Classe de test pour la view PostExerciseStat
class RestApiPostExerciseStatTest(TestCase):
    fixtures = ['demo_dump.json']
    ## Préparation du client de test
    def setUp(self):
        self.client = APIClient()
        user = User.objects.get(username='teacher1')
        self.client.force_authenticate(user=user)

    ## Test d'une requete POST valide. Doit renvoyer un code 200
    def test_post_exercise_stat(self):
        reference = 'maths-geometrie'
        user_id = 5
        data = {"multi":"true","time":"79","success":"8","failure":"2"}
        response = self.client.post(reverse('backoffice:restapi-save-exercise-stat'), json.dumps({'reference':reference,'user_id':user_id,'data':data}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, apiResponses['post_exercise_stat'])

    ## Test d'une requete POST invalide: utilisation d'une reference invalide. Doit renvoyer un code 400
    def test_post_invalid_reference(self):
        reference = 'abcd'
        user_id = 5
        data = {"multi":"true","time":"79","success":"8","failure":"2"}
        response = self.client.post(reverse('backoffice:restapi-save-exercise-stat'), json.dumps({'reference':reference,'user_id':user_id,'data':data}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 400)

    ## Test d'une requete POST invalide: reference manquante. Doit renvoyer un code 400
    def test_post_missing_reference(self):
        user_id = 5
        data = {"multi":"true","time":"79","success":"8","failure":"2"}
        response = self.client.post(reverse('backoffice:restapi-save-exercise-stat'), json.dumps({'user_id':user_id,'data':data}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 400)

    ## Test d'une requete POST invalide: utilisation d'un user_id invalide. Doit renvoyer un code 400
    def test_post_invalid_user_id(self):
        reference = 'maths-geometrie'
        user_id = 420
        data = {"multi":"true","time":"79","success":"8","failure":"2"}
        response = self.client.post(reverse('backoffice:restapi-save-exercise-stat'), json.dumps({'reference':reference,'user_id':user_id,'data':data}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 400)

    ## Test d'une requete POST invalide: user_id manquant. Doit renvoyer un code 400
    def test_post_missing_user_id(self):
        reference = 'maths-geometrie'
        data = {"multi":"true","time":"79","success":"8","failure":"2"}
        response = self.client.post(reverse('backoffice:restapi-save-exercise-stat'), json.dumps({'reference':reference,'data':data}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 400)

    ## Test d'une requete POST invalide: data manquante. Doit renvoyer un code 400
    def test_post_missing_data(self):
        reference = 'maths-geometrie'
        user_id = 5
        response = self.client.post(reverse('backoffice:restapi-save-exercise-stat'), json.dumps({'reference':reference,'user_id':user_id}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 400)

## Classe RestApiGetIfFirstExerciseUseTest\n
# Classe de test pour la view GetIfFirstExerciseUse
class RestApiGetIfFirstExerciseUseTest(TestCase):
    fixtures = ['demo_dump.json']
    ## Préparation du client de test
    def setUp(self):
        self.client = APIClient()
        user = User.objects.get(username='teacher1')
        self.client.force_authenticate(user=user)

    ## Test d'une requete GET valide. Doit renvoyer un code 200
    def test_get_exercise_first_use_true(self):
        user_id = 4
        ref = 'fr-lecture'
        response = self.client.get(reverse('backoffice:restapi-is-first-exercise-use', kwargs={'user_id':user_id,'ref':ref}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, apiResponses['get_if_first_exercise_use_true'])

    ## Test d'une requete GET valide. Doit renvoyer un code 200
    def test_get_exercise_first_use_false(self):
        user_id = 4
        ref = 'maths-additions'
        response = self.client.get(reverse('backoffice:restapi-is-first-exercise-use', kwargs={'user_id':user_id,'ref':ref}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, apiResponses['get_if_first_exercise_use_false'])

    ## Test d'une requete GET invalide: utilisation d'un user_id invalide. Doit renvoyer un code 400
    def test_get_exercise_first_use_wrong_user_id(self):
        user_id = 420
        ref = 'fr-lecture'
        response = self.client.get(reverse('backoffice:restapi-is-first-exercise-use', kwargs={'user_id':user_id,'ref':ref}))
        self.assertEqual(response.status_code, 400)

    ## Test d'une requete GET invalide: utilisation d'une reference invalide. Doit renvoyer un code 400
    def test_get_exercise_fisrt_use_wrong_reference(self):
        user_id = 4
        ref = 'abcd'
        response = self.client.get(reverse('backoffice:restapi-is-first-exercise-use', kwargs={'user_id':user_id,'ref':ref}))
        self.assertEqual(response.status_code, 400)

## Classe RestApiGetIfFirstSubjectUseTest\n
# Classe de test pour la view GetIfFirstSubjectUse
class RestApiGetIfFirstSubjectUseTest(TestCase):
    fixtures = ['demo_dump.json']
    ## Préparation du client de test
    def setUp(self):
        self.client = APIClient()
        user = User.objects.get(username='teacher1')
        self.client.force_authenticate(user=user)

    ## Test d'une requete GET valide. Doit renvoyer un code 200
    def test_get_subject_first_use_true(self):
        user_id = 4
        ref = 'fr'
        response = self.client.get(reverse('backoffice:restapi-is-first-subject-use', kwargs={'user_id':user_id,'ref':ref}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, apiResponses['get_if_first_subject_use_true'])

    ## Test d'une requete GET valide. Doit renvoyer un code 200
    def test_get_subject_first_use_false(self):
        user_id = 4
        ref = 'maths'
        response = self.client.get(reverse('backoffice:restapi-is-first-subject-use', kwargs={'user_id':user_id,'ref':ref}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, apiResponses['get_if_first_subject_use_false'])

    ## Test d'une requete GET invalide: utilisation d'un user_id invalide. Doit renvoyer un code 400
    def test_get_subject_first_use_wrong_user_id(self):
        user_id = 420
        ref = 'fr'
        response = self.client.get(reverse('backoffice:restapi-is-first-subject-use', kwargs={'user_id':user_id,'ref':ref}))
        self.assertEqual(response.status_code, 400)

    ## Test d'une requete GET invalide: utilisation d'une reference invalide. Doit renvoyer un code 400
    def test_get_subject_fisrt_use_wrong_reference(self):
        user_id = 4
        ref = 'abcd'
        response = self.client.get(reverse('backoffice:restapi-is-first-subject-use', kwargs={'user_id':user_id,'ref':ref}))
        self.assertEqual(response.status_code, 400)

## Classe RestApiPostSaveIpTest\n
# Classe de test pour la view PostSaveIp
class RestApiPostSaveIpTest(TestCase):
    fixtures = ['demo_dump.json']
    ## Préparation du client de test
    def setUp(self):
        self.client = APIClient()
        user = User.objects.get(username='teacher1')
        self.client.force_authenticate(user=user)

    ## Test d'une requete POST valide. Doit renvoyer un code 200
    def test_post_save_ip(self):
        class_id = 2
        server_ip = '173.194.40.159'
        response = self.client.post(reverse('backoffice:restapi-save-ip'), json.dumps({'class_id':class_id,'server_ip':server_ip}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, apiResponses['post_save_ip'])

    ## Test d'une requete POST invalide: utilisation d'un server_ip mal formatée. Doit renvoyer un code 400
    def test_post_save_ip_invalid_ip(self):
        class_id = 2
        server_ip = '173.194.40..1'
        response = self.client.post(reverse('backoffice:restapi-save-ip'), json.dumps({'class_id':class_id,'server_ip':server_ip}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 400)

    ## Test d'une requete POST invalide: server_ip manquant. Doit renvoyer un code 400
    def test_post_save_ip_missing_ip(self):
        class_id = 2
        response = self.client.post(reverse('backoffice:restapi-save-ip'), json.dumps({'class_id':class_id}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 400)

    ## Test d'une requete POST invalide: utilisation d'un class_id invalide. Doit renvoyer un code 400
    def test_post_save_ip_invalid_class_id(self):
        class_id = 420
        server_ip = '173.194.40.159'
        response = self.client.post(reverse('backoffice:restapi-save-ip'), json.dumps({'class_id':class_id,'server_ip':server_ip}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 400)

    ## Test d'une requete POST invalide: class_id manquant. Doit renvoyer un code 400
    def test_post_save_ip_missing_class_id(self):
        server_ip = '173.194.40.159'
        response = self.client.post(reverse('backoffice:restapi-save-ip'), json.dumps({'server_ip':server_ip}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 400)

## Classe RestApiGetUserDatasTest\n
# Classe de test pour la view GetUserDatas
class RestApiGetUserDatasTest(TestCase):
    fixtures = ['demo_dump.json']
    ## Préparation du client de test
    def setUp(self):
        self.client = APIClient()
        user = User.objects.get(username='teacher1')
        self.client.force_authenticate(user=user)
    ## Test d'une requete GET valide. Doit renvoyer un code 200
    def test_get_user_datas(self):
        user_id = 3
        response = self.client.get(reverse('backoffice:restapi-user-datas', kwargs={'user_id':user_id}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, apiResponses['get_user_data'])

    ## Test d'une requete GET valide. Doit renvoyer un code 200 et une json vide car l'utilisateur ne possede pas de data associées
    def test_get_user_datas_empty(self):
        user_id = 4
        response = self.client.get(reverse('backoffice:restapi-user-datas', kwargs={'user_id':user_id}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, apiResponses['get_user_data_empty'])

    ## Test d'une requete GET invalide: user_id innexistant. Doit renvoyer un code 400
    def test_get_user_datas_wrong_id(self):
        user_id = 420
        response = self.client.get(reverse('backoffice:restapi-user-datas', kwargs={'user_id':user_id}))
        self.assertEqual(response.status_code, 400)

## Classe RestApiPostUserDatasTest\n
# Classe de test pour la view PostUserDatas
class RestApiPostUserDatasTest(TestCase):
    fixtures = ['demo_dump.json']
    ## Préparation du client de test
    def setUp(self):
        self.client = APIClient()
        user = User.objects.get(username='teacher1')
        self.client.force_authenticate(user=user)

    ## Test d'une requete POST valide. Doit renvoyer un code 200
    def test_post_user_datas(self):
        user_id = 3
        data = '{"credits":43}'
        response = self.client.post(reverse('backoffice:restapi-save-user-datas'), json.dumps({'user_id':user_id,'data':data}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, apiResponses['post_user_datas'])

    ## Test d'une requete POST invalide: user_id innexistant. Doit renvoyer un code 400
    def test_post_user_datas(self):
        user_id = 420
        data = '{"credits":43}'
        response = self.client.post(reverse('backoffice:restapi-save-user-datas'), json.dumps({'user_id':user_id,'data':data}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 400)

    ## Test d'une requete POST invalide: data invalide. Doit renvoyer un code 400
    def test_post_user_datas(self):
        user_id = 3
        data = '{"credits":43}dwdewdewew'
        response = self.client.post(reverse('backoffice:restapi-save-user-datas'), json.dumps({'user_id':user_id,'data':data}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 400)

    ## Test d'une requete POST invalide: user_id manquant. Doit renvoyer un code 400
    def test_post_user_datas(self):
        data = '{"credits":43}'
        response = self.client.post(reverse('backoffice:restapi-save-user-datas'), json.dumps({'data':data}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 400)

    ## Test d'une requete POST invalide: data manquant. Doit renvoyer un code 400
    def test_post_user_datas(self):
        user_id = 3
        response = self.client.post(reverse('backoffice:restapi-save-user-datas'), json.dumps({'user_id':user_id}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 400)

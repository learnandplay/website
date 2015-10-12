from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse
import json

## Classe GetUserSchoolClassesTest\n
# Classe de test pour la view api_get_user_schoolclasses
class GetUserSchoolClassesTest(TestCase):
    fixtures = ['demo_dump.json']
    ## Préparation du client de test et login avec un compte professeur
    def setUp(self):
        self.client = Client()
        self.client.login(username='teacher1', password='password')

    ## Test d'une requete GET valide. Doit renvoyer un code 200
    def test_get_user_schoolclasses(self):
        response = self.client.get(reverse('backoffice:api_get_user_schoolclasses'))
        self.assertEqual(response.status_code, 200)


## Classe DeleteSchoolClassTest\n
# Classe de test pour la view api_delete_school_class
class DeleteSchoolClassTest(TestCase):
    fixtures = ['demo_dump.json']
    ## Préparation du client de test et login avec un compte professeur
    def setUp(self):
        self.client = Client()
        self.client.login(username='teacher1', password='password')

    ## Test d'une requete POST valide. Doit renvoyer un code 200
    def test_delete_schoolclass(self):
        class_id = 1
        response = self.client.post(reverse('backoffice:api_delete_school_class'), json.dumps({'class_id':class_id}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 200)

    ## Test d'une requete POST invalide: utilisation d'un class_id inexistant. Doit renvoyer un code 400
    def test_delete_schoolclass_wrong_id(self):
        class_id = 420
        response = self.client.post(reverse('backoffice:api_delete_school_class'), json.dumps({'class_id':class_id}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 400)

    ## Test d'une requete POST invalide: class_id manquant dans la requete. Doit renvoyer un code 400
    def test_delete_schoolclass_missing_class_id(self):
        response = self.client.post(reverse('backoffice:api_delete_school_class'), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 400)


## Classe GetAllClassesStudentsTest\n
# Classe de test pour la view api_get_all_classes_students
class GetAllClassesStudentsTest(TestCase):
    fixtures = ['demo_dump.json']
    ## Préparation du client de test et login avec un compte professeur
    def setUp(self):
        self.client = Client()
        self.client.login(username='teacher1', password='password')

    ## Test d'une requete GET valide. Doit renvoyer un code 200
    def test_get_all_classes_students(self):
        response = self.client.get(reverse('backoffice:api_get_all_classes_students'))
        self.assertEqual(response.status_code, 200)


## Classe DeleteUserTest\n
# Classe de test pour la view api_delete_user
class DeleteUserTest(TestCase):
    fixtures = ['demo_dump.json']
    ## Préparation du client de test et login avec un compte professeur
    def setUp(self):
        self.client = Client()
        self.client.login(username='teacher1', password='password')

    ## Test d'une requete POST valide. Doit renvoyer un code 200
    def test_delete_user(self):
        user_id = 5
        response = self.client.post(reverse('backoffice:api_delete_user'), json.dumps({'user_id':user_id}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 200)

    ## Test d'une requete POST invalide: utilisation d'un user_id inexistant. Doit renvoyer un code 400
    def test_delete_user_wrong_id(self):
        user_id = 420
        response = self.client.post(reverse('backoffice:api_delete_user'), json.dumps({'user_id':user_id}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 400)

    ## Test d'une requete POST invalide: user_id manquant dans la requete. Doit renvoyer un code 400
    def test_delete_user_missing_user_id(self):
        response = self.client.post(reverse('backoffice:api_delete_user'), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 400)


## Classe GetSchoolClassAdministratorsTest\n
# Classe de test pour la view api_get_schoolclass_administrators
class GetSchoolClassAdministratorsTest(TestCase):
    fixtures = ['demo_dump.json']
    ## Préparation du client de test et login avec un compte professeur
    def setUp(self):
        self.client = Client()
        self.client.login(username='teacher1', password='password')

    ## Test d'une requete GET valide. Doit renvoyer un code 200
    def test_get_schoolclass_administrators(self):
        class_id = 1
        response = self.client.get(reverse('backoffice:api_get_schoolclass_administrators', kwargs={'class_id':class_id}))
        self.assertEqual(response.status_code, 200)

    ## Test d'une requete GET invalide: utilisation d'un class_id inexistant. Doit renvoyer un code 400
    def test_get_schoolclass_administrators_wrong_id(self):
        class_id = 420
        response = self.client.get(reverse('backoffice:api_get_schoolclass_administrators', kwargs={'class_id':class_id}))
        self.assertEqual(response.status_code, 400)


## Classe RemoveAdministratorTest\n
# Classe de test pour la view api_remove_administrator
class RemoveAdministratorTest(TestCase):
    fixtures = ['demo_dump.json']
    ## Préparation du client de test et login avec un compte professeur
    def setUp(self):
        self.client = Client()
        self.client.login(username='teacher1', password='password')

    ## Test d'une requete POST valide. Doit renvoyer un code 200
    def test_remove_administrator(self):
        class_id = 2
        administrator_id = 2
        response = self.client.post(reverse('backoffice:api_remove_administrator'), json.dumps({'class_id':class_id,'administrator_id':administrator_id}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 200)

    ## Test d'une requete POST invalide: utilisation d'un class_id inexistant. Doit renvoyer un code 400
    def test_remove_administrator_wrong_class_id(self):
        class_id = 420
        administrator_id = 2
        response = self.client.post(reverse('backoffice:api_remove_administrator'), json.dumps({'class_id':class_id,'administrator_id':administrator_id}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 400)

    ## Test d'une requete POST invalide: utilisation d'un administrator_id inexistant. Doit renvoyer un code 400
    def test_remove_administrator_wrong_administrator_id(self):
        class_id = 2
        administrator_id = 420
        response = self.client.post(reverse('backoffice:api_remove_administrator'), json.dumps({'class_id':class_id,'administrator_id':administrator_id}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 400)

    ## Test d'une requete POST invalide: class_id manquant dans la requete. Doit renvoyer un code 400
    def test_remove_administrator_missing_class_id(self):
        administrator_id = 2
        response = self.client.post(reverse('backoffice:api_remove_administrator'), json.dumps({'administrator_id':administrator_id}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 400)

    ## Test d'une requete POST invalide: administrator_id manquant dans la requete. Doit renvoyer un code 400
    def test_remove_administrator_missing_administrator_id(self):
        class_id = 2
        response = self.client.post(reverse('backoffice:api_remove_administrator'), json.dumps({'class_id':class_id}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 400)


## Classe AddAdministratorTest\n
# Classe de test pour la view api_add_administrator
class AddAdministratorTest(TestCase):
    fixtures = ['demo_dump.json']
    ## Préparation du client de test et login avec un compte professeur
    def setUp(self):
        self.client = Client()
        self.client.login(username='teacher1', password='password')

    ## Test d'une requete POST valide. Doit renvoyer un code 200
    def test_add_administrator(self):
        username = 'teacher2'
        class_id = 1
        response = self.client.post(reverse('backoffice:api_add_administrator'), json.dumps({'username':username,'class_id':class_id}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 200)

    ## Test d'une requete POST invalide: utilisation d'un username inexistant. Doit renvoyer un code 400
    def test_add_administrator_wrong_username(self):
        username = 'toto'
        class_id = 1
        response = self.client.post(reverse('backoffice:api_add_administrator'), json.dumps({'username':username,'class_id':class_id}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 400)

    ## Test d'une requete POST invalide: utilisation d'un class_id inexistant. Doit renvoyer un code 400
    def test_add_administrator_wrong_class_id(self):
        username = 'teacher2'
        class_id = 420
        response = self.client.post(reverse('backoffice:api_add_administrator'), json.dumps({'username':username,'class_id':class_id}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 400)

    ## Test d'une requete POST invalide: username manquant dans la requete. Doit renvoyer un code 400
    def test_add_administrator_missing_username(self):
        class_id = 1
        response = self.client.post(reverse('backoffice:api_add_administrator'), json.dumps({'class_id':class_id}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 400)

    ## Test d'une requete POST invalide: class_id manquant dans la requete. Doit renvoyer un code 400
    def test_add_administrator_missing_class_id(self):
        username = 'teacher2'
        response = self.client.post(reverse('backoffice:api_add_administrator'), json.dumps({'username':username}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 400)


## Classe GetStatisticsTest\n
# Classe de test pour la view api_get_statistics
class GetStatisticsTest(TestCase):
    fixtures = ['demo_dump.json']
    ## Préparation du client de test et login avec un compte professeur
    def setUp(self):
        self.client = Client()
        self.client.login(username='teacher1', password='password')

    ## Test d'une requete GET valide. Doit renvoyer un code 200
    def test_get_statistics_student(self):
        class_id = 1
        student_id = 4
        response = self.client.get(reverse('backoffice:api_get_statistics', kwargs={'class_id':class_id,'student_id':student_id}))
        self.assertEqual(response.status_code, 200)

    ## Test d'une requete GET valide. Doit renvoyer un code 200
    def test_get_statistics_class(self):
        class_id = 1
        student_id = -1
        response = self.client.get(reverse('backoffice:api_get_statistics', kwargs={'class_id':class_id,'student_id':student_id}))
        self.assertEqual(response.status_code, 200)

    ## Test d'une requete GET valide: Ne renvoit aucune données car utilisation d'un class_id inexistant. Doit renvoyer un code 200
    def test_get_statistics_wrong_class_id(self):
        class_id = 42
        student_id = -1
        response = self.client.get(reverse('backoffice:api_get_statistics', kwargs={'class_id':class_id,'student_id':student_id}))
        self.assertEqual(response.status_code, 200)

    ## Test d'une requete GET valide: Ne renvoit aucune données car utilisation d'un student_id inexistant. Doit renvoyer un code 200
    def test_get_statistics_wrong_student_id(self):
        class_id = 1
        student_id = 40392
        response = self.client.get(reverse('backoffice:api_get_statistics', kwargs={'class_id':class_id,'student_id':student_id}))
        self.assertEqual(response.status_code, 200)


## Classe GetSubjectsTest\n
# Classe de test pour la view api_get_subjects
class GetSubjectsTest(TestCase):
    fixtures = ['demo_dump.json']
    ## Préparation du client de test et login avec un compte professeur
    def setUp(self):
        self.client = Client()
        self.client.login(username='teacher1', password='password')

    ## Test d'une requete GET valide. Doit renvoyer un code 200
    def test_get_subjects(self):
        response = self.client.get(reverse('backoffice:api_get_subjects'))
        self.assertEqual(response.status_code, 200)


## Classe GetSubjectsExercisesTest\n
# Classe de test pour la view api_get_subjects_exercices
class GetSubjectsExercisesTest(TestCase):
    fixtures = ['demo_dump.json']
    ## Préparation du client de test et login avec un compte professeur
    def setUp(self):
        self.client = Client()
        self.client.login(username='teacher1', password='password')

    ## Test d'une requete GET valide. Doit renvoyer un code 200
    def test_get_subjects_exercices(self):
        response = self.client.get(reverse('backoffice:api_get_subjects_exercices'))
        self.assertEqual(response.status_code, 200)


## Classe SaveSubjectConfigTest\n
# Classe de test pour les views api_save_subject_config et api_update_subject_config
class SaveSubjectConfigTest(TestCase):
    fixtures = ['demo_dump.json']
    ## Préparation du client de test et login avec un compte professeur
    def setUp(self):
        self.client = Client()
        self.client.login(username='teacher1', password='password')

    ## Test d'une requete POST valide pour la sauvegarde d'une configuration. Doit renvoyer un code 200
    def test_save_subject_config(self):
        config_name = 'test de configuration'
        class_id = 1
        subject_id = 1
        data = "{'fakedata'=data}"
        response = self.client.post(reverse('backoffice:api_save_subject_config'), json.dumps({'config_name':config_name,'school_class':class_id,'subject_id':subject_id,'data':data}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 200)

    ## Test d'une requete POST valide pour l'update d'une configuration. Doit renvoyer un code 200
    def test_update_subject_config(self):
        config_name = 'test de configuration'
        class_id = 1
        subject_id = 1
        data = "{'fakedata'=data}"
        subject_config_id = 1
        response = self.client.post(reverse('backoffice:api_update_subject_config', kwargs={'subject_config_id':subject_config_id}), json.dumps({'config_name':config_name,'school_class':class_id,'subject_id':subject_id,'data':data}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 200)

    ## Test d'une requete POST invalide pour l'update d'une configuration: utilisation d'un config_id inexistant. Doit renvoyer un code 400
    def test_update_subject_wrong_config_id(self):
        config_name = 'test de configuration'
        class_id = 1
        subject_id = 1
        data = "{'fakedata'=data}"
        subject_config_id = 420
        response = self.client.post(reverse('backoffice:api_update_subject_config', kwargs={'subject_config_id':subject_config_id}), json.dumps({'config_name':config_name,'school_class':class_id,'subject_id':subject_id,'data':data}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 400)

    ## Test d'une requete POST invalide pour la sauvegarde d'une configuration: utilisation d'un class_id inexistant. Doit renvoyer un code 400
    def test_save_subject_config_wrong_class_id(self):
        config_name = 'test de configuration'
        class_id = 420
        subject_id = 1
        data = "{'fakedata'=data}"
        response = self.client.post(reverse('backoffice:api_save_subject_config'), json.dumps({'config_name':config_name,'school_class':class_id,'subject_id':subject_id,'data':data}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 400)

    ## Test d'une requete POST invalide pour la sauvegarde d'une configuration: utilisation d'un subject_id inexistant. Doit renvoyer un code 400
    def test_save_subject_config_wrong_subject_id(self):
        config_name = 'test de configuration'
        class_id = 1
        subject_id = 420
        data = "{'fakedata'=data}"
        response = self.client.post(reverse('backoffice:api_save_subject_config'), json.dumps({'config_name':config_name,'school_class':class_id,'subject_id':subject_id,'data':data}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 400)

    ## Test d'une requete POST invalide pour la sauvegarde d'une configuration: class_id manquant dans la requete. Doit renvoyer un code 400
    def test_save_subject_config_missing_class_id(self):
        config_name = 'test de configuration'
        subject_id = 1
        data = "{'fakedata'=data}"
        response = self.client.post(reverse('backoffice:api_save_subject_config'), json.dumps({'config_name':config_name,'subject_id':subject_id,'data':data}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 400)

    ## Test d'une requete POST invalide pour la sauvegarde d'une configuration: subject_id manquant dans la requete. Doit renvoyer un code 400
    def test_save_subject_config_missing_subject_id(self):
        config_name = 'test de configuration'
        class_id = 1
        data = "{'fakedata'=data}"
        response = self.client.post(reverse('backoffice:api_save_subject_config'), json.dumps({'config_name':config_name,'school_class':class_id,'data':data}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 400)

    ## Test d'une requete POST invalide pour la sauvegarde d'une configuration: config_name manquant dans la requete. Doit renvoyer un code 400
    def test_save_subject_config_missing_config_name(self):
        class_id = 1
        subject_id = 1
        data = "{'fakedata'=data}"
        response = self.client.post(reverse('backoffice:api_save_subject_config'), json.dumps({'school_class':class_id,'subject_id':subject_id,'data':data}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 400)

    ## Test d'une requete POST invalide pour la sauvegarde d'une configuration: data manquant dans la requete. Doit renvoyer un code 400
    def test_save_subject_config_missing_data(self):
        config_name = 'test de configuration'
        class_id = 1
        subject_id = 1
        response = self.client.post(reverse('backoffice:api_save_subject_config'), json.dumps({'config_name':config_name,'school_class':class_id,'subject_id':subject_id}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 400)


## Classe SaveExerciseConfigTest\n
# Classe de test pour les views api_save_exercise_config et api_update_exercise_config
class SaveExerciseConfigTest(TestCase):
    fixtures = ['demo_dump.json']
    ## Préparation du client de test et login avec un compte professeur
    def setUp(self):
        self.client = Client()
        self.client.login(username='teacher1', password='password')

    ## Test d'une requete POST valide pour la sauvegarde d'une configuration. Doit renvoyer un code 200
    def test_save_exercise_config(self):
        config_name = 'test de configuration'
        class_id = 1
        exercise_id = 1
        data = "{'fakedata'=data}"
        response = self.client.post(reverse('backoffice:api_save_exercise_config'), json.dumps({'config_name':config_name,'school_class':class_id,'exercise_id':exercise_id,'data':data}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 200)

    ## Test d'une requete POST valide pour l'update d'une configuration. Doit renvoyer un code 200
    def test_update_exercise_config(self):
        config_name = 'test de configuration'
        class_id = 1
        exercise_id = 1
        data = "{'fakedata'=data}"
        exercise_config_id = 1
        response = self.client.post(reverse('backoffice:api_update_exercise_config', kwargs={'exercise_config_id':exercise_config_id}), json.dumps({'config_name':config_name,'school_class':class_id,'exercise_id':exercise_id,'data':data}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 200)

    ## Test d'une requete POST invalide pour l'update d'une configuration: utilisation d'un config_id inexistant. Doit renvoyer un code 400
    def test_update_exercise_wrong_config_id(self):
        config_name = 'test de configuration'
        class_id = 1
        exercise_id = 1
        data = "{'fakedata'=data}"
        exercise_config_id = 420
        response = self.client.post(reverse('backoffice:api_update_exercise_config', kwargs={'exercise_config_id':exercise_config_id}), json.dumps({'config_name':config_name,'school_class':class_id,'exercise_id':exercise_id,'data':data}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 400)

    ## Test d'une requete POST invalide pour la sauvegarde d'une configuration: utilisation d'un class_id inexistant. Doit renvoyer un code 400
    def test_save_exercise_config_wrong_class_id(self):
        config_name = 'test de configuration'
        class_id = 420
        exercise_id = 1
        data = "{'fakedata'=data}"
        response = self.client.post(reverse('backoffice:api_save_exercise_config'), json.dumps({'config_name':config_name,'school_class':class_id,'exercise_id':exercise_id,'data':data}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 400)

    ## Test d'une requete POST invalide pour la sauvegarde d'une configuration: utilisation d'un exercise_id inexistant. Doit renvoyer un code 400
    def test_save_exercise_config_wrong_exercise_id(self):
        config_name = 'test de configuration'
        class_id = 1
        exercise_id = 420
        data = "{'fakedata'=data}"
        response = self.client.post(reverse('backoffice:api_save_exercise_config'), json.dumps({'config_name':config_name,'school_class':class_id,'exercise_id':exercise_id,'data':data}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 400)

    ## Test d'une requete POST invalide pour la sauvegarde d'une configuration: class_id manquant dans la requete. Doit renvoyer un code 400
    def test_save_exercise_config_missing_class_id(self):
        config_name = 'test de configuration'
        exercise_id = 1
        data = "{'fakedata'=data}"
        response = self.client.post(reverse('backoffice:api_save_exercise_config'), json.dumps({'config_name':config_name,'exercise_id':exercise_id,'data':data}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 400)

    ## Test d'une requete POST invalide pour la sauvegarde d'une configuration: exercise_id manquant dans la requete. Doit renvoyer un code 400
    def test_save_exercise_config_missing_exercise_id(self):
        config_name = 'test de configuration'
        class_id = 1
        data = "{'fakedata'=data}"
        response = self.client.post(reverse('backoffice:api_save_exercise_config'), json.dumps({'config_name':config_name,'school_class':class_id,'data':data}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 400)

    ## Test d'une requete POST invalide pour la sauvegarde d'une configuration: config_name manquant dans la requete. Doit renvoyer un code 400
    def test_save_exercise_config_missing_config_name(self):
        class_id = 1
        exercise_id = 1
        data = "{'fakedata'=data}"
        response = self.client.post(reverse('backoffice:api_save_exercise_config'), json.dumps({'school_class':class_id,'exercise_id':exercise_id,'data':data}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 400)

    ## Test d'une requete POST invalide pour la sauvegarde d'une configuration: data manquant dans la requete. Doit renvoyer un code 400
    def test_save_exercise_config_missing_data(self):
        config_name = 'test de configuration'
        class_id = 1
        exercise_id = 1
        response = self.client.post(reverse('backoffice:api_save_exercise_config'), json.dumps({'config_name':config_name,'school_class':class_id,'exercise_id':exercise_id}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 400)


## Classe GetConfigurationsTest\n
# Classe de test pour la view api_get_configurations
class GetConfigurationsTest(TestCase):
    fixtures = ['demo_dump.json']
    ## Préparation du client de test et login avec un compte professeur
    def setUp(self):
        self.client = Client()
        self.client.login(username='teacher1', password='password')

    ## Test d'une requete GET valide. Doit renvoyer un code 200
    def test_get_configurations(self):
        response = self.client.get(reverse('backoffice:api_get_configurations'))
        self.assertEqual(response.status_code, 200)


## Classe DeleteExerciseConfigurationTest\n
# Classe de test pour la view api_delete_exercise_configuration
class DeleteExerciseConfigurationTest(TestCase):
    fixtures = ['demo_dump.json']
    ## Préparation du client de test et login avec un compte professeur
    def setUp(self):
        self.client = Client()
        self.client.login(username='teacher1', password='password')

    ## Test d'une requete POST valide. Doit renvoyer un code 200
    def test_delete_exercise_configuration(self):
        config_id = 1
        response = self.client.post(reverse('backoffice:api_delete_exercise_configuration'), json.dumps({'config_id':config_id}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 200)

    ## Test d'une requete POST invalide: utilisation d'un config_id inexistant. Doit renvoyer un code 400
    def test_delete_exercise_configuration_wrong_config_id(self):
        config_id = 420
        response = self.client.post(reverse('backoffice:api_delete_exercise_configuration'), json.dumps({'config_id':config_id}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 400)

    ## Test d'une requete POST invalide: config_id manquant dans la requete. Doit renvoyer un code 400
    def test_delete_exercise_configuration_missing_config_id(self):
        response = self.client.post(reverse('backoffice:api_delete_exercise_configuration'), json.dumps({}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 400)


## Classe DeleteSubjectConfigurationTest\n
# Classe de test pour la view api_delete_subject_configuration
class DeleteSubjectConfigurationTest(TestCase):
    fixtures = ['demo_dump.json']
    ## Préparation du client de test et login avec un compte professeur
    def setUp(self):
        self.client = Client()
        self.client.login(username='teacher1', password='password')

    ## Test d'une requete POST valide. Doit renvoyer un code 200
    def test_delete_subject_configuration(self):
        config_id = 1
        response = self.client.post(reverse('backoffice:api_delete_subject_configuration'), json.dumps({'config_id':config_id}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 200)

    ## Test d'une requete POST invalide: utilisation d'un config_id inexistant. Doit renvoyer un code 400
    def test_delete_subject_configuration_wrong_config_id(self):
        config_id = 420
        response = self.client.post(reverse('backoffice:api_delete_subject_configuration'), json.dumps({'config_id':config_id}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 400)

    ## Test d'une requete POST invalide: config_id manquant dans la requete. Doit renvoyer un code 400
    def test_delete_subject_configuration_missing_config_id(self):
        response = self.client.post(reverse('backoffice:api_delete_subject_configuration'), json.dumps({}), content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 400)

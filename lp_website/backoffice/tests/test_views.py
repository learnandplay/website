from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse
from backoffice.forms import ClassForm, SchoolClassPasswordForm

class IndexTest(TestCase):
    fixtures = ['demo_dump.json']
    def setUp(self):
        self.client = Client()
        self.client.login(username='teacher1', password='password')

    def test_index(self):
        response = self.client.get(reverse('backoffice:index'))
        self.assertEqual(response.status_code, 200)


class TeachersRequiredTest(TestCase):
    fixtures = ['demo_dump.json']
    def setUp(self):
        self.client = Client()
        self.client.login(username='Benjamin.Boisset', password='password')

    def test_index(self):
        response = self.client.get(reverse('backoffice:teachers_required'))
        self.assertEqual(response.status_code, 200)


class MyClassesTest(TestCase):
    fixtures = ['demo_dump.json']
    def setUp(self):
        self.client = Client()
        self.client.login(username='teacher1', password='password')

    def test_my_classes(self):
        response = self.client.get(reverse('backoffice:my_classes'))
        self.assertEqual(response.status_code, 200)


class EditClassTest(TestCase):
    fixtures = ['demo_dump.json']
    def setUp(self):
        self.client = Client()
        self.client.login(username='teacher1', password='password')

    def test_create_class(self):
        pass

    def test_edit_class(self):
        pass

    def test_edit_class_wrong_id(self):
        class_id = 420
        response = self.client.post(reverse('backoffice:edit_class', kwargs={'id':class_id}))
        self.assertEqual(response.status_code, 400)

class MyStudentsTest(TestCase):
    fixtures = ['demo_dump.json']
    def setUp(self):
        self.client = Client()
        self.client.login(username='teacher1', password='password')

    def test_my_students_default(self):
        response = self.client.get(reverse('backoffice:my_students_default'))
        self.assertEqual(response.status_code, 200)

    def test_my_students(self):
        class_id = 1
        response = self.client.get(reverse('backoffice:my_students', kwargs={'class_id':class_id}))
        self.assertEqual(response.status_code, 200)


class EditStudentTest(TestCase):
    fixtures = ['demo_dump.json']
    def setUp(self):
        self.client = Client()
        self.client.login(username='teacher1', password='password')

    def test_create_student(self):
        pass

    def test_edit_student(self):
        pass

    def test_edit_student_wrong_id(self):
        student_id = 420
        class_id = 1
        response = self.client.post(reverse('backoffice:edit_student', kwargs={'id':student_id, 'class_id':class_id}))
        self.assertEqual(response.status_code, 400)


class ClassAdministratorsTest(TestCase):
    fixtures = ['demo_dump.json']
    def setUp(self):
        self.client = Client()
        self.client.login(username='teacher1', password='password')

    def test_class_administrators(self):
        class_id = 1
        response = self.client.get(reverse('backoffice:class_administrators', kwargs={'class_id':class_id}))
        self.assertEqual(response.status_code, 200)

    def test_class_administrators_wrong_id(self):
        class_id = 420
        response = self.client.get(reverse('backoffice:class_administrators', kwargs={'class_id':class_id}))
        self.assertEqual(response.status_code, 400)


class EditProfileTest(TestCase):
    fixtures = ['demo_dump.json']
    def setUp(self):
        self.client = Client()
        self.client.login(username='teacher1', password='password')

    def test_edit_profile(self):
        pass

    def test_edit_profile_error(self):
        pass


class StatisticsTest(TestCase):
    fixtures = ['demo_dump.json']
    def setUp(self):
        self.client = Client()
        self.client.login(username='teacher1', password='password')

    def test_statistics(self):
        response = self.client.get(reverse('backoffice:statistics'))
        self.assertEqual(response.status_code, 200)


class ConfigurationTest(TestCase):
    fixtures = ['demo_dump.json']
    def setUp(self):
        self.client = Client()
        self.client.login(username='teacher1', password='password')

    def test_configuration(self):
        response = self.client.get(reverse('backoffice:configuration'))
        self.assertEqual(response.status_code, 200)


class SubjectConfigurationTest(TestCase):
    fixtures = ['demo_dump.json']
    def setUp(self):
        self.client = Client()
        self.client.login(username='teacher1', password='password')

    def test_subject_configuration(self):
        subject_config_id = 1
        response = self.client.get(reverse('backoffice:subject_configuration', kwargs={'subject_id':subject_config_id}))
        self.assertEqual(response.status_code, 200)

    def test_subject_configuration_wrong_id(self):
        subject_config_id = 420
        response = self.client.get(reverse('backoffice:subject_configuration', kwargs={'subject_id':subject_config_id}))
        self.assertEqual(response.status_code, 400)


class ExerciseConfigurationTest(TestCase):
    fixtures = ['demo_dump.json']
    def setUp(self):
        self.client = Client()
        self.client.login(username='teacher1', password='password')

    def test_exercise_configuration(self):
        exercise_config_id = 1
        response = self.client.get(reverse('backoffice:exercise_configuration', kwargs={'exercise_id':exercise_config_id}))
        self.assertEqual(response.status_code, 200)

    def test_exercise_configuration_wrong_id(self):
        exercise_config_id = 420
        response = self.client.get(reverse('backoffice:exercise_configuration', kwargs={'exercise_id':exercise_config_id}))
        self.assertEqual(response.status_code, 400)


class MyconfigurationsTest(TestCase):
    fixtures = ['demo_dump.json']
    def setUp(self):
        self.client = Client()
        self.client.login(username='teacher1', password='password')

    def test_my_configurations(self):
        response = self.client.get(reverse('backoffice:my_configurations'))
        self.assertEqual(response.status_code, 200)

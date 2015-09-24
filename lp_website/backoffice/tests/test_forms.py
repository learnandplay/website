from django.test import TestCase
from backoffice.forms import UserRegistrationForm, UserLoginForm, ClassForm, AvatarForm, StudentForm, UserEmailForm, UserPasswordNotRequiredForm, SchoolClassPasswordForm, SchoolClassPasswordNotRequiredForm

class UserRegistrationFormTest(TestCase):
    def setUp(self):
        self.valid_form_data = {'username':'user1', 'email':'validemail@domain.com', 'password':'password', 'password_confirm': 'password'}
        self.invalid_username = {'username':'user!', 'email':'validemail@domain.com', 'password':'password', 'password_confirm': 'password'}
        self.invalid_email = {'username':'user1', 'email':'invalidemail@domain.c', 'password':'password', 'password_confirm': 'password'}
        self.invalid_password_length = {'username':'user1', 'email':'validemail@domain.com', 'password':'pass', 'password_confirm': 'pass'}
        self.invalid_password_confirmation = {'username':'user1', 'email':'validemail@domain.com', 'password':'password', 'password_confirm': 'password420'}

    def test_valid_form(self):
        form = UserRegistrationForm(data=self.valid_form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_username(self):
        form = UserRegistrationForm(data=self.invalid_username)
        self.assertFalse(form.is_valid())

    def test_invalid_email(self):
        form = UserRegistrationForm(data=self.invalid_email)
        self.assertFalse(form.is_valid())

    def test_invalid_password_length(self):
        form = UserRegistrationForm(data=self.invalid_password_length)
        self.assertFalse(form.is_valid())

    def test_invalid_password_confirmation(self):
        form = UserRegistrationForm(data=self.invalid_password_confirmation)
        self.assertFalse(form.is_valid())


class UserLoginFormTest(TestCase):
    def setUp(self):
        self.valid_form_data = {'username':'user1', 'password':'password', 'remember_me':True}
        self.valid_form_data_without_remember_me = {'username':'user1', 'password':'password'}
        self.missing_username = {'password':'password'}
        self.missing_password = {'username':'user1'}

    def test_valid_form(self):
        form = UserLoginForm(data=self.valid_form_data)
        self.assertTrue(form.is_valid())

    def test_valid_form_without_remember_me(self):
        form = UserLoginForm(data=self.valid_form_data_without_remember_me)
        self.assertTrue(form.is_valid())

    def test_missing_username(self):
        form = UserLoginForm(data=self.missing_username)
        self.assertFalse(form.is_valid())

    def test_missing_password(self):
        form = UserLoginForm(data=self.missing_password)
        self.assertFalse(form.is_valid())


class ClassFormTest(TestCase):
    def setUp(self):
        self.valid_form_data = {'name':'cp', 'school_name':'primaire'}
        self.missing_name = {'school_name':'primaire'}
        self.missing_school_name = {'name':'cp'}

    def test_valid_form(self):
        form = ClassForm(data=self.valid_form_data)
        self.assertTrue(form.is_valid())

    def test_missing_name(self):
        form = ClassForm(data=self.missing_name)
        self.assertFalse(form.is_valid())

    def test_missing_school_name(self):
        form = ClassForm(data=self.missing_school_name)
        self.assertFalse(form.is_valid())


class AvatarFormTest(TestCase):
    def setUp(self):
        pass


class StudentFormTest(TestCase):
    def setUp(self):
        self.valid_form_data = {'username':'studentName'}
        self.missing_username = {}

    def test_valid_form(self):
        form = StudentForm(data=self.valid_form_data)
        self.assertTrue(form.is_valid())

    def test_missing_username(self):
        form = StudentForm(data=self.missing_username)
        self.assertFalse(form.is_valid())


class UserEmailFormTest(TestCase):
    def setUp(self):
        self.valid_form_data = {'email':'validemail@domain.com'}
        self.invalid_email = {'email':'invalidemail@domain.c'}
        self.missing_email = {}

    def test_valid_form(self):
        form = UserEmailForm(data=self.valid_form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_email(self):
        form = UserEmailForm(data=self.invalid_email)
        self.assertFalse(form.is_valid())

    def test_missing_email(self):
        form = UserEmailForm(data=self.missing_email)
        self.assertTrue(form.is_valid())


class UserPasswordNotRequiredFormTest(TestCase):
    def setUp(self):
        self.valid_form_data = {'password':'password', 'password_confirm':'password'}
        self.empty_form = {}
        self.invalid_password = {'password':'pass', 'password_confirm':'pass'}
        self.invalid_password_confirm = {'password':'password', 'password_confirm':'password420'}
        self.missing_password_confirm = {'password':'password'}

    def test_valid_form(self):
        form = UserPasswordNotRequiredForm(data=self.valid_form_data)
        self.assertTrue(form.is_valid())

    def test_empty_form(self):
        form = UserPasswordNotRequiredForm(data=self.empty_form)
        self.assertTrue(form.is_valid())

    def test_invalid_password(self):
        form = UserPasswordNotRequiredForm(data=self.invalid_password)
        self.assertFalse(form.is_valid())

    def test_invalid_password_confirm(self):
        form = UserPasswordNotRequiredForm(data=self.invalid_password_confirm)
        self.assertFalse(form.is_valid())

    def test_missing_password_confirm(self):
        form = UserPasswordNotRequiredForm(data=self.missing_password_confirm)
        self.assertFalse(form.is_valid())


class SchoolClassPasswordFormTest(TestCase):
    def setUp(self):
        self.valid_form_data = {'password':'password', 'password_confirm':'password'}
        self.empty_form = {}
        self.invalid_password = {'password':'pass', 'password_confirm':'pass'}
        self.invalid_password_confirm = {'password':'password', 'password_confirm':'password420'}
        self.missing_password_confirm = {'password':'password'}

    def test_valid_form(self):
        form = SchoolClassPasswordForm(data=self.valid_form_data)
        self.assertTrue(form.is_valid())

    def test_empty_form(self):
        form = SchoolClassPasswordForm(data=self.empty_form)
        self.assertFalse(form.is_valid())

    def test_invalid_password(self):
        form = SchoolClassPasswordForm(data=self.invalid_password)
        self.assertFalse(form.is_valid())

    def test_invalid_password_confirm(self):
        form = SchoolClassPasswordForm(data=self.invalid_password_confirm)
        self.assertFalse(form.is_valid())

    def test_missing_password_confirm(self):
        form = SchoolClassPasswordForm(data=self.missing_password_confirm)
        self.assertFalse(form.is_valid())


class SchoolClassPasswordNotRequiredFormTest(TestCase):
    def setUp(self):
        self.valid_form_data = {'password':'password', 'password_confirm':'password'}
        self.empty_form = {}
        self.invalid_password = {'password':'pass', 'password_confirm':'pass'}
        self.invalid_password_confirm = {'password':'password', 'password_confirm':'password420'}
        self.missing_password_confirm = {'password':'password'}

    def test_valid_form(self):
        form = SchoolClassPasswordNotRequiredForm(data=self.valid_form_data)
        self.assertTrue(form.is_valid())

    def test_empty_form(self):
        form = SchoolClassPasswordNotRequiredForm(data=self.empty_form)
        self.assertTrue(form.is_valid())

    def test_invalid_password(self):
        form = SchoolClassPasswordNotRequiredForm(data=self.invalid_password)
        self.assertFalse(form.is_valid())

    def test_invalid_password_confirm(self):
        form = SchoolClassPasswordNotRequiredForm(data=self.invalid_password_confirm)
        self.assertFalse(form.is_valid())

    def test_missing_password_confirm(self):
        form = SchoolClassPasswordNotRequiredForm(data=self.missing_password_confirm)
        self.assertFalse(form.is_valid())

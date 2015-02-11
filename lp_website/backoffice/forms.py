# -*- coding: UTF-8 -*-
from django.contrib.auth.models import User
from django import forms
from backoffice.models import SchoolClass, LPUser

class UserRegistrationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        help_texts = {
            'username': '',
        }
    password = forms.CharField(label="Mot de passe",
                               widget=forms.PasswordInput(render_value = True, attrs={'placeholder': 'Mot de passe contenant au moins 8 caractères'}))
    password_confirm = forms.CharField(label="Confirmation du mot de passe", widget=forms.PasswordInput(render_value = True))
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError("Erreur ! Le mot de passe doit contenir au moins 8 caractères")
        return password
    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if not password:
            raise forms.ValidationError("")
        if password != password_confirm:
            raise forms.ValidationError("Erreur ! La confirmation du mot de passe ne correspond pas")
        return password_confirm

class UserLoginForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    remember_me = forms.BooleanField(label="Se souvenir de moi", required=False, widget=forms.CheckboxInput())

class ClassForm(forms.ModelForm):
    class Meta:
        model = SchoolClass
        exclude = ('data',)
    name = forms.CharField(label="Nom de la classe", max_length=64)
    school_name = forms.CharField(label="Nom de l'établissement", max_length=128)

class StudentAvatarForm(forms.ModelForm):
    class Meta:
        model = LPUser
        fields = ('avatar',)
        labels = {
            'avatar': "Avatar"
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username',)
        help_texts = {
            'username': '',
        }

class AddAdministratorForm(forms.Form):
    username = forms.CharField(label="", max_length=30, required=False, widget=forms.TextInput(attrs={'placeholder': "Nom d'utilisateur"}))
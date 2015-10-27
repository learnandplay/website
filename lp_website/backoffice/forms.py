# -*- coding: UTF-8 -*-
## @package forms
# Formulaires Django utilisés dans l'application
from django.contrib.auth.models import User
from django import forms
from backoffice.models import SchoolClass, LPUser

## Classe UserRegistrationForm\n
# Formulaire de création de compte professeur
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
    ## Mot de passe
    password = forms.CharField(label="Mot de passe",
                               widget=forms.PasswordInput(render_value = True, attrs={'placeholder': 'Mot de passe contenant au moins 8 caractères'}))
    ## Confirmation du mot de passe
    password_confirm = forms.CharField(label="Confirmation du mot de passe", widget=forms.PasswordInput(render_value = True))
    ## Verification du mot de passe
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError("Erreur ! Le mot de passe doit contenir au moins 8 caractères")
        return password
    ## Verification de la confirmation du mot de passe
    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if not password:
            raise forms.ValidationError("")
        if password != password_confirm:
            raise forms.ValidationError("Erreur ! La confirmation du mot de passe ne correspond pas")
        return password_confirm

## Classe UserLoginForm\n
# Formulaire de login
class UserLoginForm(forms.Form):
    ## Nom d'utilisateur
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    ## Mot de passe
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    ## Option remember_me pour rester connecté au dela de la session actuelle
    remember_me = forms.BooleanField(label="Se souvenir de moi", required=False, widget=forms.CheckboxInput())

## Classe ClassForm\n
# Formulaire de création ou d'édition de classe
class ClassForm(forms.ModelForm):
    class Meta:
        model = SchoolClass
        exclude = ('data','password')
    ## Nom de la classe
    name = forms.CharField(label="Nom de la classe", max_length=64)
    ## Nom de l'établissement
    school_name = forms.CharField(label="Nom de l'établissement", max_length=128)
    ## Adresse IP
    ip = forms.CharField(label="Adresse IP du serveur", required=False)

## Classe AvatarForm\n
# Formulaire pour l'upload d'avatar
class AvatarForm(forms.ModelForm):
    class Meta:
        model = LPUser
        fields = ('avatar',)
        labels = {
            'avatar': "Avatar"
        }

## Classe StudentForm\n
# Formulaire pour la création et l'édition d'élèves
class StudentForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username',)
        help_texts = {
            'username': '',
        }

## Classe UserLoginForm\n
# Formulaire d'email utilisateur
class UserEmailForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)

## Classe UserPasswordNotRequiredForm\n
# Formulaire de mot de passe utilisateur optionnel
class UserPasswordNotRequiredForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('password',)
    ## Mot de passe
    password = forms.CharField(required=False, label="Mot de passe",
                               widget=forms.PasswordInput(render_value = True, attrs={'placeholder': 'Mot de passe contenant au moins 8 caractères'}))
    ## Confirmation du mot de passe
    password_confirm = forms.CharField(required=False, label="Confirmation du mot de passe", widget=forms.PasswordInput(render_value = True))
    ## Verification du mot de passe
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8 and len(password) > 0:
            raise forms.ValidationError("Erreur ! Le mot de passe doit contenir au moins 8 caractères")
        return password
    ## Verification de la confirmation du mot de passe
    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password != password_confirm:
            raise forms.ValidationError("Erreur ! La confirmation du mot de passe ne correspond pas")
        return password_confirm

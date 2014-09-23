from django.contrib.auth.models import User
from django import forms

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
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    password_confirm = forms.CharField(label="Confirmation du mot de passe", widget=forms.PasswordInput)
    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
                raise forms.ValidationError("Erreur ! La confirmation du mot de passe ne correspond pas")
        return password_confirm

class UserLoginForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    remember_me = forms.BooleanField(label="Se souvenir de moi", required=False, widget=forms.CheckboxInput())

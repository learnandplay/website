# -*- coding: UTF-8 -*-
## @package decorators
# Décorateurs
from django.shortcuts import redirect

def anonymous_required(view_function, redirect_to = None):
    return AnonymousRequired(view_function, redirect_to)

## Classe AnonymousRequired\n
# Utilisé pour les pages nécéssitant de ne pas être authentifié (page de login, de création de compte, ...)\n
# Redirige l'utilisateur vers la page configurée dans settings.LOGGED_USER_REDIRECT si l'utilisateur est authentifié
class AnonymousRequired(object):
    def __init__(self, view_function, redirect_to):
        if redirect_to is None:
            from django.conf import settings
            redirect_to = settings.LOGGED_USER_REDIRECT
        self.view_function = view_function
        self.redirect_to = redirect_to

    def __call__(self, request, *args, **kwargs):
        if request.user is not None and request.user.is_authenticated():
            return redirect(self.redirect_to)
        return self.view_function(request, *args, **kwargs)

## Décorateur teacher_required\n
# Vérifie que l'utilisateur est bien un professeur (groupe 'teacher')\n
# Redirige l'utilisateur vers la page backoffice:teachers_required si l'utilisateur ne possède pas les droits
def teacher_required(function):
    def test_group(request, *args, **kwargs):
        if request.user.groups.filter(name='teachers').count() > 0:
            return function(request, *args, **kwargs)
        else:
            return redirect("backoffice:teachers_required")
    return test_group
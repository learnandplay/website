from django.shortcuts import redirect

def anonymous_required(view_function, redirect_to = None):
    return AnonymousRequired(view_function, redirect_to)

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

def teacher_required(function):
    def test_group(request, *args, **kwargs):
        if request.user.groups.filter(name='teachers').count() > 0:
            return function(request, *args, **kwargs)
        else:
            return redirect("backoffice:teachers_required")
    return test_group
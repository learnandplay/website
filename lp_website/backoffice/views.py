# -*- coding: UTF-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect, HttpResponse
from backoffice.forms import UserRegistrationForm, UserLoginForm
from backoffice.models import LPUser
from backoffice.decorators import anonymous_required, teacher_required

@login_required
@teacher_required
def index(request):
    return render(request, 'backoffice/index.html')

@anonymous_required
def register(request):
    registered = False
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.groups.add(Group.objects.get(name='teachers'))
            user.save()
            lp_user = LPUser()
            lp_user.user = user
            lp_user.save()
            registered = True
    else:
        form = UserRegistrationForm()
    return render(request, 'backoffice/register.html',
        {'registration_form': form, 'registered': registered})

@anonymous_required
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if not data.get('remember_me', None):
                request.session.set_expiry(0)
            user = authenticate(username=data.get('username'), password=data.get('password'))
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect('backoffice:index')
                else:
                    return HttpResponse("Votre compte est désactivé.")
            else:
                return HttpResponse("Identifiants invalides.")
    else:
        form = UserLoginForm()
        return render(request, 'backoffice/login.html',
                      {'login_form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('backoffice:index')

@login_required
def teachers_required(request):
    return render(request, 'backoffice/teachers_required.html')
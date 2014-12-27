# -*- coding: UTF-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from backoffice.forms import UserRegistrationForm, UserLoginForm, ClassForm
from backoffice.models import LPUser, SchoolClass
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

@login_required
@teacher_required
def my_classes(request):
    user = request.user.LPUser
    classes = user.school_class.all()
    return render(request, 'backoffice/my_classes.html',
        {'classes': classes})

@login_required
@teacher_required
def edit_class(request, id=None):
    school_class = SchoolClass.objects.get(id=id) if id else None
    form = ClassForm(request.POST or None, instance=school_class)
    if form.is_valid():
        school_class = form.save()
        if not id:
            request.user.LPUser.school_class.add(school_class)
        return redirect('backoffice:my_classes')
    return render(request, 'backoffice/edit_class.html',
        {'class_form': form, 'school_class': school_class})
# -*- coding: UTF-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from backoffice.forms import UserRegistrationForm, UserLoginForm, ClassForm, StudentAvatarForm, StudentForm, AddAdministratorForm
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

@login_required
@teacher_required
def delete_user(request):
    user_id = request.POST.get("user_id")
    if user_id is not None:
        LPUser.objects.get(id=user_id).delete()
    return redirect(request.META.get('HTTP_REFERER', reverse('backoffice:index')))

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
    return render(request, 'backoffice/my_classes.html')

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

@login_required
@teacher_required
def delete_class(request):
    print "Ca passe ici"
    class_id = request.POST.get("class_id")
    print class_id
    if class_id is not None:
        SchoolClass.objects.get(id=class_id).delete()
    print "Ca passe là"
    return redirect(request.META.get('HTTP_REFERER', reverse('backoffice:my_classes')))

@login_required
@teacher_required
def my_students(request, class_id=None):
    selected_class = None
    students = None
    classes = SchoolClass.objects.all()
    if classes and class_id is None:
        selected_class = classes[0]
    elif class_id is not None:
        selected_class = SchoolClass.objects.get(id=class_id)
    if selected_class is not None:
        students = selected_class.lpuser_set.filter(user__groups__name__in=['students'])
    return render(request, 'backoffice/my_students.html',
        {'classes': classes, 'selected_class': selected_class, 'students': students})

@login_required
@teacher_required
def edit_student(request, class_id, id=None):
    school_class = SchoolClass.objects.get(id=class_id)
    student = LPUser.objects.get(id=id) if id else None
    instance = student.user if student else None
    avatar_form = StudentAvatarForm(request.POST, request.FILES)
    form = StudentForm(request.POST or None, instance=instance)
    if form.is_valid():
        user = form.save()
        user.set_password("password")
        user.save()
        if not id:
            user.groups.add(Group.objects.get(name='students'))
            lp_user = LPUser()
            lp_user.user = user
            lp_user.save()
            lp_user.school_class.add(school_class)
        else:
            lp_user = student
        if avatar_form.is_valid():
            lp_user.avatar = avatar_form.cleaned_data['avatar']
            lp_user.save()
        return redirect(reverse('backoffice:my_students', kwargs={'class_id': class_id}))

    return render(request, 'backoffice/edit_student.html',
        {'avatar_form': avatar_form, 'student_form': form, 'school_class': school_class, 'student': student})

@login_required
@teacher_required
def class_administrators(request, class_id):
    school_class = SchoolClass.objects.get(id=class_id)
    add_administrator_form = AddAdministratorForm(request.POST)
    add_username_failed = None
    if add_administrator_form.is_valid() and add_administrator_form.cleaned_data.get('username'):
        try:
            username = add_administrator_form.cleaned_data.get('username')
            user = LPUser.objects.filter(user__groups__name__in=['teachers']).get(user__username=add_administrator_form.cleaned_data.get('username'))
            user.school_class.add(school_class)
        except LPUser.DoesNotExist:
            add_username_failed = username
        add_administrator_form = AddAdministratorForm()
    administrators = school_class.lpuser_set.filter(user__groups__name__in=['teachers'])
    return render(request, 'backoffice/class_administrators.html',
        {'add_administrator_form': add_administrator_form, 'administrators': administrators, 'school_class': school_class,
        'add_username_failed': add_username_failed})

@login_required
@teacher_required
def delete_administrator(request):
    class_id = request.POST.get("class_id")
    administrator_id = request.POST.get("administrator_id")
    if class_id is not None and administrator_id is not None:
        LPUser.objects.get(id=administrator_id).school_class.remove(SchoolClass.objects.get(id=class_id))
    if request.user.id == administrator_id:
        return redirect(reverse('backoffice:my_classes'))
    else:
        return redirect(reverse('backoffice:class_administrators', kwargs={'class_id': class_id}))

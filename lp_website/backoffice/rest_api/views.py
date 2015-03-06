# -*- coding: UTF-8 -*-
import json
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from rest_framework.response import Response
from backoffice.decorators import anonymous_required, teacher_required
from backoffice.models import LPUser, SchoolClass
from backoffice.rest_api.serializers import LPUserSerializer, SchoolClassSerializer
from pprint import pprint


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@login_required
@teacher_required
def get_user_schoolclasses(request):
    user = request.user.LPUser
    classes = user.school_class.all().order_by('name')
    serializer = SchoolClassSerializer(classes, many=True)
    return JSONResponse(serializer.data)

@login_required
@teacher_required
def delete_school_class(request):
	post = json.loads(request.body)
	SchoolClass.objects.get(id=post['class_id']).delete()
	response = {}
	response['result'] = 'success'
	response['deleted'] = post['class_id']
	return JSONResponse(json.dumps(response))

@login_required
@teacher_required
def get_all_classes_students(request):
	user = request.user.LPUser
	school_classes = user.school_class.all().order_by('name')
	school_class_serializer = SchoolClassSerializer(school_classes, many=True)
	response = {}
	response['school_classes'] = school_class_serializer.data
	response['students'] = {}
	for school_class in school_classes:
		user_serializer = LPUserSerializer(school_class.lpuser_set.filter(user__groups__name__in=['students']).order_by('user__username'), many=True)
		response['students'][school_class.id] = user_serializer.data
	return JSONResponse(json.dumps(response))

@login_required
@teacher_required
def delete_user(request):
    post = json.loads(request.body)
    user_id = post['user_id']
    response = {}
    if user_id is not None:
        LPUser.objects.get(id=user_id).delete()
        response['result'] = 'success'
        response['deleted'] = user_id
    else:
    	response['result'] = 'failure'
    return JSONResponse(json.dumps(response))

@login_required
@teacher_required
def get_schoolclass_administrators(request, class_id):
    try:
        school_class = SchoolClass.objects.get(id=class_id)
    except SchoolClass.DoesNotExist:
        return HttpResponse(status=400)
    administrators = school_class.lpuser_set.filter(user__groups__name__in=['teachers']).order_by('user__username')
    response = LPUserSerializer(administrators, many=True).data
    return JSONResponse(json.dumps(response))

@login_required
@teacher_required
def remove_administrator(request):
    post = json.loads(request.body)
    class_id = post['class_id']
    administrator_id = post['administrator_id']
    response = {}
    if class_id is not None and administrator_id is not None:
        try:
            LPUser.objects.get(id=administrator_id).school_class.remove(SchoolClass.objects.get(id=class_id))
        except (LPUser.DoesNotExist, SchoolClass.DoesNotExist):
            return HttpResponse(status=400)
        response['result'] = 'success'
        response['removed'] = administrator_id
        response['class_id'] = class_id
    else:
        return HttpResponse(status=400)
    if request.user.id == administrator_id:
        response['needRedirect'] = reverse('backoffice:my_classes')
    return JSONResponse(json.dumps(response))

@login_required
@teacher_required
def add_administrator(request):
    post = json.loads(request.body)
    response = {}
    try:
        user = LPUser.objects.filter(user__groups__name__in=['teachers']).get(user__username=post['username'])
        if user.school_class.filter(id=post['class_id']).exists():
            return HttpResponse(status=400)
        school_class = SchoolClass.objects.get(id=post['class_id'])
        user.school_class.add(school_class)
        response['result'] = 'success'
        response['added_administrator'] = LPUserSerializer(user).data
    except (LPUser.DoesNotExist, SchoolClass.DoesNotExist):
        return HttpResponse(status=400)
    return JSONResponse(json.dumps(response))        
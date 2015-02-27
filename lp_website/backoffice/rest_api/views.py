# -*- coding: UTF-8 -*-
import json
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from rest_framework.renderers import JSONRenderer
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
    post = json.loads(request.body);
    user_id = post['user_id']
    response = {}
    if user_id is not None:
        LPUser.objects.get(id=user_id).delete()
        response['result'] = 'success'
        response['deleted'] = user_id
    else:
    	response['result'] = 'failure'
    return JSONResponse(json.dumps(response))
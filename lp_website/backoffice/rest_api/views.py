# -*- coding: UTF-8 -*-
import json
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from rest_framework.renderers import JSONRenderer
from backoffice.decorators import anonymous_required, teacher_required
from backoffice.models import LPUser, SchoolClass
from backoffice.rest_api.serializers import SchoolClassSerializer
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
    classes = user.school_class.all()
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
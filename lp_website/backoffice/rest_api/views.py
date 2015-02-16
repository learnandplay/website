# -*- coding: UTF-8 -*-
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from rest_framework.renderers import JSONRenderer
from backoffice.decorators import anonymous_required, teacher_required
from backoffice.models import LPUser, SchoolClass
from backoffice.rest_api.serializers import SchoolClassSerializer


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
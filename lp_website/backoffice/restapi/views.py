from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from backoffice.models import LPUser, SchoolClass, Statistics, Subject, Exercise, SubjectConfig, ExerciseConfig
from backoffice.restapi.serializers import SchoolClassSerializer, LPUserSerializer, SubjectConfigSerializer, ExerciseConfigSerializer

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

class GetClasses(APIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, )

    def get(self, request):
        user = request.user.LPUser
        classes = user.school_class.all().order_by('name')
        serializer = SchoolClassSerializer(classes, many=True)
        return JSONResponse(serializer.data)

class GetStudents(APIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, )

    def get(self, request, class_id):
        try:
            user = request.user.LPUser
            school_class = user.school_class.get(id=class_id)
        except SchoolClass.DoesNotExist:
            return HttpResponse(status=400)
        students =  school_class.lpuser_set.filter(user__groups__name__in=['students']).order_by('user__username')
        serializer = LPUserSerializer(students, many=True)
        return JSONResponse(serializer.data)

class GetSubjectConfig(APIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, )

    def get(self, request, class_id, ref):
        try:
            user = request.user.LPUser
            my_school_class = user.school_class.get(id=class_id)
            subject_ref = Subject.objects.filter(reference=ref)
            subject_config = SubjectConfig.objects.filter(school_class=my_school_class, subject=subject_ref).order_by('-start_date')[:1]
        except (SchoolClass.DoesNotExist, SubjectConfig.DoesNotExist, Subject.DoesNotExist):
            return HttpResponse(status=400)
        serializer = SubjectConfigSerializer(subject_config, many=True)
        return JSONResponse(serializer.data)

class GetExerciseConfig(APIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, )

    def get(self, request, class_id, ref):
        try:
            user = request.user.LPUser
            my_school_class = user.school_class.get(id=class_id)
            exercise_ref = Exercise.objects.filter(reference=ref)
            exercise_config = ExerciseConfig.objects.filter(school_class=my_school_class, exercise=exercise_ref).order_by('-start_date')[:1]
        except (SchoolClass.DoesNotExist, ExerciseConfig.DoesNotExist, Exercise.DoesNotExist):
            return HttpResponse(status=400)
        serializer = ExerciseConfigSerializer(exercise_config, many=True)
        return JSONResponse(serializer.data)

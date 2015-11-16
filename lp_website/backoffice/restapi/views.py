# -*- coding: UTF-8 -*-
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

"""
@apiDefine teacher_required
@apiHeader {String} Authorization Format : "Authorization: JWT <your_token>" : Authentification de la requête
"""

"""
@apiDefine UNAUTHORIZED
@apiError UNAUTHORIZED Le token n'est pas inclus dans le header ou est invalide

@apiErrorExample Error-Response:
    HTTP 401 UNAUTHORIZED
    {
        "detail": "Authentication credentials were not provided."
    }
"""

"""
@api {post} /api-token-auth/ Récupérer le token d'authentification
@apiParam {String} username Nom d'utilisateur
@apiParam {String} password Mot de passe
@apiVersion 0.1.0
@apiName api-token-auth
@apiGroup Authentification

@apiSuccess {String} token Token d'authentification

@apiSuccessExample Success-Response:
    HTTP 200 OK
    {
        "token": "a_token"
    }

@apiError BADREQUEST La paire nom d'utilisateur / mot de passe n'est pas valide

@apiErrorExample Error-Response:
    HTTP 400 BAD REQUEST
    {
        "non_field_errors": [
            "Unable to login with provided credentials."
            ]
    }
"""

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

class GetClasses(APIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, )
    """
    @api {get} /classes/ Récupérer les classes de l'utilisateur
    @apiUse teacher_required
    @apiVersion 0.1.0
    @apiName GetClasses
    @apiGroup Classes

    @apiSuccess {Object[]} classes             Liste des classes
    @apiSuccess {Number}   classes.id          ID de la classe
    @apiSuccess {String}   classes.name        Nom de la classe
    @apiSuccess {String}   classes.school_name Nom de l'établissement
    @apiSuccess {String}   classes.ip          IP du serveur

    @apiSuccessExample Success-Response:
        HTTP/1.1 200 OK
        [
            {"id":1,"name":"CP 1","school_name":"Ecole Albert Camus","ip":"127.0.0.1"},
            {"id":2,"name":"CP 2","school_name":"Ecole Albert Camus","ip":"188.165.200.111"}
        ]

    @apiUse UNAUTHORIZED
    """
    def get(self, request):
        user = request.user.LPUser
        classes = user.school_class.all().order_by('name')
        serializer = SchoolClassSerializer(classes, many=True)
        return JSONResponse(serializer.data)

class GetStudents(APIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, )
    """
    @api {get} /students/:class_id/ Récupérer la liste des élèves d'une classe
    @apiUse teacher_required
    @apiVersion 0.1.0
    @apiName GetStudents
    @apiGroup Classes

    @apiSuccess {Object[]} students         Liste des étudiants
    @apiSuccess {Number}   students.id      ID de l'étudiant
    @apiSuccess {String}   student.username Nom d'utilisateur'

    @apiSuccessExample Success-Response:
        HTTP/1.1 200 OK
        [
            {"id":11,"username":"Anthony.Payet"},
            {"id":3,"username":"Benjamin.Boisset"},
            ...
            {"id":8,"username":"Romain.Brunet"}
        ]

    @apiUse UNAUTHORIZED
    """
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
    """
    @api {get} /subject-config/:class_id/:reference/ Récupérer la configuration d'une matière
    @apiUse teacher_required
    @apiVersion 0.1.0
    @apiName GetSubjectConfig
    @apiGroup Configuration

    @apiSuccess {Number}    id          ID de la configuration
    @apiSuccess {String}    name        Nom de la configuration
    @apiSuccess {Object}    data        Json de configuration
    @apiSuccess {String}    reference   Référence de la matière

    @apiSuccessExample Success-Response:
        HTTP/1.1 200 OK
        {
            "id":1,
            "name":"Anglais bloqué",
            "data":"{\"accessible\": false, \"config_name\": \"Anglais bloqué\", \"school_class\": \"2\"}",
            "reference":"en"
        }

    @apiUse UNAUTHORIZED
    """
    def get(self, request, class_id, ref):
        try:
            user = request.user.LPUser
            my_school_class = user.school_class.get(id=class_id)
            subject_ref = Subject.objects.get(reference=ref)
            subject_config = SubjectConfig.objects.filter(school_class=my_school_class, subject=subject_ref).order_by('-modification_date')[:1]
        except (SchoolClass.DoesNotExist, SubjectConfig.DoesNotExist, Subject.DoesNotExist):
            return HttpResponse(status=400)
        serializer = SubjectConfigSerializer(subject_config[0])
        return JSONResponse(serializer.data)

class GetExerciseConfig(APIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, )
    """
    @api {get} /exercise-config/:class_id/:reference/ Récupérer la configuration d'un exercice
    @apiUse teacher_required
    @apiVersion 0.1.0
    @apiName GetExerciseConfig
    @apiGroup Configuration

    @apiSuccess {Number}    id          ID de la configuration
    @apiSuccess {String}    name        Nom de la configuration
    @apiSuccess {Object}    data        Json de configuration
    @apiSuccess {String}    reference   Référence de l'exercice'

    @apiSuccessExample Success-Response:
        HTTP/1.1 200 OK
        {
            "id":1,
            "name":"Config anglais lecture bloqué",
            "data":"{\"accessible\": false, \"config_name\": \"Config anglais lecture bloqué\", \"school_class\": \"2\"}",
            "reference":"en-lecture"
        }

    @apiUse UNAUTHORIZED
    """
    def get(self, request, class_id, ref):
        try:
            user = request.user.LPUser
            my_school_class = user.school_class.get(id=class_id)
            exercise_ref = Exercise.objects.get(reference=ref)
            exercise_config = ExerciseConfig.objects.filter(school_class=my_school_class, exercise=exercise_ref).order_by('-modification_date')[:1]
        except (SchoolClass.DoesNotExist, ExerciseConfig.DoesNotExist, Exercise.DoesNotExist):
            return HttpResponse(status=400)
        serializer = ExerciseConfigSerializer(exercise_config[0])
        return JSONResponse(serializer.data)

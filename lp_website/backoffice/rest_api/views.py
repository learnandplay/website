# -*- coding: UTF-8 -*-
## @package api
# API de la partie backoffice\n
# Il est nécessaire d'être un utilisateur authentifié de type 'teacher' pour utiliser cette API\n
# Les réponses sont au format JSON
import json
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from rest_framework.response import Response
from backoffice.decorators import anonymous_required, teacher_required
from backoffice.models import LPUser, SchoolClass, Statistics, Subject, Exercise, SubjectConfig, ExerciseConfig
from backoffice.rest_api.serializers import LPUserSerializer, SchoolClassSerializer, StatisticsSerializer, SubjectSerializer, ExerciseSerializer
from pprint import pprint

## Classe JSONResponse\n
# Génère une réponse de type JSON\n
# Utilisé pour générer les réponses de l'API
class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

## get_user_schoolclasses\n
# Requête GET
# @returns Toutes les classes dont l'utilisateur loggé est un administrateur
@login_required
@teacher_required
def get_user_schoolclasses(request):
    user = request.user.LPUser
    classes = user.school_class.all().order_by('name')
    serializer = SchoolClassSerializer(classes, many=True)
    return JSONResponse(serializer.data)

## delete_school_class\n
# Supprimer une classe\n
# Requête POST
# @param class_id ID de la classe à supprimer
# @returns Une erreur 400 si la classe n'existe pas, sinon un json confirmant la suppression
@login_required
@teacher_required
def delete_school_class(request):
    post = json.loads(request.body)
    try:
        SchoolClass.objects.get(id=post['class_id']).delete()
    except SchoolClass.DoesNotExist:
        return HttpResponse(status=400)
    response = {}
    response['result'] = 'success'
    response['deleted'] = post['class_id']
    return JSONResponse(json.dumps(response))

## get_all_classes_students\n
# Requête GET
# @returns Toutes les classes liées au professeur ainsi que les élèves dans chaque classe
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


## delete_user\n
# Supprimer un utilisateur\n
# Requête POST
# @param user_id ID de l'utilisateur à supprimer
# @returns Une erreur 400 si l'utilisateur n'existe pas, sinon un json confirmant la suppression
@login_required
@teacher_required
def delete_user(request):
    post = json.loads(request.body)
    user_id = post['user_id']
    response = {}
    if user_id is not None:
        try:
            lp_user = LPUser.objects.get(id=user_id)
            lp_user.user.delete()
            lp_user.delete()
        except LPUser.DoesNotExist:
            return HttpResponse(status=400)
        response['result'] = 'success'
        response['deleted'] = user_id
    else:
        return HttpResponse(status=400)
    return JSONResponse(json.dumps(response))

## get_schoolclass_administrators\n
# Récupérer la liste des administrateurs pour une classe donnée\n
# Requête GET
# @param class_id ID de la classe
# @returns Une erreur 400 si la classe n'existe pas, sinon la liste des administrateurs associés à la classe
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

## remove_administrator\n
# Retirer les droits d'administrateur d'un utilisateur sur une classe\n
# Requête POST
# @param class_id ID de la classe
# @param administrator_id ID de l'administrateur
# @returns Une erreur 400 si la classe n'existe pas ou si l'utilisateur n'en est pas administrateur, sinon un json confirmant la suppression
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

## add_administrator\n
# Ajouter un administrateur à une classe\n
# Requête POST
# @param class_id ID de la classe
# @param username Username de l'utilisateur à ajouter en administrateur
# @returns Une erreur 400 si la classe ou l'utilisateur n'existe pas, sinon un json confirmant la suppression
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

## get_statistics\n
# Recuperer les statistiques associees a un eleve ou une classe\n
# Requête GET
# @param class_id ID de la classe
# @param student_id Id de l'utilisateur
# @returns Les statistiques de l'utilisateur ou les statistiques de la classe si student_id == -1
@login_required
@teacher_required
def get_statistics(request, class_id, student_id):
    class_id = int(class_id)
    student_id = int(student_id)
    stats = None
    if student_id == -1:
        stats = Statistics.objects.filter(user__school_class__id__in=[class_id]).order_by('user__user__username', 'date')
    else:
        stats = Statistics.objects.filter(user__id__in=[student_id]).order_by('date')
    response = StatisticsSerializer(stats, many=True).data
    return JSONResponse(json.dumps(response))

@login_required
@teacher_required
def get_subjects(request):
    subjects = Subject.objects.all().order_by('name')
    serializer = SubjectSerializer(subjects, many=True)
    return JSONResponse(serializer.data)

@login_required
@teacher_required
def get_subjects_exercices(request):
    response = {}
    subjects = Subject.objects.all().order_by('name')
    subjects_serializer = SubjectSerializer(subjects, many=True)
    response['subjects'] = subjects_serializer.data
    exercises = Exercise.objects.all().order_by('subject__name', 'name')
    exercises_serializer = ExerciseSerializer(exercises, many=True)
    response['exercises'] = exercises_serializer.data
    return JSONResponse(json.dumps(response))

@login_required
@teacher_required
def save_subject_config(request):
    post = json.loads(request.body)
    subject_id = post['subject_id']
    data = json.dumps(post['data'])
    response = {}
    try:
        if subject_id is not None and data is not None:
            subject = Subject.objects.get(id=subject_id)
            subject_config = SubjectConfig()
            subject_config.subject = subject
            subject_config.data = data
            subject_config.save()
            response['result'] = 'success'
    except (Subject.DoesNotExist):
        return HttpResponse(status=400)
    return JSONResponse(json.dumps(response))

@login_required
@teacher_required
def save_exercise_config(request):
    post = json.loads(request.body)
    exercise_id = post['exercise_id']
    data = json.dumps(post['data'])
    response = {}
    try:
        if exercise_id is not None and data is not None:
            exercise = Exercise.objects.get(id=exercise_id)
            exercise_config = ExerciseConfig()
            exercise_config.exercise = exercise
            exercise_config.data = data
            exercise_config.save()
    except (Exercise.DoesNotExist):
        return HttpResponse(status=400)
    return JSONResponse(json.dumps(response))

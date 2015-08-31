# -*- coding: UTF-8 -*-
## @package serializers
# Serializers basés sur les serializers de django rest_framework
from backoffice.models import LPUser, SchoolClass, Statistics, Subject, SubjectConfig, Exercise, ExerciseConfig
from rest_framework import serializers
from django.core.urlresolvers import reverse
import json

## Classe SchoolClassSerializer\n
# Serialise une classe
class SchoolClassSerializer(serializers.ModelSerializer):
	## url pour éditer la classe
	edit_url = serializers.SerializerMethodField('generate_edit_url')
	## url pour consulter les administrateurs de la classe
	administrators_url = serializers.SerializerMethodField('generate_administrator_url')
	## url pour ajouter un étudiant dans la classe
	create_student_url = serializers.SerializerMethodField('generate_create_student_url')

	## Génère l'url pour éditer la classe
	# @param schoolclass La classe
	# @returns l'url pour éditer la classe
	def generate_edit_url(self, schoolclass):
		return reverse('backoffice:edit_class', kwargs={'id': schoolclass.id})

	## Génère l'url pour consulter les administrateurs de la classe
	# @param schoolclass La classe
	# @returns l'url pour consulter les administrateurs de la classe
	def generate_administrator_url(self, schoolclass):
		return reverse('backoffice:class_administrators', kwargs={'class_id': schoolclass.id})

	## Génère l'url pour ajouter un étudiant dans la classe
	# @param schoolclass La classe
	# @returns l'url pour ajouter un étudiant dans la classe
	def generate_create_student_url(self, schoolclass):
		return reverse('backoffice:create_student', kwargs={'class_id': schoolclass.id})

	class Meta:
		model = SchoolClass
		fields = ('id', 'name', 'school_name', 'edit_url', 'administrators_url', 'create_student_url')

## Classe LPUserSerializer\n
# Serialise un utilisateur
class LPUserSerializer(serializers.ModelSerializer):
	## Nom d'utilisateur
	username = serializers.SerializerMethodField('generate_username')
	## url pour éditer l'utilisateur
	edit_url = serializers.SerializerMethodField('generate_edit_url')

	## Génère le nom d'utilisateur
	# @param lpuser L'utilisateur
	# @returns Le nom d'utilisateur
	def generate_username(self, lpuser):
		return lpuser.user.username

	## Génère l'url pour éditer l'utilisateur
	# @param lpuser L'utilisateur
	# @returns L'url pour éditer l'utilisateur
	def generate_edit_url(self, lpuser):
		return reverse('backoffice:edit_student', kwargs={'class_id': lpuser.school_class.all()[0].id, 'id': lpuser.id})

	class Meta:
		model = LPUser
		fields = ('id', 'username', 'edit_url', 'data')

## Classe StatisticsSerializer\n
# Serialise une statistique
class StatisticsSerializer(serializers.ModelSerializer):
	## Nom d'utilisateur
	username = serializers.SerializerMethodField('generate_username')
	## Matiere scolaire
	subject = serializers.SerializerMethodField('generate_subject')
	## Exercice
	exercise = serializers.SerializerMethodField('generate_exercise')

	## Génère le nom d'utilisateur
	# @param statistics Une statistique
	# @returns Le nom d'utilisateur
	def generate_username(self, statistics):
		return statistics.user.user.username

	## Génère la matiere scolaire
	# @param statistics Une statistique
	# @returns La matiere scolaire
	def generate_subject(self, statistics):
		return statistics.exercise.subject.name

	## Génère l'exercice'
	# @param statistics Une statistique
	# @returns Le nom de l'exercice
	def generate_exercise(self, statistics):
		return statistics.exercise.name

	class Meta:
		model = Statistics
		fields = ('username', 'subject', 'exercise', 'date', 'data')


class SubjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Subject
		fields = ('id', 'name', 'data')


class SubjectConfigSerializer(serializers.ModelSerializer):
	edit_url = serializers.SerializerMethodField('generate_edit_url')

	delete_url = serializers.SerializerMethodField('generate_delete_url')

	base_name = serializers.SerializerMethodField('generate_base_name')

	school_class = serializers.SerializerMethodField('generate_school_class')

	def generate_edit_url(self, subjectConfig):
		return reverse('backoffice:subject_configuration', kwargs={'subject_id': subjectConfig.id})

	def generate_delete_url(self, subjectConfig):
		return reverse('backoffice:api_delete_subject_configuration')

	def generate_base_name(self, subjectConfig):
		return subjectConfig.subject.name

	def generate_school_class(self, subjectConfig):
		return subjectConfig.school_class.name + ' - ' + subjectConfig.school_class.school_name

	class Meta:
		model = SubjectConfig
		fields = ('id', 'name', 'start_date', 'end_date', 'data', 'edit_url', 'delete_url', 'base_name', 'school_class')


class ExerciseSerializer(serializers.ModelSerializer):
	subject = serializers.SerializerMethodField('generate_subject')

	def generate_subject(self, exercise):
		return exercise.subject.name

	class Meta:
		model = Exercise
		fields = ('id', 'name', 'subject', 'data')


class ExerciseConfigSerializer(serializers.ModelSerializer):
	edit_url = serializers.SerializerMethodField('generate_edit_url')

	delete_url = serializers.SerializerMethodField('generate_delete_url')

	base_name = serializers.SerializerMethodField('generate_base_name')

	school_class = serializers.SerializerMethodField('generate_school_class')

	def generate_edit_url(self, exerciseConfig):
		return reverse('backoffice:exercise_configuration', kwargs={'exercise_id': exerciseConfig.id})

	def generate_delete_url(self, exerciseConfig):
		return reverse('backoffice:api_delete_exercise_configuration')

	def generate_base_name(self, exerciseConfig):
		return exerciseConfig.exercise.subject.name + ' - ' + exerciseConfig.exercise.name

	def generate_school_class(self, exerciseConfig):
		return exerciseConfig.school_class.name + ' - ' + exerciseConfig.school_class.school_name

	class Meta:
		model = ExerciseConfig
		fields = ('id', 'name', 'start_date', 'end_date', 'data', 'edit_url', 'delete_url', 'base_name', 'school_class')

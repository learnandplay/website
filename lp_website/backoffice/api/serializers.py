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
        ## url pour visualiser un profil
	view_url = serializers.SerializerMethodField('generate_view_url')

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

        ## Génère l'url pour visualiser un profil
	# @param lpuser L'utilisateur
	# @returns L'url pour visualiser le profil
	def generate_view_url(self, lpuser):
		return reverse('backoffice:view_profile', kwargs={'class_id': lpuser.school_class.all()[0].id, 'id': lpuser.id})

	class Meta:
		model = LPUser
		fields = ('id', 'username', 'edit_url', 'view_url', 'data')

## Classe StatisticsSerializer\n
# Serialise une statistique
class StatisticsSerializer(serializers.ModelSerializer):
	## Nom d'utilisateur
	username = serializers.SerializerMethodField('generate_username')
	## Matiere scolaire
	subject = serializers.SerializerMethodField('generate_subject')
	## Exercice
	exercise = serializers.SerializerMethodField('generate_exercise')
	## Date formattée
	datestring = serializers.SerializerMethodField('generate_datestring')

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

	## Génère l'exercice
	# @param statistics Une statistique
	# @returns Le nom de l'exercice
	def generate_exercise(self, statistics):
		return statistics.exercise.name

	## Génère la date formatée
	# @param statistics Une statistique
	# @returns Une string contenant la date formatée
	def generate_datestring(self, statistics):
		return statistics.date.strftime('%d/%m/%Y %Hh%M')

	class Meta:
		model = Statistics
		fields = ('username', 'subject', 'exercise', 'date', 'datestring','data')

## Classe SubjectSerializer\n
# Serialise une matiere
class SubjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Subject
		fields = ('id', 'name', 'data')

## Classe SubjectConfigSerializer\n
# Serialise une configuration de matiere
class SubjectConfigSerializer(serializers.ModelSerializer):
	## url pour éditer la configuration
	edit_url = serializers.SerializerMethodField('generate_edit_url')
	## url pour supprimer la configuration
	delete_url = serializers.SerializerMethodField('generate_delete_url')
	## nom de la matiere de base
	base_name = serializers.SerializerMethodField('generate_base_name')
	## classe a laquelle s'applique la configuration
	school_class = serializers.SerializerMethodField('generate_school_class')

	## Génère l'url pour éditer la configuration
	# @param subjectConfig La configuration
	# @returns l'url pour éditer la configuration
	def generate_edit_url(self, subjectConfig):
		return reverse('backoffice:subject_configuration', kwargs={'subject_id': subjectConfig.id})

	## Génère l'url pour supprimer la configuration
	# @param subjectConfig La configuration
	# @returns l'url pour supprimer la configuration
	def generate_delete_url(self, subjectConfig):
		return reverse('backoffice:api_delete_subject_configuration')

	## Génère le nom de la matiere de base
	# @param subjectConfig La configuration
	# @returns La matiere scolaire
	def generate_base_name(self, subjectConfig):
		return subjectConfig.subject.name

	## Génère le nom de la classe associée
	# @param subjectConfig La configuration
	# @returns Le nom de la classe associée
	def generate_school_class(self, subjectConfig):
		return subjectConfig.school_class.name + ' - ' + subjectConfig.school_class.school_name

	class Meta:
		model = SubjectConfig
		fields = ('id', 'name', 'start_date', 'end_date', 'data', 'edit_url', 'delete_url', 'base_name', 'school_class')

## Classe ExerciseSerializer\n
# Serialise un exercice
class ExerciseSerializer(serializers.ModelSerializer):
	## nom de la matiere associée
	subject = serializers.SerializerMethodField('generate_subject')

	## Génère le nom de la matiere associée
	# @param exercise L'exercice'
	# @returns La matiere scolaire
	def generate_subject(self, exercise):
		return exercise.subject.name

	class Meta:
		model = Exercise
		fields = ('id', 'reference', 'name', 'subject', 'data')

## Classe ExerciseConfigSerializer\n
# Serialise une configuration d'exercice
class ExerciseConfigSerializer(serializers.ModelSerializer):
	## url pour éditer la configuration
	edit_url = serializers.SerializerMethodField('generate_edit_url')
	## url pour supprimer la configuration
	delete_url = serializers.SerializerMethodField('generate_delete_url')
	## nom de l'exercice de base
	base_name = serializers.SerializerMethodField('generate_base_name')
	## classe a laquelle s'applique la configuration
	school_class = serializers.SerializerMethodField('generate_school_class')

	## Génère l'url pour éditer la configuration
	# @param exerciseConfig La configuration
	# @returns l'url pour éditer la configuration
	def generate_edit_url(self, exerciseConfig):
		return reverse('backoffice:exercise_configuration', kwargs={'exercise_id': exerciseConfig.id})

	## Génère l'url pour supprimer la configuration
	# @param exerciseConfig La configuration
	# @returns l'url pour supprimer la configuration
	def generate_delete_url(self, exerciseConfig):
		return reverse('backoffice:api_delete_exercise_configuration')

	## Génère le nom de l'exercice de base
	# @param exerciseConfig La configuration
	# @returns Le nom de l'exercice
	def generate_base_name(self, exerciseConfig):
		return exerciseConfig.exercise.subject.name + ' - ' + exerciseConfig.exercise.name

	## Génère le nom de la classe associée
	# @param exerciseConfig La configuration
	# @returns Le nom de la classe associée
	def generate_school_class(self, exerciseConfig):
		return exerciseConfig.school_class.name + ' - ' + exerciseConfig.school_class.school_name

	class Meta:
		model = ExerciseConfig
		fields = ('id', 'name', 'start_date', 'end_date', 'data', 'edit_url', 'delete_url', 'base_name', 'school_class')

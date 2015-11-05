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
	class Meta:
		model = SchoolClass
		fields = ('id', 'name', 'school_name', 'ip')


## Classe LPUserSerializer\n
# Serialise un utilisateur
class LPUserSerializer(serializers.ModelSerializer):
	## Nom d'utilisateur
	username = serializers.SerializerMethodField('generate_username')

	## Génère le nom d'utilisateur
	# @param lpuser L'utilisateur
	# @returns Le nom d'utilisateur
	def generate_username(self, lpuser):
		return lpuser.user.username

	class Meta:
		model = LPUser
		fields = ('id', 'username')


## Classe SubjectConfigSerializer\n
# Serialise une configuration de matiere
class SubjectConfigSerializer(serializers.ModelSerializer):
	## Reference de la matiere
	reference = serializers.SerializerMethodField('generate_reference')

	## Génère la reference
	# @param exercise_config La configuration
	# @returns La reference
	def generate_reference(self, subject_config):
		return subject_config.subject.reference

	class Meta:
		model = SubjectConfig
		fields = ('id', 'name', 'start_date', 'end_date', 'data', 'reference')


## Classe ExerciseConfigSerializer\n
# Serialise une configuration d'exercice
class ExerciseConfigSerializer(serializers.ModelSerializer):
	## Reference de l'exercice
	reference = serializers.SerializerMethodField('generate_reference')

	## Génère la reference
	# @param exercise_config La configuration
	# @returns La reference
	def generate_reference(self, exercise_config):
		return exercise_config.exercise.reference

	class Meta:
		model = ExerciseConfig
		fields = ('id', 'name', 'start_date', 'end_date', 'data', 'reference')

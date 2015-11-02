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
		fields = ('id', 'name', 'school_name')

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
        class Meta:
                model = SubjectConfig
                fields = ('id', 'name', 'start_date', 'end_date', 'data')

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

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

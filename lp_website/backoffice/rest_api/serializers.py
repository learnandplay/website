from backoffice.models import LPUser, SchoolClass
from rest_framework import serializers
from django.core.urlresolvers import reverse


class SchoolClassSerializer(serializers.ModelSerializer):
	edit_url = serializers.SerializerMethodField('generate_edit_url')
	administrators_url = serializers.SerializerMethodField('generate_administrator_url')
	create_student_url = serializers.SerializerMethodField('generate_create_student_url')

	def generate_edit_url(self, schoolclass):
		return reverse('backoffice:edit_class', kwargs={'id': schoolclass.id})

	def generate_administrator_url(self, schoolclass):
		return reverse('backoffice:class_administrators', kwargs={'class_id': schoolclass.id})

	def generate_create_student_url(self, schoolclass):
		return reverse('backoffice:create_student', kwargs={'class_id': schoolclass.id})

	class Meta:
		model = SchoolClass
		fields = ('id', 'name', 'school_name', 'edit_url', 'administrators_url', 'create_student_url')


class LPUserSerializer(serializers.ModelSerializer):
	username = serializers.SerializerMethodField('generate_username')
	edit_url = serializers.SerializerMethodField('generate_edit_url')

	def generate_username(self, lpuser):
		return lpuser.user.username

	def generate_edit_url(self, lpuser):
		return reverse('backoffice:edit_student', kwargs={'class_id': lpuser.school_class.all()[0].id, 'id': lpuser.id})

	class Meta:
		model = LPUser
		fields = ('id', 'username', 'edit_url', 'data')
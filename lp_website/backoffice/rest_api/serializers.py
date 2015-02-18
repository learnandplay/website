from backoffice.models import SchoolClass
from rest_framework import serializers
from django.core.urlresolvers import reverse

class SchoolClassSerializer(serializers.ModelSerializer):
	edit_url = serializers.SerializerMethodField('generate_edit_url')
	administrators_url = serializers.SerializerMethodField('generate_administrator_url')

	def generate_edit_url(self, schoolclass):
		return reverse('backoffice:edit_class', kwargs={'id': schoolclass.id})

	def generate_administrator_url(self, schoolclass):
		return reverse('backoffice:class_administrators', kwargs={'class_id': schoolclass.id})

	class Meta:
		model = SchoolClass
		fields = ('id', 'name', 'school_name', 'edit_url', 'administrators_url')
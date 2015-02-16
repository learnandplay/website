from backoffice.models import SchoolClass
from rest_framework import serializers

class SchoolClassSerializer(serializers.ModelSerializer):
	class Meta:
		model = SchoolClass
		fields = ('id', 'name', 'school_name')
from django.contrib import admin
from backoffice.models import Subject, Exercise, SchoolClass, SubjectConfig, ExerciseConfig, LPUser, Statistics

admin.site.register(Subject)
admin.site.register(Exercise)
admin.site.register(SchoolClass)
admin.site.register(SubjectConfig)
admin.site.register(ExerciseConfig)
admin.site.register(LPUser)
admin.site.register(Statistics)

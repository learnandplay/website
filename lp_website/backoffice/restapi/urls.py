from django.conf.urls import include, patterns, url
from backoffice.restapi import views
from backoffice.restapi.views import GetClasses, GetStudents, GetSubjectConfig, GetExerciseConfig, PostExerciseStat, GetIfFirstExerciseUse, GetIfFirstSubjectUse, PostSaveIp

urlpatterns = patterns('',
                       url(r'^api-token-auth/$', 'rest_framework_jwt.views.obtain_jwt_token', name='restapi-token-auth'),
                       url(r'^classes/$', GetClasses.as_view(), name='restapi-classes'),
                       url(r'^students/(?P<class_id>\d+)/$', GetStudents.as_view(), name='restapi-students'),
                       url(r'^subject-config/(?P<class_id>\d+)/(?P<ref>\w+)/$', GetSubjectConfig.as_view(), name='restapi-subject-config'),
                       url(r'^exercise-config/(?P<class_id>\d+)/(?P<ref>[\w-]+)/$', GetExerciseConfig.as_view(), name='restapi-exercise-config'),
                       url(r'^save-exercise-stat/$', PostExerciseStat.as_view(), name='restapi-save-exercise-stat'),
                       url(r'^is-first-exercise-use/(?P<user_id>\d+)/(?P<ref>[\w-]+)/$', GetIfFirstExerciseUse.as_view(), name='restapi-is-first-exercise-use'),
                       url(r'^is-first-subject-use/(?P<user_id>\d+)/(?P<ref>[\w-]+)/$', GetIfFirstSubjectUse.as_view(), name='restapi-is-first-subject-use'),
                       url(r'^save-ip/$', PostSaveIp.as_view(), name='restapi-save-ip'),
)

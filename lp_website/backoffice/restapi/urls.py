from django.conf.urls import include, patterns, url
from backoffice.restapi import views
from backoffice.restapi.views import GetClasses, GetStudents

urlpatterns = patterns('',
                       url(r'^api-token-auth/$', 'rest_framework_jwt.views.obtain_jwt_token'),
                       url(r'^classes/$', GetClasses.as_view()),
                       url(r'^students/(?P<class_id>\d+)/$', GetStudents.as_view()),
                       url(r'^subject-config/(?P<class_id>\d+)/$', GetStudents.as_view()),
)

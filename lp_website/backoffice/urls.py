from django.conf.urls import include, patterns, url
from backoffice import views

urlpatterns = patterns('',
    url(r'^api/', include('backoffice.api.urls'), name='api'),
    url(r'^restapi/', include('backoffice.restapi.urls'), name='restapi'),
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^teachers_required/$', views.teachers_required, name='teachers_required'),
    url(r'^my_classes/$', views.my_classes, name='my_classes'),
    url(r'^edit_class/', include(patterns('',
    	url(r'^$', views.edit_class, name='create_class'),
    	url(r'^(?P<id>\d+)/$', views.edit_class, name='edit_class'),
    ))),
    url(r'^my_students/', include(patterns('',
        url(r'^$', views.my_students, name='my_students_default'),
        url(r'^(?P<class_id>\d+)/$', views.my_students, name='my_students'),
    ))),
    url(r'^edit_student/(?P<class_id>\d+)/', include(patterns('',
        url(r'^$', views.edit_student, name='create_student'),
        url(r'^(?P<id>\d+)/$', views.edit_student, name='edit_student'),
    ))),
    url(r'^class_administrators/(?P<class_id>\d+)/', views.class_administrators, name='class_administrators'),
    url(r'^edit_profile/$', views.edit_profile, name='edit_profile'),
    url(r'^view_profile/(?P<class_id>\d+)/(?P<id>\d+)/$', views.view_profile, name='view_profile'),
    url(r'^statistics/$', views.statistics, name='statistics'),
    url(r'^raw_statistics/$', views.raw_statistics, name='raw_statistics'),
    url(r'^configuration/', include(patterns('',
        url(r'^$', views.configuration, name='configuration'),
        url(r'^subject/(?P<subject_id>\d+)/$', views.subject_configuration, name='subject_configuration'),
        url(r'^exercise/(?P<exercise_id>\d+)/$', views.exercise_configuration, name='exercise_configuration'),
    ))),
    url(r'^my_configurations/$', views.my_configurations, name='my_configurations'),
)

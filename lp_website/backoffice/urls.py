from django.conf.urls import include, patterns, url
from backoffice import views

urlpatterns = patterns('',
    url(r'^restapi/', include('backoffice.rest_api.urls'), name='restapi'),
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^delete_user/', views.delete_user, name='delete_user'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^teachers_required/$', views.teachers_required, name='teachers_required'),
    url(r'^my_classes/$', views.my_classes, name='my_classes'),

    url(r'^edit_class/', include(patterns('',
    	url(r'^$', views.edit_class, name='create_class'),
    	url(r'^(?P<id>\d+)/$', views.edit_class, name='edit_class'),
    ))),
    url(r'^delete_class/', views.delete_class, name='delete_class'),
    url(r'^my_students/', include(patterns('',
        url(r'^$', views.my_students, name='my_students_default'),
        url(r'^(?P<class_id>\d+)/$', views.my_students, name='my_students'),
    ))),
    url(r'^edit_student/(?P<class_id>\d+)/', include(patterns('',
        url(r'^$', views.edit_student, name='create_student'),
        url(r'^(?P<id>\d+)/$', views.edit_student, name='edit_student'),
    ))),
    url(r'^class_administrators/(?P<class_id>\d+)/', views.class_administrators, name='class_administrators'),
    url(r'^delete_administrator/', views.delete_administrator, name='delete_administrator'),
)

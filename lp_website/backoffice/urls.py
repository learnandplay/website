from django.conf.urls import include, patterns, url
from backoffice import views

urlpatterns = patterns('',
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
    url(r'^delete_class/', views.delete_class, name='delete_class'),
)

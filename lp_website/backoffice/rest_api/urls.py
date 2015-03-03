from django.conf.urls import include, patterns, url
from backoffice.rest_api import views

urlpatterns = patterns('',
    url(r'^get_user_schoolclasses', views.get_user_schoolclasses, name='api_get_user_schoolclasses'),
    url(r'^delete_school_class', views.delete_school_class, name='api_delete_school_class'),
    url(r'^get_all_classes_students', views.get_all_classes_students, name='api_get_all_classes_students'),
    url(r'^delete_user', views.delete_user, name='api_delete_user'),
    url(r'^get_schoolclass_administrators/(?P<class_id>\d+)/', views.get_schoolclass_administrators, name="api_get_schoolclass_administrators"),
    url(r'^remove_administrator', views.remove_administrator, name="api_remove_administrator"),
    url(r'^add_administrator', views.add_administrator, name="api_add_administrator"),
)
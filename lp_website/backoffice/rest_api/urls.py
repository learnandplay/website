from django.conf.urls import include, patterns, url
from backoffice.rest_api import views

urlpatterns = patterns('',
    url(r'^get_user_schoolclasses', views.get_user_schoolclasses, name='api_get_user_schoolclasses'),
    url(r'^delete_school_class', views.delete_school_class, name='api_delete_school_class'),
)
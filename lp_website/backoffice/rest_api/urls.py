from django.conf.urls import include, patterns, url
from backoffice.rest_api import views

urlpatterns = patterns('',
    url(r'^get_user_schoolclasses', views.get_user_schoolclasses, name='get_user_schoolclasses'),
)
from django.conf.urls import patterns, url
from backoffice import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='backoffice-index'),
)

from django.conf.urls import url

from . import views

app_name = 'intro'
urlpatterns = [
    url('^$', views.index, name='index'),
    url(r'^intro/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^intro/(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^intro/(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
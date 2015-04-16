from django.conf.urls import patterns, url
from conferences import views

urlpatterns = patterns('',
                       url(r'^$', views.map, name='map'),
                       url(r'^about/$', views.about, name='about'),
                       url(r'^feedback/$', views.feedback, name='feedback'),
                       url(r'^conferences/$',
                           views.conferences_all, name='conferences_all'),
                       url(r'^conferences/(?P<conference_slug>[\w\-]+)/$',
                           views.conference_particular,
                           name='conference_particular'),
                       )

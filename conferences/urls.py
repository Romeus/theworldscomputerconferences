from django.conf.urls import patterns, url
from conferences import views

urlpatterns = patterns('',
                       url(r'^$', views.map, name='map'),
                       url(r'^about$', views.about, name='about'),
                       url(r'^all$', views.all, name='all'),
                       url(r'^feedback$', views.feedback, name='feedback'),
                       url(r'^conference/(?P<conference_name_slug>[\w\-]+)/$',
                           views.conference, name='category'),
                       )

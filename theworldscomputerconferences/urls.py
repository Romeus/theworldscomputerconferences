from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'', include('conferences.urls')),
                       url(r'^captcha/', include('captcha.urls')),
                       )

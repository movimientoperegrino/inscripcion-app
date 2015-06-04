from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = [
    url(r'^inicio/', include('mp.apps.inscripcion.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

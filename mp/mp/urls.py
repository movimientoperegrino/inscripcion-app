from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = [
    url(r'^inicio/', include('mp.apps.inscripcion.urls')),
    url(r'^admin/', include(admin.site.urls)),


    # DB Store plugin URLs
    url(r'^fobi/plugins/form-handlers/db-store/',
        include('fobi.contrib.plugins.form_handlers.db_store.urls')),

    # View URLs
    url(r'^fobi/', include('fobi.urls.view')),

    # Edit URLs
    url(r'^fobi/', include('fobi.urls.edit')),

]

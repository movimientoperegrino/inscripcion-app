from django.conf.urls import url
from mp.apps import inscripcion

urlpatterns = [

    url(r'^$', 'mp.apps.inscripcion.views.inicio', name='inicio')
]

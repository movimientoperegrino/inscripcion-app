from django.conf.urls import url


urlpatterns = [

    url(r'^$', 'mp.apps.inscripcion.views.inicio_vista', name='inicio'),
    url(r'^usuario$', 'mp.apps.inscripcion.views.usuario_inicio_vista', name='usuario inicio')
]

from django.conf.urls import url


urlpatterns = [

    url(r'^$', 'mp.apps.inscripcion.views.inicio_vista', name='Inicio'),
    url(r'^login$', 'mp.apps.inscripcion.views.iniciar_sesion', name='Login'),
    url(r'^actividad/(?P<id_actividad>\d+)/formulario/', 'mp.apps.inscripcion.views.formulario_actividad_view', name='Actividad'),
    url(r'^actividad/(?P<id_actividad>\d+)/inscripto/', 'mp.apps.inscripcion.views.inscriptos_actividad_view', name='Inscriptos')

]

# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseServerError
from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader
from mp.apps.inscripcion import services, queries

from mp.apps.inscripcion.models import Actividad


def inicio_vista(request):
    """ Retorna la página de inicio de la aplicación."""

    # lista_actividades = Actividad.objects.all().order_by('fechaActivacion').reverse()
    # fechaActivacion = timezone.now() + timedelta(days=16)
    # fechaFin = timezone.now() + timedelta(days=1)
    # lista_actividades = lista_actividades.exclude(fechaFin__lte=fechaFin).filter(fechaActivacion__lte=fechaActivacion)


    actividades = queries.obtener_todas_actividades_por_estados(["activo", "inactivo"])

    template_path = 'inscripcion/inicio.html'
    context = {'actividades_lista': actividades}
    return render_to_response(template_path, context,
                              context_instance=RequestContext(request))


@login_required(login_url='/login')
def actividad_agregar_vista(request):
    """Retorna la vista para crea una actividad nueva o guarda una actividad nueva."""

    if request.method == 'POST':
        # TODO Implementar POST de nuevas actividades.
        return
    else:
        actividad_vacia = Actividad

    template_path = 'inscripcion/actividad/actividad.html'
    context = []
    return render_to_response(template_path, context, context_instance=RequestContext(request)
    )


@login_required(login_url='/login')
def usuario_inicio_vista(request):
    """Retorna la vista para un usuario registado en el sistema."""

    if request.method == 'GET':
        # TODO Obtener todas las actividades por usuario y retornar la vista con este contexto.


        template_path = 'inscripcion/usuario/inicio.html'
        context = []
        return render_to_response(template_path, context, context_instance=RequestContext(request))
    else:
        return HttpResponseServerError()


# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader




# Página de inicio (Home Page)
def inicio(request):
    # lista_actividades = Actividad.objects.all().order_by('fechaActivacion').reverse()
    # fechaActivacion = timezone.now() + timedelta(days=16)
    # fechaFin = timezone.now() + timedelta(days=1)
    # lista_actividades = lista_actividades.exclude(fechaFin__lte=fechaFin).filter(fechaActivacion__lte=fechaActivacion)

    template_path = 'inscripcion/inicio.html'
    context = []
    return render_to_response(template_path,context,
                              context_instance=RequestContext(request))

# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http.response import HttpResponseServerError, HttpResponseRedirect
from django.shortcuts import render_to_response

from django.template import RequestContext

from mp.apps.inscripcion import services, queries
from mp.apps.inscripcion.exceptions import CustomError
from mp.apps.inscripcion.forms import InscripcionActividadForm


def inicio_vista(request):
    """ Retorna la página de inicio de la aplicación."""

    actividades = queries.obtener_todas_actividades_activas()

    template_path = 'inscripcion/index.html'
    context = {'actividades_lista': actividades}
    return render_to_response(template_path, context,
                              context_instance=RequestContext(request))


def mensaje_vista(request, es_exito, mensaje):
    """ Retorna la vista con el mensaje pasado por argumento. """
    template_path = 'inscripcion/actividad/mensaje.html'
    context = {'es_exito': es_exito, 'mensaje': mensaje}
    return render_to_response(template_path, context,
                              context_instance=RequestContext(request))


def formulario_actividad_view(request, id_actividad):
    """Retorna la página para inscribirse a la actividad correspondiente. """

    # Se controla si la actividad esta activa.
    es_actividad_activa = services.activar_o_desactivar_actividad(id_actividad)

    # Se controla si la actividad esta llena.
    es_actividad_llena = False
    if es_actividad_activa:
        es_actividad_llena = services.es_actividad_llena(id_actividad)
    else:
        actividad = queries.obtener_actividad_por_id(id_actividad)
        es_finalizada = services.es_actividad_finalizada(id_actividad)
        if es_finalizada:
            mensaje = 'La inscripcion a la actividad: "' + actividad.descripcion + '" ha finalizado.'
            mensaje += ' Si tiene alguna consulta, comuniquese con el encargado de inscripciones al correo: '
            mensaje += actividad.responsable.email
        else:
            mensaje = 'La inscripcion a la actividad "' + actividad.descripcion + '" aun no se encuentra habilitada.'

        return mensaje_vista(request, False, mensaje)

    if es_actividad_llena:
        actividad = queries.obtener_actividad_por_id(id_actividad)
        mensaje = 'El cupo  para "' + actividad.descripcion + '" se encuentra lleno.'
        mensaje += ' Si tiene alguna consulta, comuniquese con el encargado de inscripciones al correo: '
        mensaje += actividad.responsable.email
        return mensaje_vista(request, False, mensaje)
    else:
        if request.method == 'POST':
            try:
                inscripcion_actividad_form = InscripcionActividadForm(request.POST)
                if inscripcion_actividad_form.is_valid():
                    data = inscripcion_actividad_form.cleaned_data
                    nombre = data['nombre']
                    apellido = data['apellido']
                    fecha_nacimiento = data['fecha_nacimiento']
                    telefono = data['telefono']
                    email = data['email']
                    inscripcion_guardada = services.guardarInscripcion(id_actividad, nombre, apellido, fecha_nacimiento,
                                                                       telefono, email)
                    services.enviar_mail_inscripcion(inscripcion_guardada)

                    mensaje = 'Su solicitud ha sido procesada con exito. En breve recibira un correo de confirmacion,' \
                              'verifique la carpeta "Correo no deseado" si no encuentra el correo'
                    return mensaje_vista(request, True, mensaje)

            except CustomError, arg:
                print 'Error:', arg.msg
                actividad = queries.obtener_actividad_por_id(id_actividad)
                mensaje = 'Ya se encuentra inscripto a la actividad "' + actividad.descripcion
                mensaje += ' Si tiene alguna consulta, comuniquese con el encargado de inscripciones al correo: '
                mensaje += actividad.responsable.email
                return mensaje_vista(request, False, mensaje)
        else:
            inscripcion_actividad_form = InscripcionActividadForm()

        actividad = queries.obtener_actividad_por_id(id_actividad)
        template_path = 'inscripcion/actividad/actividad_formulario.html'
        context = {'actividad': actividad, 'inscripcion_actividad': inscripcion_actividad_form}
        return render_to_response(template_path, context,
                                  context_instance=RequestContext(request))


@login_required(login_url='/login')
def actividades_usuario(request):
    """Retorna la vista para un usuario registado en el sistema."""

    actividades_lista = None
    if request.user.is_superuser:
        actividades_lista = queries.obtener_todas_actividades_ordenadas_por_activacion()
    else:
        actividades_lista = queries.obtener_actividades_por_responsable(request.user.username)

    template_path = 'inscripcion/usuario/actividades.html'
    context = {'actividades_lista':actividades_lista}
    return render_to_response(template_path, context, context_instance=RequestContext(request))


def iniciar_sesion(request):
    if not request.user.is_anonymous():
        return actividades_usuario(request)
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return actividades_usuario(request)
    else:
        formulario = AuthenticationForm()

    template_path = 'inscripcion/usuario/login.html'
    return render_to_response(template_path, {'formulario': formulario},
                              context_instance=RequestContext(request))


@login_required(login_url='/login')
def inscriptos_actividad_view(request, id_actividad):
    """Retorna la vista que lista los inscriptos por actividad."""

    actividad = queries.obtener_actividad_por_id(id_actividad)
    inscriptos = queries.obtener_inscripciones_por_actividad(id_actividad)

    template_path = 'inscripcion/usuario/inscriptos.html'
    context = {'inscriptos':inscriptos, 'actividad':actividad}
    return render_to_response(template_path, context, context_instance=RequestContext(request))


# -*- coding: utf-8 -*-
from mp.apps.inscripcion.models import *

__author__ = 'gzacur'


def obtener_todas_actividades():
    """ Retorna todas las actividades activas """

    actividades = Actividad.objects.all()

    return actividades

def obtener_todas_actividades_ordenadas_por_activacion():
    """ Retorna todas las actividades activas """

    actividades = Actividad.objects.all().order_by('-fecha_activacion')

    return actividades

def obtener_actividades_por_responsable(responsable):
    """ Retorna todas las actividades por responsable """

    user = User.objects.filter(username=responsable)
    actividades = Actividad.objects.filter(responsable=user)

    return actividades

def obtener_todas_actividades_activas():
    """ Retorna todas las actividades activas """

    actividades = Actividad.objects.all().filter(activa=True).order_by('-fecha_activacion')

    return actividades

def obtener_actividad_por_id(id_actividad):
    """ Retorna la actividad con el id pasado por parámetro o vacio en caso de no encontrar la actividad. """

    actividad = Actividad.objects.get(pk=id_actividad)

    return actividad

def obtener_cantidad_inscriptos_por_actividad(actividad_id):
    """Retorna la cantidad de inscriptos a una actividad. """

    actividad = obtener_actividad_por_id(actividad_id)
    cantidad_inscriptos = Inscripcion.objects.filter(actividad=actividad).count()

    return cantidad_inscriptos

def obtener_posicion_inscripto_por_actividad_y_inscripcion(actividad_id, inscripcion_id):
    """Retorna la posición en la que fue se inscripbio a la actividad """

    actividad = obtener_actividad_por_id(actividad_id)
    posicion = Inscripcion.objects.filter(actividad=actividad).filter(pk__lte=inscripcion_id).count()

    return posicion

def obtener_inscripcion_estado_por_id(id_inscripcion_estado):

    estado = InscripcionEstado.objects.get(pk=id_inscripcion_estado)
    
    return estado

def obtener_parametro_por_clave(parametro_clave):

    parametro = Parametro.objects.get(clave=parametro_clave.value)

    return parametro


def obtener_inscripciones_por_actividad(id_actividad):

    actividad = obtener_actividad_por_id(id_actividad)
    inscriptos = Inscripcion.objects.all().filter(actividad=actividad).order_by('posicion')

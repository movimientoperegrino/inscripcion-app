from gc import get_objects
from mp.apps.inscripcion.models import *

__author__ = 'gzacur'

def obtener_todas_actividades_por_estados(estados):
    """ Retorna todas las actividades activas """

    actividades = Actividad.objects.all()

    return actividades

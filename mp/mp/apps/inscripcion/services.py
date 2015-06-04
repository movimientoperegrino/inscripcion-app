# -*- coding: utf-8 -*-
from django.template import Context, Template
from django.utils import timezone
from django.core.mail import EmailMultiAlternatives

from mp.apps.inscripcion import queries
from mp.apps.inscripcion.exceptions import *
from mp.apps.inscripcion.models import *
from mp.apps.inscripcion.parameters import *


__author__ = 'gzacur'


def guardarInscripcion(id_actividad, nombre, apellido, fecha_nacimiento, telefono, email):
    """ Guarda una nueva inscripcion o retorna un error en caso de no pasar las validaciones. """

    if es_actividad_llena(id_actividad):
        raise ActividadLlena('Esta actividad se encuentra llena.')

    # if existe_inscripto_en_actividad_por_email(id_actividad, email):
    #     raise InscripcionRepetida('Ya se encuentra inscripto a esta actividad')

    actividad = queries.obtener_actividad_por_id(id_actividad)
    estado = queries.obtener_inscripcion_estado_por_id(
        queries.obtener_parametro_por_clave(ParametrosInscripcion.INSCRIPCION_ESTADO_INICIAL))
    inscripcion = Inscripcion()
    inscripcion.actividad = actividad
    inscripcion.nombre = nombre
    inscripcion.apellido = apellido
    inscripcion.fecha_nacimiento = fecha_nacimiento
    inscripcion.mail = email
    inscripcion.telefono = telefono
    inscripcion.saldo = actividad.costo
    inscripcion.posicion = 0  #maximo valor para un entero. Valor temporal.
    inscripcion.participo = False
    inscripcion.estado_inscripcion = estado
    inscripcion.save()

    inscripcion.posicion = queries.obtener_posicion_inscripto_por_actividad_y_inscripcion(id_actividad, inscripcion.id)
    inscripcion.save()

    return inscripcion


def es_actividad_llena(id_actividad):
    """ Retorna falso si la actividad aún no se ha llenado, en caso contrario retorna verdadero"""

    actividad = queries.obtener_actividad_por_id(id_actividad)

    maximo_inscriptos = actividad.cantidad_suplentes + actividad.cantidad_titulares
    cantidad_inscriptos = queries.obtener_cantidad_inscriptos_por_actividad(actividad.id)

    if (cantidad_inscriptos >= maximo_inscriptos):
        return True
    else:
        return False


def activar_o_desactivar_actividad(id_actividad):
    """Verifica si debe activar o desactivar la actividad, lo hace y luego retorna True si esta activa o False si esta inactiva. """

    actividad = Actividad.objects.get(pk=id_actividad)

    fecha_activacion = actividad.fecha_activacion
    fecha_desactivacion = actividad.fecha_desactivacion
    ahora = timezone.now()

    if fecha_activacion <= ahora <= fecha_desactivacion:
        if not actividad.activa:
            actividad.activa = True
            actividad.save()
    elif actividad.activa:
        actividad.activa = False
        actividad.save()

    return actividad.activa


def existe_inscripto_en_actividad_por_email(id_actividad, email):
    """ Retorna TRUE si ya existe una inscripcion con el email pasado como argumento en la actividad con id = id_actividad, en caso contrario retorna False """

    actividad = queries.obtener_actividad_por_id(id_actividad)
    inscripcion = Inscripcion.objects.filter(actividad=actividad).filter(mail=email)

    if inscripcion.count() > 0:
        return True
    else:
        return False


def es_actividad_finalizada(id_actividad):
    """ Retorna True si la fecha de inscripción a la actividad ha finalizado."""

    actividad = queries.obtener_actividad_por_id(id_actividad)

    if timezone.now() > actividad.fecha_desactivacion:
        return True
    else:
        return False


def enviar_mail_inscripcion(inscripcion_guardada):
    """ Prepara y envia el mail para una inscripción realizada.
    """

    actividad = inscripcion_guardada.actividad

    template = None
    html_render = None
    context = None
    if inscripcion_guardada.posicion <= actividad.cantidad_titulares:
        context = Context(
            {'inscripto': inscripcion_guardada, 'contactoTitular': inscripcion_guardada.actividad.responsable.email})
        parametro = queries.obtener_parametro_por_clave(ParametrosInscripcion.MAIL_TEMPLATE_TITULAR)
        template = Template(parametro.valor)
    else:
        context = Context(
            {'inscripto': inscripcion_guardada, 'contactoTitular': inscripcion_guardada.actividad.responsable.email})
        parametro = queries.obtener_parametro_por_clave(ParametrosInscripcion.MAIL_TEMPLATE_SUPLENTE)
        template = Template(parametro.valor)

    html_render = template.render(context)
    enviar_mail("zakyur@gmail.com", html_render, "Inscripciones 2 - testing")


def enviar_mail(destino, cuerpo, asunto):
    """ Envia mails al destino con el cuerpo y el asunto pasado por parametros.
        Solo envía archivos adjuntos del tipo text/html.
        Si no desea enviar archivos adjuntos debe pasar None como parametro.
    """
    origen = 'Movimiento Peregrino <retiros-noreply@movimientoperegrino.org>'

    msg = EmailMultiAlternatives(asunto, cuerpo, origen, [destino])
    msg.attach_alternative(cuerpo, 'text/html')
    msg.send()


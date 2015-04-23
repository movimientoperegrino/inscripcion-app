# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Lugar(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    direccion = models.TextField(verbose_name="Dirección")
    descripcion = models.TextField(verbose_name="Descripción")
    latitud = models.FloatField()
    longitud = models.FloatField()

class Actividad(models.Model):
    lugar = models.ForeignKey(Lugar)
    descripcion = models.TextField(verbose_name="Descripción")
    costo = models.IntegerField()
    requisitos = models.TextField()
    fecha_inicio = models.DateTimeField(verbose_name="Fecha inicio")
    fecha_fin = models.DateTimeField(verbose_name="Fecha fin")
    fecha_activacion = models.DateTimeField(verbose_name="Fecha activacion")
    fecha_creacion = models.DateTimeField(verbose_name="Fecha creacion", auto_now_add=True)
    cantidad_titulares = models.PositiveIntegerField(verbose_name="Cantidad de titulares")
    cantidad_suplentes = models.PositiveIntegerField(verbose_name="Cantidad de suplentes")
    ACTIVO = "A"
    INACTIVO = "I"
    FINALIZADO = "F"
    ESTADO_ACTIVIDAD_OPCIONES = (
        (ACTIVO, 'Activo'),
        (INACTIVO, 'Inactivo'),
        (FINALIZADO, 'Finalizado')
    )
    estado = models.CharField(max_length=1, choices=ESTADO_ACTIVIDAD_OPCIONES)
    responsable = models.ForeignKey(User)


class Inscripcion(models.Model):
    actividad = models.ForeignKey(Actividad)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(verbose_name="Fecha de nacimiento")
    telefono = models.CharField(max_length=50, verbose_name="Teléfono")
    mail = models.EmailField()
    PENDIENTE = "P"
    CONFIRMADO = "C"
    INCOMPLETO = "I"
    CANCELADO = "X"
    ESTADO_INSCRIPCION_OPCIONES = (
        (PENDIENTE, 'Pendiente'),
        (CONFIRMADO, 'Confirmado'),
        (INCOMPLETO, 'Incompleto'),
        (CANCELADO, 'Cancelado')
    )
    estado = models.CharField(max_length=1, choices=ESTADO_INSCRIPCION_OPCIONES)
    posicion = models.PositiveIntegerField()
    observacion = models.TextField(blank=True, verbose_name="Observación")
    participo = models.BooleanField()
    saldo = models.IntegerField(default=0)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Actividades"


class TipoPago(models.Model):
    nombre = models.CharField(max_length=100)


class Pago(models.Model):
    monto = models.IntegerField()
    tipo = models.ForeignKey(TipoPago)
    fecha = models.DateField()







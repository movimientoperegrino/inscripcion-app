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

    def __unicode__(self):
        return self.nombre

class Actividad(models.Model):
    lugar = models.ForeignKey(Lugar)
    nombre = models.TextField(verbose_name="Nombre")
    descripcion = models.TextField(verbose_name="Descripción")
    costo = models.IntegerField()
    requisitos = models.TextField()
    fecha_inicio = models.DateTimeField(verbose_name="Fecha inicio")
    fecha_fin = models.DateTimeField(verbose_name="Fecha fin")
    fecha_activacion = models.DateTimeField(verbose_name="Fecha activacion")
    fecha_desactivacion = models.DateTimeField(verbose_name="Fecha cierre")
    fecha_creacion = models.DateTimeField(verbose_name="Fecha creacion", auto_now_add=True)
    cantidad_titulares = models.PositiveIntegerField(verbose_name="Cantidad de titulares")
    cantidad_suplentes = models.PositiveIntegerField(verbose_name="Cantidad de suplentes")
    activa = models.BooleanField(default=False)
    responsable = models.ForeignKey(User)

    def __unicode__(self):
        return self.descripcion

class InscripcionEstado(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre

class Inscripcion(models.Model):
    actividad = models.ForeignKey(Actividad)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(verbose_name="Fecha de nacimiento")
    telefono = models.CharField(max_length=50, verbose_name="Teléfono")
    mail = models.EmailField()
    cedula = models.PositiveIntegerField(verbose_name="Cédula")
    estado_inscripcion = models.ForeignKey(InscripcionEstado)
    posicion = models.PositiveIntegerField()
    observacion = models.TextField(blank=True, verbose_name="Observación")
    participo = models.BooleanField(default=False)
    saldo = models.IntegerField(default=0)


class TipoPago(models.Model):
    nombre = models.CharField(max_length=100)


class Pago(models.Model):
    monto = models.IntegerField()
    tipo = models.ForeignKey(TipoPago)
    fecha = models.DateField()


class InscripcionEstadoFlujo(models.Model):
    estado_inicio = models.ForeignKey(InscripcionEstado, related_name='inicio')
    estado_final = models.ForeignKey(InscripcionEstado, related_name='fin')
    descripcion = models.CharField(max_length=100)

    def __unicode__(self):
        return self.estado_inicio.nombre + ' > ' + self.estado_final.nombre


class Parametro(models.Model):
    clave = models.PositiveIntegerField()
    valor = models.TextField()
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)





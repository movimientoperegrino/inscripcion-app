from django.contrib import admin

# Register your models here.
from mp.apps.inscripcion.models import *


class ActividadEstadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')

class InscripcionEstadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')

class InscripcionEstadoFlujoAdmin(admin.ModelAdmin):
    list_display = ('id', 'estado_inicio', 'estado_final', 'descripcion')

class LugarAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

class ActividadAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion', 'fecha_inicio', 'fecha_fin', 'fecha_creacion')

class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('id', 'actividad', 'nombre', 'apellido', 'fecha_nacimiento', 'mail')


admin.site.register(ActividadEstado, ActividadEstadoAdmin)
admin.site.register(Actividad, ActividadAdmin)
admin.site.register(Inscripcion, InscripcionAdmin)
admin.site.register(InscripcionEstado, InscripcionEstadoAdmin)
admin.site.register(InscripcionEstadoFlujo, InscripcionEstadoFlujoAdmin)
admin.site.register(Lugar, LugarAdmin)
admin.site.register(Pago)
admin.site.register(TipoPago)




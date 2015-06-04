# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inscripcion', '0002_actividadestado_mostrar_vista'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actividad',
            name='estado_actividad',
        ),
        migrations.AddField(
            model_name='actividad',
            name='activa',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='ActividadEstado',
        ),
    ]

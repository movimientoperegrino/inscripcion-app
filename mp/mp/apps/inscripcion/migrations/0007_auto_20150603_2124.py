# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inscripcion', '0006_auto_20150603_2118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inscripcionestado',
            name='inicial',
        ),
        migrations.AddField(
            model_name='actividad',
            name='nombre',
            field=models.TextField(default='actividad', verbose_name=b'Nombre'),
            preserve_default=False,
        ),
    ]

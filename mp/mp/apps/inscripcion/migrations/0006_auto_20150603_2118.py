# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inscripcion', '0005_parametro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inscripcionestadoflujo',
            name='es_raiz',
        ),
        migrations.AddField(
            model_name='inscripcion',
            name='cedula',
            field=models.PositiveIntegerField(default=0, verbose_name=b'C\xc3\xa9dula'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inscripcionestado',
            name='inicial',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]

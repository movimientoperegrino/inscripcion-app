# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('inscripcion', '0003_auto_20150501_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividad',
            name='fecha_desactivacion',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 4, 23, 29, 5, 552175, tzinfo=utc), verbose_name=b'Fecha cierre'),
            preserve_default=False,
        ),
    ]

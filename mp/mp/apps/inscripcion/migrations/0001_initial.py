# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.TextField(verbose_name=b'Descripci\xc3\xb3n')),
                ('costo', models.IntegerField()),
                ('requisitos', models.TextField()),
                ('fecha_inicio', models.DateTimeField(verbose_name=b'Fecha inicio')),
                ('fecha_fin', models.DateTimeField(verbose_name=b'Fecha fin')),
                ('fecha_activacion', models.DateTimeField(verbose_name=b'Fecha activacion')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name=b'Fecha creacion')),
                ('cantidad_titulares', models.PositiveIntegerField(verbose_name=b'Cantidad de titulares')),
                ('cantidad_suplentes', models.PositiveIntegerField(verbose_name=b'Cantidad de suplentes')),
                ('estado', models.CharField(max_length=1, choices=[(b'A', b'Activo'), (b'I', b'Inactivo'), (b'F', b'Finalizado')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField(verbose_name=b'Fecha de nacimiento')),
                ('telefono', models.CharField(max_length=50, verbose_name=b'Tel\xc3\xa9fono')),
                ('mail', models.EmailField(max_length=75)),
                ('estado', models.CharField(max_length=1, choices=[(b'P', b'Pendiente'), (b'C', b'Confirmado'), (b'I', b'Incompleto'), (b'X', b'Cancelado')])),
                ('posicion', models.PositiveIntegerField()),
                ('observacion', models.TextField(verbose_name=b'Observaci\xc3\xb3n', blank=True)),
                ('participo', models.BooleanField()),
                ('saldo', models.IntegerField(default=0)),
                ('actividad', models.ForeignKey(to='inscripcion.Actividad')),
            ],
            options={
                'verbose_name_plural': 'Actividades',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lugar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, verbose_name=b'Nombre')),
                ('direccion', models.TextField(verbose_name=b'Direcci\xc3\xb3n')),
                ('descripcion', models.TextField(verbose_name=b'Descripci\xc3\xb3n')),
                ('latitud', models.FloatField()),
                ('longitud', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('monto', models.IntegerField()),
                ('fecha', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoPago',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='pago',
            name='tipo',
            field=models.ForeignKey(to='inscripcion.TipoPago'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='actividad',
            name='lugar',
            field=models.ForeignKey(to='inscripcion.Lugar'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='actividad',
            name='responsable',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]

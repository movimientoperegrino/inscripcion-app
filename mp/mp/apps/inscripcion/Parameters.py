# -*- coding: utf-8 -*-
from enum import Enum

__author__ = 'gzacur'


# Se utiliza para realizar el mapeo de los parámetros del sistema con la base de datos.

class ParametrosInscripcion(Enum):
    MAIL_TEMPLATE_TITULAR = 1
    MAIL_TEMPLATE_SUPLENTE = 2
    INSCRIPCION_ESTADO_INICIAL = 3

__author__ = 'gzacur'


class CustomError(Exception):
    def __init__(self, arg):
        # Set some exception infomation
        self.msg = arg


class ActividadLlena(CustomError):
    """ Excepcion cuando la actividad ya se encuentra llena. """
    pass

class InscripcionRepetida(CustomError):
    """ Excepcion cuando se quiere repetir una inscripcion en una actividad. """
    pass

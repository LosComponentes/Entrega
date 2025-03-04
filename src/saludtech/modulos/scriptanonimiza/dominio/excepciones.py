"""
Excepciones del dominio de imágenes médicas

En este archivo usted encontrará las excepciones relacionadas
al dominio de imágenes médicas.
"""

from saludtech.seedwork.dominio.excepciones import ExcepcionFabrica


class TipoObjetoNoExisteEnDominioImagenesExcepcion(ExcepcionFabrica):
    """Excepción lanzada cuando se intenta crear un objeto que no existe en el dominio de imágenes médicas."""

    def __init__(self, mensaje="No existe una fábrica para el tipo solicitado en el módulo de imágenes médicas."):
        self.__mensaje = mensaje

    def __str__(self):
        return str(self.__mensaje)

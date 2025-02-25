""" Interfaces para los repositorios del dominio de mandejador de datos

En este archivo usted encontrará las diferentes interfaces para repositorios
del dominio de manejados de datos

"""

from abc import ABC
from saludtech.seedwork.dominio.repositorios import Repositorio

class RepositorioImagenes(Repositorio, ABC):
    ...
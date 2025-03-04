""" Fábricas para la creación de objetos en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos en la capa de infraestructura del dominio de vuelos

"""

from dataclasses import dataclass, field
from saludtech.seedwork.dominio.fabricas import Fabrica
from saludtech.seedwork.dominio.repositorios import Repositorio
from saludtech.modulos.anonimizacion.dominio.repositorios import RepositorioImagenesAnonimizadas
from .repositorios import RepositorioImagenesSQLite
from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj ==  RepositorioImagenesAnonimizadas.__class__:
            return RepositorioImagenesSQLite()
        else:
            raise ExcepcionFabrica()
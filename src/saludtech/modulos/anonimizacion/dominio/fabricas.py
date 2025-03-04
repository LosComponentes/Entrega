"""
Fábricas para la creación de objetos del dominio de imágenes médicas

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos del dominio de imágenes médicas.
"""

from saludtech.modulos.anonimizacion.dominio.excepciones import TipoObjetoNoExisteEnDominioImagenesAnonimizadasExcepcion
from .entidades import ImagenAnonimizada
from saludtech.seedwork.dominio.repositorios import Mapeador
from saludtech.seedwork.dominio.fabricas import Fabrica
from saludtech.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass


@dataclass
class _FabricaImagenAnomizada(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            imagen: ImagenAnonimizada = mapeador.dto_a_entidad(obj)
            return imagen


@dataclass
class FabricaImagenesAnonimizadas(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == ImagenAnonimizada.__class__:
            fabrica_imagen = _FabricaImagenAnomizada()
            return fabrica_imagen.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioImagenesAnonimizadasExcepcion()

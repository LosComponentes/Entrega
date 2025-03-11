"""
Fábricas para la creación de objetos del dominio de imágenes médicas

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos del dominio de imágenes médicas.
"""

from .entidades import Imagen
from .reglas import ImagenDebeTenerToken, ModalidadValida
from .excepciones import TipoObjetoNoExisteEnDominioImagenesExcepcion
from saludtech.seedwork.dominio.repositorios import Mapeador
from saludtech.seedwork.dominio.fabricas import Fabrica
from saludtech.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass


@dataclass
class _FabricaImagen(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        # print('_FabricaImagen')
        if isinstance(obj, Entidad):
            # print('isinstance')
            return mapeador.entidad_a_dto(obj)
        else:
            # print('Not isinstance')
            imagen: Imagen = mapeador.dto_a_entidad(obj)
            # print('dto_a_entidad finalizado')
            self.validar_regla(ImagenDebeTenerToken(imagen.token))
            # print('ImagenDebeTenerToken')
            self.validar_regla(ModalidadValida(imagen.modalidad))
            # print('ModalidadValida')
            return imagen


@dataclass
class FabricaImagenes(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        # print('crear_objeto')
        if mapeador.obtener_tipo() == Imagen.__class__:
            fabrica_imagen = _FabricaImagen()
            return fabrica_imagen.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioImagenesExcepcion()

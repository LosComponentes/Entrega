""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de vuelos

"""

from saludtech.config.db import db
from saludtech.modulos.anonimizacion.dominio.repositorios import RepositorioImagenesAnonimizadas
from saludtech.modulos.anonimizacion.dominio.entidades import ImagenAnonimizada
from saludtech.modulos.anonimizacion.dominio.fabricas import FabricaImagenesAnonimizadas
from .dto import ImagenAnomizada as ImagenAnonimizadaDTO
from .mapeadores import MapeadorImagen
from uuid import UUID


class RepositorioImagenesSQLite(RepositorioImagenesAnonimizadas):

    def __init__(self):
        self._fabrica_imagenes:  FabricaImagenesAnonimizadas = FabricaImagenesAnonimizadas()

    @property
    def fabrica_imagenes(self):
        return self._fabrica_imagenes

    def obtener_por_id(self, id: UUID) -> ImagenAnonimizada:
        imagen_dto = db.session.query(ImagenAnonimizadaDTO).filter_by(id=str(id)).first()

        print(imagen_dto)
        
        if imagen_dto is None:
            return '', 404

        return self.fabrica_iamagenes.crear_objeto(imagen_dto, MapeadorImagen())

    def agregar(self, imagen: ImagenAnonimizada):
        imagen_dto = self.fabrica_iamagenes.crear_objeto(imagen, MapeadorImagen())
        db.session.add(imagen_dto)
        db.session.commit()

    
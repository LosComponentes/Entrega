""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de vuelos

"""

from saludtech.config.db import db
from saludtech.modulos.manejador_datos.dominio.repositorios import RepositorioImagenes
from saludtech.modulos.manejador_datos.dominio.entidades import Imagen
from saludtech.modulos.manejador_datos.dominio.fabricas import FabricaImagenes
from .dto import Imagen as ImagenDTO
from .mapeadores import MapeadorImagen
from uuid import UUID


class RepositorioImagenesSQLite(RepositorioImagenes):

    def __init__(self):
        self._fabrica_imagenes: FabricaImagenes = FabricaImagenes()

    @property
    def fabrica_iamagenes(self):
        return self._fabrica_imagenes

    def obtener_por_id(self, id: UUID) -> Imagen:
        imagen_dto = db.session.query(ImagenDTO).filter_by(id=str(id)).first()

        print(imagen_dto)
        
        if imagen_dto is None:
            return '', 404

        return self.fabrica_iamagenes.crear_objeto(imagen_dto, MapeadorImagen())

    def obtener_todos(self) -> list[Imagen]:
        # TODO
        raise NotImplementedError

    def agregar(self, imagen: Imagen):
        imagen_dto = self.fabrica_iamagenes.crear_objeto(imagen, MapeadorImagen())
        db.session.add(imagen_dto)
        db.session.commit()

    def actualizar(self, reserva: Imagen):
        # TODO
        raise NotImplementedError

    def eliminar(self, reserva_id: UUID):
        # TODO
        raise NotImplementedError
from saludtech.seedwork.aplicacion.dto import Mapeador
from saludtech.seedwork.dominio.repositorios import Mapeador as MapRepo
from saludtech.modulos.metadatos.dominio.entidades import Imagen
from saludtech.modulos.metadatos.dominio.objetos_valor import Datos
from .dto import ImagenDTO, DatosDTO, SintomasDTO, CondicionesDTO

class MapeadorImagenDTOJson(Mapeador):
    def obtener_tipo(self) -> type:
        return Imagen.__class__
from saludtech.seedwork.aplicacion.dto import Mapeador as AppMap
from saludtech.seedwork.aplicacion.servicios import ServicioImagen
from saludtech.seedwork.dominio.repositorios import Mapeador as RepMap
from saludtech.modulos.manejador_datos.dominio.entidades import Imagen, Condicion, Metadata
from saludtech.modulos.manejador_datos.dominio.objetos_valor import Modalidad, RegionAnatomica, Token, TipoCondicion, EntornoClinico, ContextoProcesal, Sintoma
from .dto import ImagenDTO

from datetime import datetime

class MapeadorImagenDTOJson(AppMap):
    def _procesar_imagen(self, imagen: dict) -> ImagenDTO:
        ...

class MapeadorImagen(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def entidad_a_dto(self, entidad: Imagen) -> ImagenDTO:
        fecha_creacion = entidad.fecha_creacion.strftime(self._FORMATO_FECHA)
        fecha_adquisicion = entidad.fecha_adquisicion.fecha_adquisicion.strftime(self._FORMATO_FECHA)
        _id = str(entidad.id)
        
        return ImagenDTO(fecha_creacion, fecha_adquisicion, _id, itinerarios)

    def dto_a_entidad(self, dto: ImagenDTO) -> Imagen:
        imagen = Imagen()
        imagen.condiciones = list()

        condiciones_dto: list[CondicioneDTO] = dto.condiciones

        for cond in condiciones_dto:
            imagen.condiciones.append(self._procesar_condicion(cond))
        
        return condicion


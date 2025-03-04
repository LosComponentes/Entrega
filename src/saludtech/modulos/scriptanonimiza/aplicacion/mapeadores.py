from saludtech.seedwork.aplicacion.dto import Mapeador as AppMap
from saludtech.seedwork.dominio.repositorios import Mapeador as RepMap
from saludtech.modulos.manejador_datos.dominio.entidades import Imagen, Condicion, Metadata
from saludtech.modulos.manejador_datos.dominio.objetos_valor import Modalidad, RegionAnatomica, Token, TipoCondicion, EntornoClinico, ContextoProcesal, Sintoma
from .dto import ImagenDTO,CondicionDTO, MetadatoDTO, TipoCondicionDTO

from datetime import datetime

class MapeadorImagenDTOJson(AppMap):
    def _procesar_imagen(self, imagen: dict) -> ImagenDTO:
        imagen_dto: ImagenDTO
        imagen_dto.modalidad = imagen.get('modalidad')

        condiciones_dto: list[CondicionDTO] = list()
        for condicion in imagen.condiciones:
            condiciones_dto.append(condicion.get('tipo_condicion'))
        
        imagen_dto.condiciones = condiciones_dto

        metadata_dto: MetadatoDTO = list()
        for metadato in imagen.Metadata:
            metadata_dto.entorno_clinico = metadato.get('entorno_clinico')
            metadata_dto.entorno_clinico = metadato.get('contexto_procesal')
            
            sintomas_dto: TipoCondicionDTO = list()
            for sintoma in metadato.sintomas:
                sintomas_dto.append(sintoma.get('tipo_condicion'))
            
            metadata_dto.sintomas.append(sintomas_dto)

        imagen_dto.metadata = metadata_dto
        return imagen_dto

    def externo_a_dto(self, externo: dict) -> ImagenDTO:
        imagen_dto = ImagenDTO()
        imagen_dto = self._procesar_itinerario(externo)
        return imagen_dto

    def dto_a_externo(self, dto: ImagenDTO) -> dict:
        return dto.__dict__

class MapeadorImagen(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'


    def _procesar_imagen(self, imagen_dto: ImagenDTO) -> Imagen:
        imagen: Imagen
        imagen.modalidad = imagen_dto.modalidad

        condiciones = list()
        for condicion in condiciones_dto.condiciones:
            condiciones.append(condicion.tipo_condicion)
        
        imagen.condiciones = condiciones

        metadata = list()
        for metadato_dto in imagen_dto.metadata:
            metadata.entorno_clinico = metadato_dto.entorno_clinico
            metadata.entorno_clinico = metadato_dto.contexto_procesal
            
            sintomas = list()
            for sintoma_dto in metadato_dto.sintomas:
                sintomas.append(sintoma_dto.tipo_condicion)
            
            metadata.sintomas.append(sintomas)

        imagen.metadata = metadata
        return imagen

    def entidad_a_dto(self, entidad: Imagen) -> ImagenDTO:
        fecha_creacion = entidad.fecha_creacion.strftime(self._FORMATO_FECHA)
        fecha_actualizacion = entidad.fecha_adquisicion.fecha_adquisicion.strftime(self._FORMATO_FECHA)
        _id = str(entidad.id)
        modalidad = str(entidad.modalidad)
        region_anatomica = str(entidad.region_anatomica)
        metadata= Metadata()
        return ImagenDTO(_id,fecha_creacion, fecha_actualizacion, modalidad,region_anatomica,"",list(),metadata)

    def dto_a_entidad(self, dto: ImagenDTO) -> Imagen:
        imagen = Imagen()
        imagen = self._procesar_condicion(dto)
        
        return imagen


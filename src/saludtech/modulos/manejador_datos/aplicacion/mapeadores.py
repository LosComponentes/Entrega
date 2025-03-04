from saludtech.seedwork.aplicacion.dto import Mapeador as AppMap
from saludtech.seedwork.dominio.repositorios import Mapeador as RepMap
from saludtech.modulos.manejador_datos.dominio.entidades import Imagen, Condicion, Metadata
from saludtech.modulos.manejador_datos.dominio.objetos_valor import Modalidad, RegionAnatomica, Token, TipoCondicion, EntornoClinico, ContextoProcesal, Sintoma
from .dto import ImagenDTO,CondicionDTO, MetadatoDTO, TipoCondicionDTO

from datetime import datetime

class MapeadorImagenDTOJson(AppMap):
    def _procesar_imagen(self, imagen: dict) -> ImagenDTO:
        print('_procesar_imagen')
        
        # Procesar condiciones correctamente
        condiciones_dto = [
            TipoCondicionDTO(tipo_condicion=condicion.get("tipo_condicion", ""))
            for condicion in imagen.get("condiciones", [])
        ]
        print('condiciones_dto')

        metadato = imagen.get("metadata",MetadatoDTO("", "", []))

        # Procesar sintomas correctamente
        sintomas_dto = [
            TipoCondicionDTO(tipo_condicion=condicion.get("tipo_condicion", ""))
            for condicion in imagen.get("sintomas", [])
        ]
        print('sintomas_dto')

        metadata_dto = MetadatoDTO (entorno_clinico=metadato.get("entorno_clinico",""),
                                  contexto_procesal=metadato.get("contexto_procesal",""),
                                  sintomas=sintomas_dto) 
            

        print('metadata_dto')

        # Se inicializa el objeto DTO antes de asignar valores
        imagen_dto = ImagenDTO(
            id=imagen.get("id", ""),
            fecha_creacion=imagen.get("fecha_creacion", ""),
            fecha_actualizacion=imagen.get("fecha_actualizacion", ""),
            modalidad=imagen.get("modalidad", ""),
            region_anatomica=imagen.get("region_anatomica", ""),
            token=imagen.get("token", ""),
            condiciones=condiciones_dto,
            metadata=metadata_dto
        )

        # imagen_dto.metadata = metadata_dto
        return imagen_dto

    def externo_a_dto(self, externo: dict) -> ImagenDTO:
        imagen_dto = ImagenDTO()
        imagen_dto = self._procesar_imagen(externo)
        return imagen_dto

    def dto_a_externo(self, dto: ImagenDTO) -> dict:
        return dto.__dict__

class MapeadorImagen(RepMap):
    _FORMATO_FECHA = "%Y-%m-%dT%H:%M:%SZ"

    def obtener_tipo(self) -> type:
        return Imagen.__class__

    def _procesar_imagen(self, imagen_dto: ImagenDTO) -> Imagen:
        imagen: Imagen()
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


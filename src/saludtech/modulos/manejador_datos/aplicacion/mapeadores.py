from saludtech.seedwork.aplicacion.dto import Mapeador as AppMap
from saludtech.seedwork.dominio.repositorios import Mapeador as RepMap
from saludtech.modulos.manejador_datos.dominio.entidades import Imagen, Condicion, Metadata
from saludtech.modulos.manejador_datos.dominio.objetos_valor import Modalidad, RegionAnatomica, Token, TipoCondicion, EntornoClinico, ContextoProcesal, Sintoma
from .dto import ImagenDTO,CondicionDTO, MetadatoDTO, TipoCondicionDTO,ModalidadDTO,RegionAnatomicaDTO,TokenDTO
from datetime import datetime
import uuid

class MapeadorImagenDTOJson(AppMap):
    def _procesar_imagen(self, imagen: dict) -> ImagenDTO:
        # print('_procesar_imagen')
        
        # Procesar condiciones correctamente
        condiciones_dto = [
            TipoCondicionDTO(tipo_condicion=condicion.get("tipo_condicion", ""))
            for condicion in imagen.get("condiciones", [])
        ]
        # print('condiciones_dto')

        metadato = imagen.get("metadata",MetadatoDTO("", "", []))

        # Procesar sintomas correctamente
        sintomas_dto = [
            TipoCondicionDTO(tipo_condicion=condicion.get("tipo_condicion", ""))
            for condicion in imagen.get("sintomas", [])
        ]
        # print('sintomas_dto')

        metadata_dto = MetadatoDTO (entorno_clinico=metadato.get("entorno_clinico",""),
                                  contexto_procesal=metadato.get("contexto_procesal",""),
                                  sintomas=sintomas_dto) 
            

        # print('metadata_dto')

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
        # print('dto_a_externo')
        # print(dto)
        try:
            return dto.__dict__
        except:
            return dto

class MapeadorImagen(RepMap):
    _FORMATO_FECHA = "%Y-%m-%dT%H:%M:%SZ"

    def obtener_tipo(self) -> type:
        return Imagen.__class__

    def _procesar_imagen(self, imagen_dto: ImagenDTO) -> Imagen:
        # print('_procesar_imagen')
        modalidad_dto : ModalidadDTO = ModalidadDTO(imagen_dto.modalidad)
        region_dto : RegionAnatomicaDTO = RegionAnatomicaDTO(imagen_dto.region_anatomica)

        condiciones : list[TipoCondicionDTO] = list()
        for condicion in imagen_dto.condiciones:
            # print(condicion)
            # print(condicion.tipo_condicion)
            tipo_condicion : TipoCondicionDTO = TipoCondicionDTO(condicion.tipo_condicion)
            condiciones.append(tipo_condicion)

        sintomas : list[TipoCondicionDTO] = list()
        for sintoma_dto in imagen_dto.metadata.sintomas:
            tipo_condicion : TipoCondicionDTO = TipoCondicionDTO(sintoma_dto.tipo_condicion)
            sintomas.append(tipo_condicion)

        metadata_dto: MetadatoDTO = MetadatoDTO(imagen_dto.metadata.entorno_clinico,
        imagen_dto.metadata.contexto_procesal, sintomas)

        token_dto : TokenDTO = TokenDTO(str(uuid.uuid4()))

        imagen: Imagen = Imagen(modalidad=modalidad_dto,
                                region_anatomica=region_dto,
                                condiciones=condiciones,
                                metadata=metadata_dto,
                                token=token_dto)
        # print('imagen procesada')
        return imagen

    def entidad_a_dto(self, entidad: Imagen) -> ImagenDTO:
        # print('aplicacion.mapeadores.entidad_a_dto')
        fecha_creacion = entidad.fecha_creacion.strftime(self._FORMATO_FECHA)
        fecha_actualizacion = entidad.fecha_actualizacion.strftime(self._FORMATO_FECHA)
        _id = str(entidad.id)
        modalidad = str(entidad.modalidad.tipo)
        region_anatomica = str(entidad.region_anatomica.parteCuerpo)
        token = entidad.token.valor
        metadata= Metadata(entorno_clinico=entidad.metadata.entorno_clinico,
                            contexto_procesal= entidad.metadata.contexto_procesal,
                            sintomas=[] )
        # print('aplicacion.mapeadores.entidad_a_dto.ImagenDTO')
        return ImagenDTO(_id,fecha_creacion, fecha_actualizacion, modalidad,region_anatomica,token,list(),metadata)

    def dto_a_entidad(self, dto: ImagenDTO) -> Imagen:
        # print('dto_a_entidad')
        imagen : Imagen = self._procesar_imagen(dto)
        # print('imagen procesada2')
        return imagen


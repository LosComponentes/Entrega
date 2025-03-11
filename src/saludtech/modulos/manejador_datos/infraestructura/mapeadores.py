""" Mapeadores para la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from saludtech.seedwork.dominio.repositorios import Mapeador
from saludtech.modulos.manejador_datos.dominio.objetos_valor import Modalidad,RegionAnatomica,Token,TipoCondicion,EntornoClinico,ContextoProcesal,Sintoma,ModalidadImagen,RegionCuerpo
from saludtech.modulos.manejador_datos.dominio.entidades import Imagen,Condicion,Metadata
from .dto import Imagen as ImagenDTO
from saludtech.modulos.manejador_datos.aplicacion.dto import CondicionDTO, MetadatoDTO, TipoCondicionDTO,ModalidadDTO,RegionAnatomicaDTO,TokenDTO

class MapeadorImagen(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def _procesar_imagen_dto(self, imagen_dto: list) -> list[Imagen]:  
        objs_imagenes: list()

        for imagen in imagen_dto:
           obj_imagen: Imagen = self._procesar_imagen(imagen) 
           objs_imagenes.append(obj_imagen)
        #     obj_imagen.token = imagen.token
        #     obj_imagen.modalidad = imagen.modalidad
        #     obj_imagen.region_anatomica = imagen.region_anatomica
            
        #     obj_imagen.condiciones = list()
        #     for condicion in imagen.condiciones:
        #         obj_imagen.condiciones.append(condicion.tipo_condicion)

        #     obj_imagen.metadata = {}
        #     obj_imagen.metadata.entorno_clinico = imagen.metadata.entorno_clinico
        #     obj_imagen.metadata.contexto_procesal = imagen.metadata.contexto_procesal

        #     obj_imagen.metadata.sintomas = list()
        #     for sintoma in imagen.metadata.sintomas:
        #         obj_imagen.metadata.sintomas.append(sintoma)

        return objs_imagenes

    def _procesar_imagen(self, imagen: any) -> ImagenDTO:
        imagen_dto = ImagenDTO()
        obj_imagen.token = imagen.token
        imagen_dto.modalidad = imagen.modalidad
        imagen_dto.region_anatomica = imagen.region_anatomica
        
        imagen_dto.condiciones = list()
        imagen_dto.condiciones = self._procesar_condiciones(imagen.condiciones)
        
        # for condicion in imagen.condiciones:
        #     imagen_dto.condiciones.append(condicion.tipo_condicion)

        imagen_dto.metadata = {}
        imagen_dto.metadata.entorno_clinico = imagen.metadata.entorno_clinico
        imagen_dto.metadata.contexto_procesal = imagen.metadata.contexto_procesal

        imagen_dto.metadata.sintomas = list()
        for sintoma in imagen.metadata.sintomas:
            imagen_dto.metadata.sintomas.append(sintoma)

        return imagen_dto

    def _procesar_condiciones(self, condiciones: any) -> list[Condicion]:
        condiciones_dto = list()
        
        for condicion in condiciones:
            condiciones_dto.append(condicion)

        return condiciones_dto


    def obtener_tipo(self) -> type:
        return Imagen.__class__

    def entidad_a_dto(self, entidad: Imagen) -> ImagenDTO:
        print('infraestructura.mapeadores.entidad_a_dto')
        
        condiciones_dto : str = ""
        for condicion in entidad.condiciones:
            condiciones_dto += condicion.tipo_condicion

        imagen_dto = ImagenDTO(fecha_creacion=entidad.fecha_creacion,
                            fecha_actualizacion=entidad.fecha_actualizacion,
                            id=str(entidad.id),
                            modalidad=entidad.modalidad.tipo,
                            region_anatomica=entidad.region_anatomica.parteCuerpo,
                            token=entidad.token.valor,
                            condiciones=condiciones_dto,
                            metadata=entidad.metadata)

        # imagen_dto.fecha_creacion = str(entidad.fecha_creacion)
        # imagen_dto.fecha_actualizacion = str(entidad.fecha_actualizacion)
        # imagen_dto.id = str(entidad.id)
        print('datos basicos')

        # imagen_dto.modalidad = entidad.modalidad.tipo
        # imagen_dto.region_anatomica = entidad.region_anatomica.parteCuerpo
        # imagen_dto.token = entidad.token.valor

        print('condiciones')
        # print(entidad.condiciones)

        # print(condiciones_dto)
        # imagen_dto.condiciones = condiciones_dto
        print('condiciones ok')
        return imagen_dto

    def dto_a_entidad(self, dto: ImagenDTO) -> Imagen:
        print('infraestructura.mapeadores.dto_a_entidad')
        # region_anatomica_dto : RegionAnatomicaDTO = RegionAnatomicaDTO(dto.region_anatomica)
        # imagen.region_anatomica = region_anatomica_dto

        # token_dto: TokenDTO = TokenDTO(dto.token)
        condiciones_dto = list()
        imagen = Imagen(id=dto.id,
                        fecha_creacion=dto.fecha_creacion,
                        fecha_actualizacion= dto.fecha_actualizacion,
                        condiciones=self._procesar_condiciones(condiciones_dto),
                        modalidad=ModalidadDTO(dto.modalidad),
                        region_anatomica=RegionAnatomicaDTO(dto.region_anatomica),
                        token=TokenDTO(dto.token),
                        metadata=MetadatoDTO("",
                                            "",
                                            []))

        print(imagen)
        return imagen
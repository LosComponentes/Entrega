""" Mapeadores para la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from saludtech.seedwork.dominio.repositorios import Mapeador
from saludtech.modulos.manejador_datos.dominio.objetos_valor import Modalidad,RegionAnatomica,Token,TipoCondicion,EntornoClinico,ContextoProcesal,Sintoma,ModalidadImagen,RegionCuerpo
from saludtech.modulos.manejador_datos.dominio.entidades import Imagen,Condicion,Metadata
from .dto import Imagen as ImagenDTO
from .dto import Condicion as CondicionDTO

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
        
        imagen_dto = ImagenDTO()
        imagen_dto.fecha_creacion = entidad.fecha_creacion
        imagen_dto.fecha_actualizacion = entidad.fecha_actualizacion
        imagen_dto.id = str(entidad.id)

        condiciones_dto = list()
        
        for condicion in entidad.condiciones:
            condiciones_dto.extend(self._procesar_condiciones(condicion))

        imagen_dto.condiciones = condiciones_dto

        return imagen_dto

    def dto_a_entidad(self, dto: ImagenDTO) -> Imagen:
        imagen = Imagen(dto.id, dto.fecha_creacion, dto.fecha_actualizacion)
        imagen.condiciones = list()

        condiciones_dto: list[CondicionDTO] = dto.condiciones

        imagen.condiciones.extend(self._procesar_condiciones(condiciones_dto))
        
        return imagen
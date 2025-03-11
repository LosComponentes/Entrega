import strawberry
import typing

from strawberry.types import Info
from bff_web import utils
from bff_web.despachadores import Despachador

from .esquemas import *

@strawberry.type
class Mutation:

    @strawberry.mutation
    async def crear_imagen(self, token: uuid, modalidad: str, condiciones: list, metadata: list ) -> ImagenRespuesta:
        payload = dict(
            token = token,
            modalidad = modalidad,
            condiciones = condiciones,
            metadata = metadata,
        )
        comando = dict(
            id = str(uuid.uuid4()),
            time=utils.time_millis(),
            specversion = "v1",
            type = "ComandoImagen",
            ingestion=utils.time_millis(),
            datacontenttype="AVRO",
            service_name = "BFF Web",
            data = payload
        )
        despachador = Despachador()
        info.context["background_tasks"].add_task(despachador.publicar_mensaje, comando, "comando-crear-imagen", "public/default/comando-crear-imagen")
        
        return ReservaRespuesta(mensaje="Procesando Mensaje", codigo=203)
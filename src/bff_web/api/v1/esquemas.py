import typing
import strawberry
import uuid
import requests
import os

from datetime import datetime


AEROALPES_HOST = os.getenv("SALUDTECH_ADDRESS", default="localhost")
FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

def obtener_imagenes(root) -> typing.List["Imagen"]:
    imagenes_json = requests.get(f'http://{AEROALPES_HOST}:5000/manejador_datos/imagen').json()
    imagenes = []

    for imagen in imagenes_json:
        imagenes.append(
            Imagen(
                id=imagen.get('id'), 
                token=imagen.get('token'), 
                modalidad=imagen.get('modalidad'), 
                condiciones=imagen.get('condiciones'),
                metadata=imagen.get('metadata')
            )
        )

    return reservas

@strawberry.type
class Condicion:
    tipo_condicion: str

@strawberry.type
class Sintoma:
    tipo_condicion: str

@strawberry.type
class Metadata:
    entorno_clinico: str
    contexto_procesal: str
    sintomas: typing.List[Sintoma]

@strawberry.type
class Imagen:
    id: str
    token: uuid
    modalidad: str
    condiciones: typing.List[Condicion]
    metadata: typing.List[Metadata]

    
@strawberry.type
class ImagenRespuesta:
    mensaje: str
    codigo: int







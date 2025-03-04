from pulsar.schema import *
from saludtech.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class ImagenAnonimizadaPayload(Record):
    id_imagen = String()
    token = String()
    fecha_creacion = Long()
    fecha_adquisicion = Long()

class EventoImagenAnonimizadaCreada(EventoIntegracion):
    data = ImagenAnonimizadaPayload()
    
    
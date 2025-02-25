from pulsar.schema import *
from saludtech.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class ImagenCreadaPayload(Record):
    id_imagen = String()
    token = String()
    region_anatomica = String()
    fecha_creacion = Long()
    fecha_adquisicion = Long()

class EventoImagenCreada(EventoIntegracion):
    data = ImagenCreadaPayload()
import pulsar
from pulsar.schema import *

from saludtech.modulos.manejador_datos.infraestructura.schema.v1.eventos import EventoImagenCreada, ImagenCreadaPayload
from saludtech.modulos.manejador_datos.infraestructura.schema.v1.comandos import ComandoCrearImagen, ComandoCrearImagenPayload
from saludtech.seedwork.infraestructura import utils

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(EventoImagenCreada))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del evento
        payload = ImagenCreadaPayload(
            id_imagen=str(evento.id_imagen), 
            token=str(evento.token), 
            region_anatomica=str(evento.region_anatomica), 
            fecha_creacion=int(unix_time_millis(evento.fecha_creacion)),
            fecha_adquisicion=int(unix_time_millis(evento.fecha_adquisicion))
        )
        evento_integracion = EventoImagenCreada(data=payload)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoImagenCreada))

    def publicar_comando(self, comando, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando
        payload = ComandoCrearImagenPayload(
            id_usuario=str(comando.id_usuario)
            # agregar itinerarios
        )
        comando_integracion = ComandoCrearImagen(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoCrearImagen))

import pulsar
from pulsar.schema import *

from saludtech.modulos.anonimizacion.infraestructura.schema.v1.eventos import EventoImagenAnonimizadaCreada, EventoImagenAnonimizadaCreadaPayload
from saludtech.modulos.anonimizacion.infraestructura.schema.v1.comandos import ComandoCrearImagenAnonimizada, ComandoCrearImagenAnonimizadaPayload
from saludtech.seedwork.infraestructura import utils

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(EventoImagenAnonimizadaCreada))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        payload = EventoImagenAnonimizadaCreadaPayload(
            id_imagen=str(evento.id_imagen), 
            token=str(evento.token), 
            tipo_anonimizacion=str(evento.tipo_anonimizacion),
            fecha_creacion=int(unix_time_millis(evento.fecha_creacion)),
            fecha_adquisicion=int(unix_time_millis(evento.fecha_adquisicion))
        )
        evento_integracion = EventoImagenAnonimizadaCreada(data=payload)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoImagenAnonimizadaCreada))

    def publicar_comando(self, comando, topico):
        payload = ComandoCrearImagenAnonimizada(
            id_usuario=str(comando.id_usuario)
        )
        comando_integracion = ComandoCrearImagenAnonimizadaPayload(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoCrearImagenAnonimizada))

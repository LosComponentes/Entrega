from pulsar.schema import *
from dataclasses import dataclass, field
from saludtech.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoCrearImagenAnonimizadaPayload(ComandoIntegracion):
    id_usuario = String()
    # TODO Cree los records para itinerarios

class ComandoCrearImagenAnonimizada(ComandoIntegracion):
    data = ComandoCrearImagenAnonimizadaPayload()
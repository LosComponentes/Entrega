from __future__ import annotations
from dataclasses import dataclass, field

import saludtech.modulos.manejador_datos.dominio.objetos_valor as ov
from saludtech.seedwork.dominio.entidades import AgregacionRaiz, Entidad
from saludtech.modulos.manejador_datos.dominio.eventos import ImagenCreada

@dataclass
class Condicion(Entidad):
    tipo_condicion: list[ov.TipoCondicion] = field(default_factory=list[ov.TipoCondicion])

@dataclass
class Metadata(Entidad):
    entorno_clinico: ov.EntornoClinico = field(default_factory=ov.EntornoClinico)
    contexto_procesal: ov.ContextoProcesal = field(default_factory=ov.ContextoProcesal)
    sintomas: list[ov.Sintoma] = field(default_factory=list[ov.Sintoma])

@dataclass
class Imagen(AgregacionRaiz):
    modalidad: ov.Modalidad = field(default_factory=ov.Modalidad)
    region_anatomica: ov.RegionAnatomica = field(default_factory=ov.RegionAnatomica)
    token: ov.Token = field(default_factory=ov.Token)
    condiciones: list[Condicion] = field(default_factory=list[Condicion])
    metadata: Metadata = field(default_factory=Metadata)

    def __str__(self) -> str:
        return f"Imagen {self.token}" 

    def crear_imagen(self, imagen: Imagen) -> dict:  
        self.token = imagen.token
        self.modalidad  = imagen.modalidad
        self.region_anatomica = imagen.region_anatomica
        self.condiciones = imagen.condiciones
        self.metadata = imagen.metadata

        self.agregar_evento(ImagenCreada(id_imagen=self.id, token=self.token, region_anatomica=self.estado.region_anatomica, fecha_creacion=self.fecha_creacion, fecha_adquisicion=self.fecha_adquisicion))



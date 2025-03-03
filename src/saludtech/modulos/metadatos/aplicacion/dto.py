# Imagen: token, modalidad, region
## Sintomas: list
#condiciones: list
#datos: entorno clinico, contexto

from dataclasses import dataclass, field
from saludtech.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class SintomasDTO(DTO):
    sintoma: str

@dataclass(frozen=True)
class CondicionesDTO(DTO):
    condicion: str

@dataclass(frozen=True)
class ImagenDTO(DTO):
    id: str = field(default_factory=str)
    token: str
    modalidad: str
    region: str
    condiciones: list[CondicionesDTO]
    sintomas: list[SintomasDTO]


@dataclass(frozen=True)
class DatosDTO(DTO):
    entorno_clinico: str
    contexto: str
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
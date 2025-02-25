from dataclasses import dataclass, field
from saludtech.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class ImagenDTO(DTO):
    id: str = field(default_factory=str)
    fecha_creacion: str = field(default_factory=str)
    fecha_adquisicion: str = field(default_factory=str)

@dataclass(frozen=True)
class CondicionDTO(DTO):
    tipos: list[TipoDTO]

@dataclass(frozen=True)
class TipoDTO(DTO):
    tipo: str



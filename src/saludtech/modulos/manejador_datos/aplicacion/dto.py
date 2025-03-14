from dataclasses import dataclass, field
from saludtech.seedwork.aplicacion.dto import DTO
import uuid

@dataclass(frozen=True)
class TipoDTO(DTO):
    tipo: str

@dataclass(frozen=True)
class ModalidadDTO(DTO):
    tipo: str

@dataclass(frozen=True)
class TokenDTO(DTO):
    valor: str

@dataclass(frozen=True)
class RegionAnatomicaDTO(DTO):
    parteCuerpo: str

@dataclass(frozen=True)
class TipoCondicionDTO(DTO):
    tipo_condicion: str

@dataclass(frozen=True)
class CondicionDTO(DTO):
    tipos: list[TipoDTO]

@dataclass(frozen=True)
class MetadatoDTO(DTO):
    entorno_clinico: str
    contexto_procesal: str
    sintomas: list[TipoCondicionDTO]

@dataclass(frozen=True)
class ImagenDTO(DTO):
    id: str = field(default_factory=str)
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
    modalidad: str = field(default_factory=str)
    region_anatomica: str = field(default_factory=str)
    token: str = field(default_factory=str)
    condiciones: list[TipoCondicionDTO] = field(default_factory=list)
    metadata: MetadatoDTO = field(default_factory=lambda: MetadatoDTO("", "", []))  # Corregido
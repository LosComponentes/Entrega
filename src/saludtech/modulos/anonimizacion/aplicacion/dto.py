from dataclasses import dataclass, field
from saludtech.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class ImagenAnonimizadaDTO(DTO):
    id: str = field(default_factory=str)
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
    modalidad: str = field(default_factory=str)
    region_anatomica: str = field(default_factory=str)
    token: str = field(default_factory=str)
    condiciones: list[str] = field(default_factory=list)
    metadata: str = field(default_factory=str)
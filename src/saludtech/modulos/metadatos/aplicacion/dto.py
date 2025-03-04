from dataclasses import dataclass, field
from saludtech.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class CondicionesDTO(DTO):
    tipoDeCondicion: str

@dataclass(frozen=True)
class SintomasDTO(DTO):
    tipoDeCondicion: list[CondicionesDTO]

@dataclass(frozen=True)
class entornoClinicoDTO(DTO):
    entornoClinico: str
    fecha_ingreso: str = field(default_factory=str)


@dataclass(frozen=True)
class ContextoProcesamientoDTO(DTO):
    contexto: str
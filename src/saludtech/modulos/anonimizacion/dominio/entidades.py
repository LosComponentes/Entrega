from __future__ import annotations
from dataclasses import dataclass, field

from saludtech.seedwork.dominio.entidades import Entidad
import saludtech.modulos.anonimizacion.dominio.objetos_valor as ov

@dataclass
class ImagenAnonimizada(Entidad):
    tipo_anonimizacion: str = field(default_factory=ov.TipoAnonimizacion)
    token: str = field(default_factory=str)
    modalidad: str = field(default_factory=str)
    region_anatomica: str = field(default_factory=str)
    condiciones: list[str] = field(default_factory=list[str])
    metadata: str = field(default_factory=str)
    
    def __str__(self) -> str:
        return f"Imagen Anonimizada {self.token}"
    
    
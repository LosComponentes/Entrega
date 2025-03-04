from __future__ import annotations
from dataclasses import dataclass, field
from saludtech.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

@dataclass
class ImagenCreada(EventoDominio):
    id_imagen: uuid.UUID = None
    token: str  = None
    region_anatomica: str  = None
    fecha_creacion: datetime = None
    fecha_adquisicion: datetime = None

from __future__ import annotations
from dataclasses import dataclass, field
from saludtech.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

class ImagenAnomizada(EventoDominio):
    tipo_anonimizacion: str = None
    token: str  = None
    fecha_creacion: datetime = None
    fecha_adquisicion: datetime = None
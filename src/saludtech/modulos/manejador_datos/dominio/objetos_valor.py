"""Objetos valor del dominio de imágenes

En este archivo encontrará los objetos valor del dominio de imágenes, basados en la agregación raíz Imagen.

"""

from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum

@dataclass(frozen=True)
class Modalidad:
    tipo: str

@dataclass(frozen=True)
class RegionAnatomica:
    parteCuerpo: str  

@dataclass(frozen=True)
class Token:
    valor: str

@dataclass(frozen=True)
class TipoCondicion:
    tipo: str  

@dataclass(frozen=True)
class EntornoClinico:
    descripcion: str 

@dataclass(frozen=True)
class ContextoProcesal:
    descripcion: str  

@dataclass(frozen=True)
class Sintoma:
    descripcion: str  

class ModalidadImagen(Enum):
    RX = "Rayos X"
    TOMOGRAFIA = "Tomografía"
    RM = "Resonancia Magnética"
    ECOGRAFIA = "Ecografía"
    ULTRA_SONIDO = "Ultra Sonido"
    MAMOGRAFIA= "Mamografía"
    ESCANEO_TEP = "Escaneo TEP"
    HISPATOLOGIA = "Hispatología"
    OTROS = "OTROS"

class RegionCuerpo(Enum):
    CABEZA_CUELLO = "Cabeza y Cuello"
    TORAX = "Toráx"
    ABDOMEN = "Abadomen"
    MUSCULOESQUELETICO= "Musculoesquelético"
    PELVIS = "Pelvis"
    CUERPO_COMPLETO = "Cuerpo completo"

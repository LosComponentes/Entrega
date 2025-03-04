from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum

class Tecnicas(Enum):
    SUPRESION = "Supresión"
    SUSTITUCION = "Sustitución"

class Normas(Enum):
    HIPAA = "HIPAA"
    GDPR = "GDPR"    
    ISO27799 = "ISO-27799"    
    
@dataclass(frozen=True)
class Estandar:
    tecnica: Tecnicas
    norma: Normas

@dataclass(frozen=True)
class Rutina:
    script: str







from __future__ import annotations
from dataclasses import dataclass, field
from saludtech.modulos.scriptanonimiza.dominio.objetos_valor import ov
from saludtech.seedwork.dominio.entidades import AgregacionRaiz

@dataclass
class ScriptAnonimizacion(AgregacionRaiz):
    estandar: ov.Estandar = field(default_factory=ov.Estandar)
    rutina: ov.Rutina = field(default_factory=ov.Rutina)
    descripcion: str

    def __str__(self) -> str:
        return f"Script: {self.rutina.script} con el estándar: {self.estandar.tecnica.value} bajo la norma: {self.estandar.norma.value}"

    def dar_script(self, script: ScriptAnonimizacion) -> str:
        self.estandar = script.estandar
        self.rutina = script.rutina
        self.descripcion = script.descripcion
        return f"Script: {self.rutina.script} con el estándar: {self.estandar.tecnica.value} bajo la norma: {self.estandar.norma.value}"        
    

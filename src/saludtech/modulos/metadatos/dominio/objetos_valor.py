from saludtech.seedwork.dominio.objetos_valor import ObjetoValor
from dataclasses import dataclass

@dataclass(frozen=True)
class Token(ObjetoValor):
    token: str
    def __str__(self):
        return self.token
    def __repr__(self):
        return self.token
    

@dataclass(frozen=True)
class modalidad(ObjetoValor):
    modalidad: str
"""
Reglas de negocio del dominio de imágenes médicas

En este archivo usted encontrará reglas de negocio del dominio de imágenes médicas.
"""
from saludtech.seedwork.dominio.reglas import ReglaNegocio
from .objetos_valor import Token, Modalidad, ModalidadImagen, RegionCuerpo, RegionAnatomica


class ImagenDebeTenerToken(ReglaNegocio):
    #Regla que valida que una imagen debe tener un token único.

    token: Token

    def __init__(self, token, mensaje="Toda imagen debe tener un token único válido."):
        super().__init__(mensaje)
        self.token = token
        print(self.token)

    def es_valido(self) -> bool:
        print(self.token.valor)
        return len(self.token.valor) > 0


class ModalidadValida(ReglaNegocio):
    #Regla que valida si la modalidad de la imagen es reconocida.

    modalidad: Modalidad

    def __init__(self, modalidad, mensaje="La modalidad de la imagen debe ser válida."):
        super().__init__(mensaje)
        self.modalidad = modalidad

    def es_valido(self) -> bool:
        return self.modalidad.tipo in [tipo.value for tipo in ModalidadImagen]

class RegionAnatomicaValida(ReglaNegocio):
    #Regla que valida si la region anatomica de la imagen es reconocida.

    regionAnatomica: RegionAnatomica

    def __init__(self, regionAnatomica, mensaje="La región anatómica de la imagen debe ser válida."):
        super().__init__(mensaje)
        self.regionAnatomica = regionAnatomica

    def es_valido(self) -> bool:
        return self.regionAnatomica.tipo in [tipo.value for tipo in RegionCuerpo]

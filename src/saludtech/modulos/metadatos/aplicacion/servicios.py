from saludtech.seedwork.aplicacion.servicios import Servicio
from saludtech.modulos.metadatos.dominio.entidades import Metadatos
from saludtech.modulos.metadatos.dominio.fabricas import FabricaMetadatos
from saludtech.modulos.metadatos.infraestructura.fabricas import FabricaRepositorio
from .dto import ImagenDTO



class ServicioMetadatos(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_metadatos: FabricaMetadatos = FabricaMetadatos()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_metadatos(self):
        return self._fabrica_metadatos
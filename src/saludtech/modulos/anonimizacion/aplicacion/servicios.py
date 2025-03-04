from saludtech.seedwork.aplicacion.servicios import Servicio
from saludtech.modulos.anonimizacion.dominio.entidades import ImagenAnonimizada
from saludtech.modulos.anonimizacion.dominio.fabricas import FabricaImagenesAnonimizadas
from saludtech.modulos.anonimizacion.infraestructura.fabricas import FabricaRepositorio
from saludtech.modulos.anonimizacion.infraestructura.repositorios import RepositorioImagenesAnonimizadas
from .mapeadores import MapeadorImagen

from .dto import ImagenDTO

class ServicioImagenAnonimizada(Servicio):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_imagenes: FabricaImagenesAnonimizadas = FabricaImagenesAnonimizadas()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_imagenes(self):
        return self._fabrica_imagenes

    def crear_imagen_anonimizada(self, imagen_dto: ImagenDTO) -> ImagenDTO:
        imagen: ImagenAnonimizada = self.fabrica_imagenes.crear_objeto(imagen_dto, MapeadorImagen())

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioImagenesAnonimizadas.__class__)
        repositorio.agregar(imagen)

        return self.fabrica_imagenes.crear_objeto(imagen, MapeadorImagen())

    def obtener_imagen_por_id(self, id) -> ImagenDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioImagenesAnonimizadas.__class__)

        imagen = repositorio.obtener_por_id(id)

        if imagen is None:
            return '', 404

        return repositorio.obtener_por_id(id).__dict__
from aeroalpes.seedwork.aplicacion.servicios import Servicio
from aeroalpes.modulos.manejador_datos.dominio.entidades import Imagen
from aeroalpes.modulos.manejador_datos.dominio.fabricas import FabricaImagenes
from aeroalpes.modulos.manejador_datos.infraestructura.fabricas import FabricaRepositorio
from aeroalpes.modulos.manejador_datos.infraestructura.repositorios import RepositorioImagenes
from .mapeadores import MapeadorImagen

from .dto import ImagenDTO

class ServicioImagen(Servicio):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_imagenes: FabricaImagenes = FabricaImagenes()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_imagenes
    
    @property
    def fabrica_imagenes(self):
        return self._fabrica_vuelos

    def crear_imagen(self, imagen_dto: ImagenDTO) -> ImagenDTO:
        imagen: Imagen = self.fabrica_imagenes.crear_objeto(imagen_dto, MapeadorImagen())

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioImagenes.__class__)
        repositorio.agregar(imagen)

        return self.fabrica_imagenes.crear_objeto(imagen, MapeadorImagen())

    def obtener_imagen_por_id(self, id) -> ReservaDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioImagenes.__class__)
        return repositorio.obtener_por_id(id).__dict__
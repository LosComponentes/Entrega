from saludtech.seedwork.aplicacion.servicios import Servicio
from saludtech.modulos.manejador_datos.dominio.entidades import Imagen
from saludtech.modulos.manejador_datos.dominio.fabricas import FabricaImagenes
from saludtech.modulos.manejador_datos.infraestructura.fabricas import FabricaRepositorio
from saludtech.modulos.manejador_datos.infraestructura.repositorios import RepositorioImagenes
from .mapeadores import MapeadorImagen

from .dto import ImagenDTO

class ServicioImagen(Servicio):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_imagenes: FabricaImagenes = FabricaImagenes()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_imagenes(self):
        return self._fabrica_imagenes

    def crear_imagen(self, imagen_dto: ImagenDTO) -> ImagenDTO:
        print('crear_imagen')
        imagen: Imagen = self.fabrica_imagenes.crear_objeto(imagen_dto, MapeadorImagen())
        print('fabrica_imagenes.crear_objeto')
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioImagenes.__class__)
        print('fabrica_repositorio.crear_objeto')
        repositorio.agregar(imagen)
        print('repositorio.agregar')
        return self.fabrica_imagenes.crear_objeto(imagen, MapeadorImagen())

    def obtener_imagen_por_id(self, id) -> ImagenDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioImagenes.__class__)

        imagen = repositorio.obtener_por_id(id)

        if imagen is None:
            return '', 404

        return repositorio.obtener_por_id(id).__dict__
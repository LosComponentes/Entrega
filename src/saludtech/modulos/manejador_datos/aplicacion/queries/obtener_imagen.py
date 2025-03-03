from saludtech.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from saludtech.seedwork.aplicacion.queries import ejecutar_query as query
from saludtech.modulos.manejador_datos.infraestructura.repositorios import RepositorioImagenes
from dataclasses import dataclass
from .base import ImagenQueryBaseHandler
from saludtech.modulos.manejador_datos.aplicacion.mapeadores import MapeadorImagen

@dataclass
class ObtenerImagen(Query):
    id: str

class ObtenerImagenHandler(ImagenQueryBaseHandler):

    def handle(self, query: ObtenerImagen) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioImagenes.__class__)
        imagen = self.fabrica_imagenes.crear_objeto(repositorio.obtener_por_id(query.id), MapeadorImagen())
        return QueryResultado(resultado=imagen)

@query.register(ObtenerImagen)
def ejecutar_query_obtener_imagen(query: ObtenerImagen):
    handler = ObtenerImagenHandler()
    return handler.handle(query)

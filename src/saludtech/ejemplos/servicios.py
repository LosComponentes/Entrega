from saludtech.modulos.vuelos.dominio.objetos_valor import Odo, ParametroBusca
from saludtech.modulos.vuelos.dominio.entidades import Itinerario, Proveedor
from saludtech.modulos.vuelos.dominio.repositorios import RepositorioProveedores as rp
from saludtech.seedwork.dominio.servicios import Servicio
from saludtech.modulos.vuelos.dominio.mixins import FiltradoItinerariosMixin
from saludtech.modulos.vuelos.dominio.reglas import MinimoUnAdulto, RutaValida

class ServicioBusqueda(Servicio, FiltradoItinerariosMixin):

    def buscar_itinerarios(self, odos: list[Odo], parametros: ParametroBusca) -> list[Itinerario]:
        itinerarios: list[Itinerario] = list()
        proveedores:list[Proveedor] = rp.obtener_todos()
        
        self.validar_regla(MinimoUnAdulto(parametros.pasajeros))
        [self.validar_regla(RutaValida(ruta)) for odo in odos for segmento in odo.segmentos for ruta in segmento.legs]

        itinerarios.append([proveedor.obtener_itinerarios(odos, parametros) for proveedor in proveedores])

        return self.filtrar_mejores_itinerarios(itinerarios)
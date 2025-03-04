from saludtech.seedwork.aplicacion.comandos import Comando
from saludtech.modulos.manejador_datos.aplicacion.dto import ImagenDTO
from saludtech.modulos.manejador_datos.aplicacion.servicios import ServicioImagen
from saludtech.seedwork.aplicacion.comandos import ejecutar_comando as comando
from dataclasses import dataclass
from saludtech.modulos.manejador_datos.dominio.eventos import ImagenProcesada
from saludtech.modulos.manejador_datos.infraestructura.mensajeria import PublicadorEventos

@dataclass
class CrearImagen(Comando):
    id_imagen: str
    fecha_creacion: str
    fecha_actualizacion: str
    modalidad: str
    region_anatomica: str
    token: str
    condiciones: list
    metadata: dict

class CrearImagenHandler:
    
    def __init__(self):
        self.servicio_imagen = ServicioImagen()

    def handle(self, comando: CrearImagen):
        imagen_dto = ImagenDTO(
            id=comando.id_imagen,
            fecha_creacion=comando.fecha_creacion,
            fecha_actualizacion=comando.fecha_actualizacion,
            modalidad=comando.modalidad,
            region_anatomica=comando.region_anatomica,
            token=comando.token,
            condiciones=comando.condiciones,
            metadata=comando.metadata
        )

        imagen_creada = self.servicio_imagen.crear_imagen(imagen_dto)

        # Publicar evento en Apache Pulsar
        evento = ImagenProcesada(
            id_imagen=imagen_creada.id,
            estado="PROCESADA"
        )
        PublicadorEventos.publicar("eventos.imagenes.creadas", evento)

@comando.register(CrearImagen)
def ejecutar_comando_crear_imagen(comando: CrearImagen):
    handler = CrearImagenHandler()
    handler.handle(comando)

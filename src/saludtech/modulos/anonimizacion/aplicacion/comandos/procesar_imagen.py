from saludtech.seedwork.aplicacion.comandos import Comando
from saludtech.modulos.anonimizacion.aplicacion.dto import ImagenAnonimizadaDTO
from saludtech.modulos.anonimizacion.aplicacion.servicios import ServicioImagen
from saludtech.seedwork.aplicacion.comandos import ejecutar_comando as comando
from dataclasses import dataclass
from saludtech.modulos.anonimizacion.dominio.eventos import ImagenAnomizada
from saludtech.modulos.anonimizacion.infraestructura.mensajeria import PublicadorEventos

@dataclass
class CrearImagenAnonimizada(Comando):
    id_imagen: str
    tipo_anonimizacion: str
    fecha_creacion: str
    fecha_actualizacion: str
    modalidad: str
    region_anatomica: str
    token: str
    condiciones: list
    metadata: dict

class CrearImagenAnonimizadaHandler:
    
    def __init__(self):
        self.servicio_imagen = ServicioImagen()

    def handle(self, comando:CrearImagenAnonimizada):
        imagen_dto = ImagenAnonimizadaDTO(
            tipo_anonimizacion=comando.tipo_anonimizacion,
            id=comando.id_imagen,
            fecha_creacion=comando.fecha_creacion,
            fecha_actualizacion=comando.fecha_actualizacion,
            modalidad=comando.modalidad,
            region_anatomica=comando.region_anatomica,
            token=comando.token,
            condiciones=comando.condiciones,
            metadata=comando.metadata
        )

        imagen_creada = self.servicio_imagen.crear_imagen_anonimizada(imagen_dto)

        evento = ImagenAnomizada(
            id_imagen=imagen_creada.id,
            tipo_anonimizacion=imagen_creada.tipo_anonimizacion,
            token=imagen_creada.token,
            fecha_creacion=imagen_creada.fecha_creacion,
            fecha_adquisicion=imagen_creada.fecha_actualizacion
        )
        PublicadorEventos.publicar("eventos.imagenes.anonimizadas", evento)

@comando.register(CrearImagen)
def ejecutar_comando_crear_imagen(comando: CrearImagen):
    handler = CrearImagenAnonimizadaHandler()
    handler.handle(comando)

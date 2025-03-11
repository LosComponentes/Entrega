 
"""
DTOs para la capa de infraestructura del dominio de imágenes médicas
En este archivo usted encontrará los DTOs (modelos anémicos) de
la infraestructura del dominio de imágenes en SaludTech de los Alpes.
"""
from saludtech.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, String, Table, DateTime, Text
import uuid

Base = db.declarative_base()

# Tabla intermedia para la relación muchos a muchos entre imágenes y condiciones médicas
# imagenes_condiciones = db.Table(
#     "imagenes_condiciones",
#     db.Model.metadata,
#     db.Column("imagen_id", db.String(40), db.ForeignKey("imagenes.id")),
#     db.Column("tipo_condicion", db.String(100)),
#     db.ForeignKeyConstraint(
#         ["imagen_id"],
#         ["imagenes.id"]
#     )
# )
class Imagen(db.Model):
    __tablename__ = "imagenes"
    id = db.Column(db.String(40), primary_key=True, default=lambda: str(uuid.uuid4()))
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False)
    modalidad = db.Column(db.String(50), nullable=False)
    region_anatomica = db.Column(db.String(50), nullable=False)
    token = db.Column(db.String(100), unique=True, nullable=False)
    # condiciones = db.relationship("Condicion", secondary=imagenes_condiciones, backref="imagenes")
    condiciones = db.Column(db.String(4000), nullable=True)
    metadata_id = db.Column(db.String(40), ForeignKey("metadatos.id"))
    metadatas = db.relationship("Metadato", backref="imagen")

class Condicion(db.Model):
    __tablename__ = "condiciones"
    id = db.Column(db.String(40), primary_key=True, default=lambda: str(uuid.uuid4()))
    tipo_condicion = db.Column(db.String(100), nullable=False)

class Modalidad(db.Model):
    __tablename__ = "modalidades"
    id = db.Column(db.String(40), primary_key=True, default=lambda: str(uuid.uuid4()))
    tipo = db.Column(db.String(100), nullable=False)

class RegionCuerpo(db.Model):
    __tablename__ = "regiones_cuerpo"
    id = db.Column(db.String(40), primary_key=True, default=lambda: str(uuid.uuid4()))
    parteCuerpo = db.Column(db.String(100), nullable=False)

class Metadato(db.Model):
    __tablename__ = "metadatos"
    id = db.Column(db.String(40), primary_key=True, default=lambda: str(uuid.uuid4()))
    entorno_clinico = db.Column(db.String(50), nullable=False)
    contexto_procesal = db.Column(db.String(50), nullable=False)
    sintomas = db.Column(db.Text, nullable=True)  # JSON con lista de síntomas

class EventosImagen(db.Model):
    __tablename__ = "eventos_imagen"
    id = db.Column(db.String(40), primary_key=True, default=lambda: str(uuid.uuid4()))
    id_imagen = db.Column(db.String(40), nullable=False)
    fecha_evento = db.Column(db.DateTime, nullable=False)
    version = db.Column(db.String(10), nullable=False)
    tipo_evento = db.Column(db.String(100), nullable=False)
    formato_contenido = db.Column(db.String(10), nullable=False)
    nombre_servicio = db.Column(db.String(40), nullable=False)
    contenido = db.Column(db.Text, nullable=False)

class ImagenAnalitica(db.Model):
    __tablename__ = "analitica_imagenes"
    fecha_creacion = db.Column(db.Date, primary_key=True)
    total_procesadas = db.Column(db.Integer, primary_key=True, nullable=False)
 
 
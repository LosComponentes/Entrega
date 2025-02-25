"""DTOs para la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará los DTOs (modelos anémicos) de
la infraestructura del dominio de vuelos

"""

from saludtech.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

Base = db.declarative_base()

# Tabla intermedia para tener la relación de muchos a muchos entre la tabla reservas e itinerarios
imagenes_condiciones = db.Table(
    "imagenes_condiciones",
    db.Model.metadata,
    db.Column("imagen_id", db.String, db.ForeignKey("imagenes.id")),
    db.Column("tipo_condicion", db.String),
    db.ForeignKeyConstraint(
        ["tipo_condicion"],
        ["condiciones.tipo_condicion"]
    )
)

class Condicion(db.Model):
    __tablename__ = "condiciones"
    tipo_condicion= db.Column(db.String, nullable=False, primary_key=True)

class Metadata(db.Model):
    __tablename__ = "metadatos"
    entorno_clinico= db.Column(db.String, nullable=False, primary_key=True)
    contexto_procesal= db.Column(db.String, nullable=False, primary_key=True)
    
class Imagen(db.Model):
    __tablename__ = "imagenes"
    id = db.Column(db.String, primary_key=True)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    fecha_adquisicion = db.Column(db.DateTime, nullable=False)

"""DTOs para la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará los DTOs (modelos anémicos) de
la infraestructura del dominio de vuelos

"""

from saludtech.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

Base = db.declarative_base()

# Tabla intermedia para tener la relación de uno a muchos entre la tabla imagenes y condiciones
imagenes_condiciones = db.Table(
    "imagenes_condiciones",
    db.Model.metadata,
    db.Column("imagen_id", db.String, db.ForeignKey("imagenes.id")),
    db.Column("tipo_condicion", db.String),
    db.ForeignKeyConstraint(
        ["imagen_id"],
        ["imagenes.id"]
    )
)

# Tabla intermedia para tener la relación de uno a muchos entre la tabla imagenes y condiciones
metadata_sintomas = db.Table(
    "metadata_sintomas",
    db.Model.metadata,
    db.Column("imagen_id", db.String, db.ForeignKey("imagenes.id")),
    db.Column("tipo_condicion", db.String),
    db.ForeignKeyConstraint(
        ["imagen_id"],
        ["imagenes.id"]
    )
)

class Sintoma(db.Model):
    __tablename__ = "sintomas"
    tipo_condicion= db.Column(db.String, nullable=False, primary_key=True)

class Metadata(db.Model):
    __tablename__ = "metadatos"
    entorno_clinico= db.Column(db.String, nullable=False, primary_key=True)
    contexto_procesal= db.Column(db.String, nullable=False, primary_key=True)
    sintomas = db.relationship('Sintoma', secondary=metadata_sintomas, backref='metadatos')

class Condicion(db.Model):
    __tablename__ = "condiciones"
    tipo_condicion= db.Column(db.String, nullable=False, primary_key=True)
    
class Imagen(db.Model):
    __tablename__ = "imagenes"
    id = db.Column(db.String, primary_key=True)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False)
    modalidad = db.Column(db.String, nullable=False)
    region_anatomica = db.Column(db.String, nullable=False)
    token = db.Column(db.String, nullable=True)
    condiciones = db.relationship('Condicion', secondary=imagenes_condiciones, backref='imagenes')

    
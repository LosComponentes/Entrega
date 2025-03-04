from saludtech.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, String, Table, DateTime, Text
import uuid

class ImagenAnomizada(db.Model):
    __tablename__ = "imagenes_anonimizadas"
    id = db.Column(db.String(40), primary_key=True, default=lambda: str(uuid.uuid4()))
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False)
    modalidad = db.Column(db.String(50), nullable=False)
    region_anatomica = db.Column(db.String(50), nullable=False)
    token = db.Column(db.String(100), unique=True, nullable=False)
    condiciones = db.Column(db.String(4000), nullable=True)
    metadata_id = db.Column(db.String(40), ForeignKey("metadatos.id"))
    metadatas = db.relationship("Metadato", backref="imagen_anonimizada")
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum
from sqlalchemy.sql import func
import enum
from app.core.database import Base

class RolUsuario(str, enum.Enum):
    admin = "admin"
    gerente = "gerente"
    costero = "costero"
    disenador = "disenador"

class Empresa(Base):
    __tablename__ = "empresas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(200), nullable=False)
    nit = Column(String(50), unique=True, nullable=True)
    plan = Column(String(50), default="basico")
    config_moneda = Column(String(10), default="COP")
    activa = Column(Boolean, default=True)
    creada_en = Column(DateTime(timezone=True), server_default=func.now())

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    empresa_id = Column(Integer, nullable=False, index=True)
    nombre = Column(String(200), nullable=False)
    email = Column(String(200), unique=True, nullable=False, index=True)
    hash_password = Column(String(500), nullable=False)
    rol = Column(Enum(RolUsuario), default=RolUsuario.disenador)
    activo = Column(Boolean, default=True)
    creado_en = Column(DateTime(timezone=True), server_default=func.now())
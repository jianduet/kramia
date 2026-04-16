from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class Cotizacion(Base):
    __tablename__ = "cotizaciones"

    id = Column(Integer, primary_key=True, index=True)
    
    empresa_id = Column(Integer, ForeignKey("empresas.id"), nullable=False)

    nombre = Column(String, nullable=False)
    descripcion = Column(String, nullable=True)

    estado = Column(String, default="borrador")  # borrador | aprobado | descartado

    cliente = Column(String, nullable=True)
    moneda = Column(String, default="COP")

    creado_en = Column(DateTime(timezone=True), server_default=func.now())
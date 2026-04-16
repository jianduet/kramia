from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CotizacionBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    cliente: Optional[str] = None
    moneda: Optional[str] = "COP"

class CotizacionCreate(CotizacionBase):
    pass

class CotizacionUpdate(BaseModel):
    nombre: Optional[str]
    descripcion: Optional[str]
    estado: Optional[str]

class CotizacionOut(CotizacionBase):
    id: int
    estado: str
    creado_en: datetime

    class Config:
        from_attributes = True
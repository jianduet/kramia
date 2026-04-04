from pydantic import BaseModel, EmailStr
from enum import Enum

class RolUsuario(str, Enum):
    admin = "admin"
    gerente = "gerente"
    costero = "costero"
    disenador = "disenador"

class EmpresaCreate(BaseModel):
    nombre: str
    nit: str | None = None
    config_moneda: str = "COP"

class EmpresaResponse(BaseModel):
    id: int
    nombre: str
    plan: str
    config_moneda: str

    class Config:
        from_attributes = True

class UsuarioCreate(BaseModel):
    nombre: str
    email: EmailStr
    password: str
    nombre_empresa: str
    nit_empresa: str | None = None

class UsuarioLogin(BaseModel):
    email: EmailStr
    password: str

class UsuarioResponse(BaseModel):
    id: int
    nombre: str
    email: str
    rol: RolUsuario
    empresa_id: int

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str
    usuario: UsuarioResponse
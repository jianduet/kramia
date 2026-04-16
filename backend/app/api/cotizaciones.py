from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.cotizacion import CotizacionCreate, CotizacionOut, CotizacionUpdate
from app.core.security import get_current_user
from app.services.cotizacion_service import *

router = APIRouter(prefix="/cotizaciones", tags=["Cotizaciones"])


# 🔹 CREAR
@router.post("/", response_model=CotizacionOut)
def crear(
    data: CotizacionCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return crear_cotizacion(db, data, current_user["empresa_id"])


# 🔹 LISTAR
@router.get("/", response_model=list[CotizacionOut])
def listar(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return obtener_cotizaciones(db, current_user["empresa_id"])


# 🔹 OBTENER
@router.get("/{id}", response_model=CotizacionOut)
def get_one(
    id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    cotizacion = obtener_cotizacion(db, id, current_user["empresa_id"])
    
    if not cotizacion:
        raise HTTPException(status_code=404, detail="No encontrada")
    
    return cotizacion


# 🔹 ACTUALIZAR
@router.put("/{id}", response_model=CotizacionOut)
def actualizar(
    id: int,
    data: CotizacionUpdate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    cotizacion = obtener_cotizacion(db, id, current_user["empresa_id"])

    if not cotizacion:
        raise HTTPException(status_code=404, detail="No encontrada")

    return actualizar_cotizacion(db, cotizacion, data)


# 🔹 ELIMINAR
@router.delete("/{id}")
def eliminar(
    id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    cotizacion = obtener_cotizacion(db, id, current_user["empresa_id"])

    if not cotizacion:
        raise HTTPException(status_code=404, detail="No encontrada")

    eliminar_cotizacion(db, cotizacion)

    return {"msg": "Eliminada"}
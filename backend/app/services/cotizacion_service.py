from sqlalchemy.orm import Session
from app.models.cotizacion import Cotizacion

def crear_cotizacion(db: Session, data, empresa_id: int):
    nueva = Cotizacion(
        nombre=data.nombre,
        descripcion=data.descripcion,
        cliente=data.cliente,
        moneda=data.moneda,
        empresa_id=empresa_id
    )
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva


def obtener_cotizaciones(db: Session, empresa_id: int):
    return db.query(Cotizacion).filter(
        Cotizacion.empresa_id == empresa_id
    ).all()


def obtener_cotizacion(db: Session, cotizacion_id: int, empresa_id: int):
    return db.query(Cotizacion).filter(
        Cotizacion.id == cotizacion_id,
        Cotizacion.empresa_id == empresa_id
    ).first()


def actualizar_cotizacion(db: Session, cotizacion, data):
    for key, value in data.dict(exclude_unset=True).items():
        setattr(cotizacion, key, value)

    db.commit()
    db.refresh(cotizacion)
    return cotizacion


def eliminar_cotizacion(db: Session, cotizacion):
    db.delete(cotizacion)
    db.commit()
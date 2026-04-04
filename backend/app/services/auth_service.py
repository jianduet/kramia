from sqlalchemy.orm import Session
from app.models.usuario import Usuario, Empresa
from app.schemas.usuario import UsuarioCreate, UsuarioLogin
from app.core.security import hash_password, verify_password, create_access_token
from fastapi import HTTPException, status

def registrar_empresa_y_usuario(datos: UsuarioCreate, db: Session):
    # Verificar si el email ya existe
    existe = db.query(Usuario).filter(Usuario.email == datos.email).first()
    if existe:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Este email ya está registrado"
        )

    # Crear la empresa primero
    empresa = Empresa(
        nombre=datos.nombre_empresa,
        nit=datos.nit_empresa,
    )
    db.add(empresa)
    db.flush()  # genera el id de la empresa sin confirmar aún

    # Crear el usuario admin de esa empresa
    usuario = Usuario(
        empresa_id=empresa.id,
        nombre=datos.nombre,
        email=datos.email,
        hash_password=hash_password(datos.password),
        rol="admin"  # el primero en registrarse es admin
    )
    db.add(usuario)
    db.commit()
    db.refresh(usuario)

    # Generar token
    token = create_access_token({
        "sub": str(usuario.id),
        "empresa_id": usuario.empresa_id,
        "rol": usuario.rol
    })

    return {
        "access_token": token,
        "token_type": "bearer",
        "usuario": usuario
    }

def login_usuario(datos: UsuarioLogin, db: Session):
    # Buscar usuario por email
    usuario = db.query(Usuario).filter(Usuario.email == datos.email).first()

    if not usuario or not verify_password(datos.password, usuario.hash_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email o contraseña incorrectos"
        )

    if not usuario.activo:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Usuario inactivo"
        )

    # Generar token
    token = create_access_token({
        "sub": str(usuario.id),
        "empresa_id": usuario.empresa_id,
        "rol": usuario.rol
    })

    return {
        "access_token": token,
        "token_type": "bearer",
        "usuario": usuario
    }

def get_usuario_actual(token_data: dict, db: Session):
    usuario_id = int(token_data.get("sub"))
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario or not usuario.activo:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Sesión inválida"
        )
    return usuario
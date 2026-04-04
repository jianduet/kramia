from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import decode_token
from app.schemas.usuario import UsuarioCreate, UsuarioLogin, Token, UsuarioResponse
from app.services.auth_service import registrar_empresa_y_usuario, login_usuario, get_usuario_actual

router = APIRouter(prefix="/auth", tags=["Autenticación"])
bearer = HTTPBearer()

@router.post("/registro", response_model=Token)
def registro(datos: UsuarioCreate, db: Session = Depends(get_db)):
    return registrar_empresa_y_usuario(datos, db)

@router.post("/login", response_model=Token)
def login(datos: UsuarioLogin, db: Session = Depends(get_db)):
    return login_usuario(datos, db)

@router.get("/me", response_model=UsuarioResponse)
def mi_perfil(
    credentials: HTTPAuthorizationCredentials = Depends(bearer),
    db: Session = Depends(get_db)
):
    token_data = decode_token(credentials.credentials)
    if not token_data:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o expirado"
        )
    return get_usuario_actual(token_data, db)
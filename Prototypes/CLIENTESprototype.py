from fastapi import FastAPI , HTTPException, status, Depends, APIRouter
from sqlalchemy.orm import Session
from database.almacen import abrir_puerta, miclaseBase, motor
from modules.Clients.model import Clients
from modules.usuarios.model import Users
from utils.hash import encriptar_contrasena
from modules.Clients.schema import Revisar_JSON_Crear_Nuevo_Cliente


router = APIRouter(
    prefix = "/clients",
    tags = ["Clients"]
)

@router.post("/")
def crear_nuevo_cliente(json: Revisar_JSON_Crear_Nuevo_Cliente,
                        db: Session = Depends(abrir_puerta)
                        ):
    
    check = db.query(Clients).filter(Clients.email == json.email).first()
    
    if check is not None:
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail = "Cliente ya esta registrado"
        )
    else:
        
        new_user = Users(
            
            user = json.user,
            password = encriptar_contrasena(json.password),
            rol = json.rol
        )
        
        db.add(new_user)
        db.refresh(new_user)
        
        new_customer = Clients(
            nombre = json.nombre,
            email = json.email,
            id_user = new_user.id
        )
        
        db.add(new_customer)
        db.commit()
        db.refresh(new_customer)
        return new_customer
        
        
        
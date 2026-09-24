from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from modules.Clients.repository import ClientsRepository as repo
from modules.Clients.model import Clients
from modules.usuarios.model import Users
from modules.Clients.schema import Revisar_JSON_Crear_Nuevo_Cliente
from utils.hash import encriptar_contrasena


class ClientsService():
    
    @staticmethod
    def crear_cliente(db: Session , json: Revisar_JSON_Crear_Nuevo_Cliente):
        
        check = repo.revisar_duplicados(db,json)
        
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
            
            new_u = repo.crear_nuevo_user(db,new_user)
                
                
            new_customer = Clients(
                    nombre = json.nombre,
                    email = json.email,
                    id_user = new_user.id
                )
            
            new_c = repo.crear_nuevo_customer(db,new_customer)
            return new_c
                
    
            
        
        



"""

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
        


"""
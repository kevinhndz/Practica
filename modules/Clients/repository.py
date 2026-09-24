# modules/Clients/repository.py
from sqlalchemy.orm import Session
from modules.Clients.model import Clients

class ClientsRepository():
    
    @staticmethod
    def revisar_duplicados(db: Session, json: dict) -> dict:
        check = db.query(Clients).filter(Clients.email == json.email).first()
        return check
        
    @staticmethod
    def crear_nuevo_user(db: Session, new_user: dict) -> dict:
        db.add(new_user)
        db.commit()          
        db.refresh(new_user) 
        return new_user
    
    @staticmethod
    def crear_nuevo_customer(db: Session, new_customer:dict) -> dict:
        db.add(new_customer)
        db.commit()         
        db.refresh(new_customer)
        return new_customer
    
    @staticmethod
    def revisar_duplicados_por_ID_put(db: Session, id: int) -> dict:
        check = db.query(Clients).filter(Clients.id == id).first()
        return check
    
    @staticmethod
    def guardar_cambios_put(db: Session, cliente_editado: dict) -> dict:
        db.commit()
        db.refresh(cliente_editado)
        return cliente_editado
        



"""
@router.put("/{id}")
def editar(id: int, json: Revisar_JSON_Editar_Cliente, db: Session = Depends(abrir_puerta)):
    
    check = db.query(Clients).filter(Clients.id == id).first()
    
    if check is not None:
        check.nombre = json.nombre
        check.email = json.email
        db.commit()
        db.refresh(check)
        return check
    else:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail = "No se encontro el recurso"
        )
        

"""
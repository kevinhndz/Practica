# modules/Clients/repository.py
from sqlalchemy.orm import Session
from modules.Clients.model import Clients

class ClientsRepository():
    
    @staticmethod
    def revisar_duplicados(db: Session, json: dict) -> dict:
        check = db.query(Clients).filter(Clients.email == json.email).first()
        return check
        
    @staticmethod
    def crear_nuevo_user(db: Session, new_user) -> dict:
        db.add(new_user)
        db.commit()          
        db.refresh(new_user) 
        return new_user
    
    @staticmethod
    def crear_nuevo_customer(db: Session, new_customer) -> dict:
        db.add(new_customer)
        db.commit()         
        db.refresh(new_customer)
        return new_customer


"""
check = db.query(Clients).filter(Clients.email == json.email).first()

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
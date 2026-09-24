from sqlalchemy.orm import Session
from modules.usuarios.model import Users

class UsuariosRepository ():
    
    @staticmethod
    def revisar(db: Session, json: dict) -> dict:
        return  db.query(Users).filter(Users.user == json.user).first()






"""

#json waiting
@router.post("/")
def login(json: Revisar_JSON_Login, db: Session = Depends(abrir_puerta)):
    
    check = db.query(Users).filter(Users.user == json.user).first()
    
    if check is None or not verificar_contrasena(json.password, check.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña incorrectos"
        )
    else:
        token = crear_token(check.id, check.user, check.rol)
        return {"user": check.user, "id_user": check.id, "token": token}
    

"""
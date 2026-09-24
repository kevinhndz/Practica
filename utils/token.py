import os
from dotenv import load_dotenv
from fastapi import Depends, Header, HTTPException, status
from jose import jwt, JWTError
from datetime import datetime, timezone, timedelta


load_dotenv()

KEY = os.getenv("SECRET_KEY")
#return {"user": check.user, "id_user": check.id, "token": token}
def crear_token(user: str, id_user: int, rol:str) -> str:
    
    expires = datetime.now(timezone.utc) + timedelta(minutes= 20)
    
    data = {
        "user": user,
        "id_user": id_user,
        "rol": rol,
        "exp": expires
    }
    
    token = jwt.encode(
        KEY,
        data,
        algorithm="HS256"
    )
    
    return token



def verificar_token(token: str):
    
    try:
        
        user_data = jwt.decode(
        KEY,
        token,
        algorithms=["HS256"]
    )
        return user_data
    
    except JWTError:
        raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, detail = "Session expirada")
    
import os
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
from fastapi import HTTPException, status
from jose import JWTError, jwt

load_dotenv()

KEY = os.getenv("SECRET_KEY")


def crear_token(user: str, id_user: int, rol: str) -> str:
    expires = datetime.now(timezone.utc) + timedelta(minutes=20)

    data = {
        "user": user,
        "id_user": id_user,
        "rol": rol,
        "exp": expires
    }

    
    token = jwt.encode(data, KEY, algorithm="HS256")

    return token


def verificar_token(token: str):
    try:
        user_data = jwt.decode(
            token,
            KEY,
            algorithms=["HS256"]
        )
        return user_data

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="Session expirada"
        )
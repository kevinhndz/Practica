from pydantic import BaseModel, Field, EmailStr

class Revisar_JSON_Crear_Nuevo_Cliente(BaseModel):
    
    nombre: str = Field(min_length= 3, max_length=30)
    email: EmailStr
    user: str = Field(min_length=5, max_length=16)
    password: str = Field(min_length= 6, max_length=20)
    rol :str
        
class Revisar_JSON_Editar_Cliente(BaseModel):
    
    nombre: str = Field(min_length= 3, max_length=30)
    email: EmailStr
    rol :str
        

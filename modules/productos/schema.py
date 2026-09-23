from pydantic import BaseModel, Field

class Revisar_JSON_Crear_Producto(BaseModel):
    
    nombre: str = Field (min_length=3, max_length=25)
    stock : int = Field(ge = 0)
    codigo: str
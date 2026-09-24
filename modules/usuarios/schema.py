from pydantic import BaseModel, Field

class Revisar_JSON_Login(BaseModel):
    
    user: str = Field(min_length=5, max_length=16)
    password: str = Field(min_length= 6, max_length=20)
    
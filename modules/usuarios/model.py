from sqlalchemy import Integer, String, Column, ForeignKey
from database.almacen import miclaseBase

class Users (miclaseBase):
    
    __tablename__ = "Users"
    
    id = Column(Integer, primary_key= True, index = True)
    user = Column(String, nullable= False)
    password = Column(String, nullable = False)
    rol = Column(String, nullable=False)
    

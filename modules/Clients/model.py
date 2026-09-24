from sqlalchemy import Integer, String, Column, ForeignKey
from database.almacen import miclaseBase

class Clients(miclaseBase):
    
    __tablename__ = "Clients"
    
    id = Column(Integer, primary_key= True, index = True)
    nombre = Column(String, nullable= False)
    email = Column(String, nullable = False)
    id_user = Column(Integer, ForeignKey("Users.id"))
    


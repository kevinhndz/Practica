from fastapi import FastAPI , APIRouter,Depends
from modules.Clients.schema import Revisar_JSON_Crear_Nuevo_Cliente
from modules.Clients.model import Clients
from database.almacen import abrir_puerta
from sqlalchemy.orm import Session
from modules.Clients.service import ClientsService as service


router = APIRouter(
    prefix = "/clients",
    tags = ["Clients"]
)

@router.post("/")
def crear_nuevo_cliente(json:Revisar_JSON_Crear_Nuevo_Cliente, db: Session = Depends(abrir_puerta)):
    return service.crear_cliente(db,json)

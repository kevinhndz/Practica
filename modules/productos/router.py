from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.almacen import abrir_puerta
from modules.productos.schema import Revisar_JSON_Crear_Producto
from modules.productos.service import ProductosService as service

router = APIRouter(
    prefix="/productos",
    tags=["Productos"]
)

@router.post("/", status_code=201)
def crear_producto(json: Revisar_JSON_Crear_Producto, db: Session = Depends(abrir_puerta)):
    return service.verificar(db, json)

@router.get("/")
def ver_productos(limite: int = 10, salto: int = 0, db: Session = Depends(abrir_puerta)):
    return service.revisar_si_hay(db, limite, salto)


"""

@router.get("/")
def ver_productos (limite: int = 10, salto: int = 0 ,db: Session = Depends (abrir_puerta)):
    
    check = db.query(Productos).offset(salto).limit(limite).all()
    
    if not check:
        raise HTTPException(
            satus_code = status.HTTP_404_NOT_FOUND,
            detail = "No records found!"
        )
    else:
        return check

"""
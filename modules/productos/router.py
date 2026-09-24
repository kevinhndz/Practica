from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session
from database.almacen import abrir_puerta
from modules.productos.schema import Revisar_JSON_Crear_Producto, Revisar_JSON_Editar_Producto
from modules.productos.service import ProductosService as service

router = APIRouter(
    prefix="/productos",
    tags=["Productos"]
)

@router.post("/", status_code=201)
def crear_producto(json: Revisar_JSON_Crear_Producto, db: Session = Depends(abrir_puerta)):
    return service.verificar(db, json)

@router.get("/")
def ver_productos(
    limite: int = Query(default=10, ge=1, le=100, description="Cantidad de productos a retornar (minimo 1, maximo 100)"),
    salto: int = Query(default=0, ge=0, description="Cantidad de registros a saltar para la paginacion"),
    db: Session = Depends(abrir_puerta)
):
    return service.revisar_si_hay(db, limite, salto)

@router.put("/{id}")
def editar_producto(id: int, json: Revisar_JSON_Crear_Producto, db: Session = Depends(abrir_puerta)):
    return service.editar_producto(db, id, json)

@router.patch("/{id}")
def editar_producto_parcial(id: int, json: Revisar_JSON_Editar_Producto, db: Session = Depends(abrir_puerta)):
    return service.editar_producto_parcial(db, id, json)

@router.delete("/{id}")
def borrar_producto(id: int, db: Session = Depends(abrir_puerta)):
    return service.borrar_producto(db, id)
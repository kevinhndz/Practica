from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from modules.productos.repository import ProductosRepository as repo
from modules.productos.model import Productos
from modules.productos.schema import Revisar_JSON_Crear_Producto

class ProductosService:
    
    @staticmethod
    def verificar(db: Session, json: Revisar_JSON_Crear_Producto):
        revisar = repo.check_existencia_producto(db, json)
        
        if revisar is not None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"El producto con codigo {json.codigo} ya existe"
            )
        else:
            nuevo = Productos(
                nombre=json.nombre,
                stock=json.stock,
                codigo=json.codigo
            )
            
            return repo.agregar_producto_al_sistema(db, nuevo)
    
    @staticmethod
    def revisar_si_hay(db: Session, limite: int = 10, salto: int = 0):
        check = repo.mandar_a_pedir_productos(db, limite, salto)
        
        if not check:
                raise HTTPException(
                    status_code = status.HTTP_404_NOT_FOUND,
                    detail = "No records found!"
                )
        else:
            return check
        
        
        


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
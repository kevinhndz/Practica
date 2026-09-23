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


"""
#json
@router.post("/", status_code= 201)
def crear_producto(json: Revisar_JSON_Crear_Producto,
                   db:Session = Depends(abrir_puerta)
                   ):
    
    check = db.query(Productos).filter(Productos.codigo == json.codigo).first()
    
    if check is not None:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = f"El producto con codigo {json.codigo} ya existe"
        )
    else:
        nuevo = Productos(
            nombre = json.nombre,
            stock = json.stock,
            codigo = json.codigo
        )
        
        db.add(nuevo)
        db.commit()
        db.refresh(nuevo)
        return {"Mensaje": f"Producto: {nuevo.nombre} con ID : {nuevo.id} creado exitosamente"}


"""
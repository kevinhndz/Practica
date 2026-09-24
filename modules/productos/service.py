from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from modules.productos.repository import ProductosRepository as repo
from modules.productos.model import Productos
from modules.productos.schema import Revisar_JSON_Crear_Producto, Revisar_JSON_Editar_Producto

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
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No records found!"
            )
        else:
            return check

    @staticmethod
    def editar_producto(db: Session, id: int, json: Revisar_JSON_Crear_Producto):
        check = repo.buscar_por_id(db, id)
        
        if check is not None:
            check.nombre = json.nombre
            check.codigo = json.codigo
            check.stock = json.stock
            return repo.guardar_cambios(db, check)
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Recurso no encontrado"
            )

    @staticmethod
    def editar_producto_parcial(db: Session, id: int, json: Revisar_JSON_Editar_Producto):
        check = repo.buscar_por_id(db, id)
        
        if check is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Recurso no encontrado"
            )
        
        datos_a_actualizar = json.model_dump(exclude_unset=True)
        
        for clave, valor in datos_a_actualizar.items():
            setattr(check, clave, valor)
            
        return repo.guardar_cambios(db, check)

    @staticmethod
    def borrar_producto(db: Session, id: int):
        check = repo.buscar_por_id(db, id)
        
        if check is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Recurso no encontrado"
            )
        
        repo.eliminar_producto(db, check)
        return {"mensaje": f"El producto con ID {id} fue eliminado correctamente"}
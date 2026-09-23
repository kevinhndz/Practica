from sqlalchemy.orm import Session
from modules.productos.model import Productos
from modules.productos.schema import Revisar_JSON_Crear_Producto

class ProductosRepository:
    
    @staticmethod
    def check_existencia_producto(db: Session, json: Revisar_JSON_Crear_Producto):
        check = db.query(Productos).filter(Productos.codigo == json.codigo).first()
        return check
    
    @staticmethod
    def agregar_producto_al_sistema(db: Session, json: Productos):
        db.add(json)
        db.commit()
        db.refresh(json)
        return {"Mensaje": f"Producto: {json.nombre} con ID : {json.id} creado exitosamente"}
"""


    check = db.query(Productos).filter(Productos.codigo == json.codigo).first()
    
    
        db.add(nuevo)
        db.commit()
        db.refresh(nuevo)
        return {"Mensaje": f"Producto: {nuevo.nombre} con ID : {nuevo.id} creado exitosamente"}


"""
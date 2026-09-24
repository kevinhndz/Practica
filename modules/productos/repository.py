from sqlalchemy.orm import Session
from modules.productos.model import Productos
from modules.productos.schema import Revisar_JSON_Crear_Producto

class ProductosRepository:
    
    @staticmethod
    def check_existencia_producto(db: Session, json: Revisar_JSON_Crear_Producto):
        check = db.query(Productos).filter(Productos.codigo == json.codigo).first()
        return check
    
    @staticmethod
    def buscar_por_id(db: Session, id: int):
        return db.query(Productos).filter(Productos.id == id).first()
    
    @staticmethod
    def agregar_producto_al_sistema(db: Session, json: Productos):
        db.add(json)
        db.commit()
        db.refresh(json)
        return {"Mensaje": f"Producto: {json.nombre} con ID : {json.id} creado exitosamente"}
    
    @staticmethod
    def mandar_a_pedir_productos(db: Session, limite: int = 10, salto: int = 0):
        check = db.query(Productos).offset(salto).limit(limite).all()
        return check

    @staticmethod
    def guardar_cambios(db: Session, producto: Productos):
        db.commit()
        db.refresh(producto)
        return producto

    @staticmethod
    def eliminar_producto(db: Session, producto: Productos):
        db.delete(producto)
        db.commit()




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
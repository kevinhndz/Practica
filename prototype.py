from fastapi import FastAPI , HTTPException, status, Depends, APIRouter
from sqlalchemy.orm import Session
from database.almacen import abrir_puerta, miclaseBase, motor
from modules.productos.model import Productos
from modules.productos.schema import Revisar_JSON_Crear_Producto

app = FastAPI()

miclaseBase.metadata.create_all(bind = motor)

router = APIRouter(
    prefix = "/productos",
    tags = ["Productos"]
)

#PROTOTIPO DE POST


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
    
    
    
#PROTOTIPO DE GET:

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
from fastapi import FastAPI
from database.almacen import miclaseBase, motor
from modules.productos.router import router as router_productos

app = FastAPI(
    title="Sistema de Almacen",
    version="1.0.0"
)

# Crear tablas en la base de datos al arrancar
miclaseBase.metadata.create_all(bind=motor)

# Registrar rutas del modulo de productos
app.include_router(router_productos)
}
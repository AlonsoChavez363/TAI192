from fastapi import FastAPI
from DB.conexion import engine,  Base
from routers.usuario import routerUsuario
from routers.auth  import routerToken


app = FastAPI(
    title="Mi Primer API 192",
    description="Alonso",
    version="1.0.1",
)



Base.metadata.create_all(bind=engine)

#endpoint home
@app.get('/', tags=['Hola Mundo'])
def home():
    return "Hola Mundo"

app.include_router(routerUsuario)
app.include_router(routerToken)
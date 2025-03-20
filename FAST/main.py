from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from typing import Optional,List
from modelsPydantic import ModeloUsuario, modeloAuth
from genToken import createToken
from middlewares import BearerJWT
from DB.conexion import session, engine,  Base
from models.modelsDB import User


app = FastAPI(
    title="Mi Primer API 192",
    description="Alonso",
    version="1.0.1",
)


Base.metadata.create_all(bind=engine)

usuarios = [
    {"id": 1, "nombre": "Alonso", "edad": 20, "correo":"example@example.com"},
    {"id": 2, "nombre": "Elvira", "edad": 20,"correo":"example@example.com"},
    {"id": 3, "nombre": "Ana", "edad": 20,"correo":"example@example.com"},
    {"id": 4, "nombre": "Fatima", "edad": 20,"correo":"example@example.com"},
]
#Endpoint home
@app.get('/', tags=['Hola Mundo'])
def home():
    return "Hola Mundo"

#Endpoitn Autenticacion
@app.post('/auth', tags=["Autentificacion"])
def login(autorizacion:modeloAuth):
    if autorizacion.correo == 'alonso@example.com' and autorizacion.passw == '123456789':
        token:str = createToken(autorizacion.model_dump())
        print(token)
        return JSONResponse(token)
    else:
        return{"Usuario no registrado"}

# Endpoint CONSULTA TODOS
@app.get("/todosUsuarios", dependencies=[Depends(BearerJWT())],response_model=List[ModeloUsuario], tags=["Operaciones CRUD"])
def leerUsuarios():
    return usuarios



#Endpoint Agregar nuevos
@app.post('/usuario/', response_model= ModeloUsuario, tags=['Operaciones CRUD'])
def agregarUsuario(usuario:ModeloUsuario):
    db= session()
    try:
        db.add(User(**usuario.model_dump()))   
        db.commit()
        return JSONResponse(status_code=201,
                            content={"message":"Usuario Guardado",
                                     "usuario":usuario.model_dump() } )
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500,
                            content={"message":"Error al guardar el usuario",} )
    finally:
        db.close()
    
#Endpoint actualizar usuraios(put)
@app.put('/usuarios/{id}', response_model= ModeloUsuario, tags=['Operaciones CRUD'])
def actualizar(id:int, usuarioActualizado:ModeloUsuario):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index]=usuarioActualizado.model_dump()
            return usuarios[index]
    raise HTTPException(status_code=400, detail="El usuario no existe") 


@app.delete('/usuarios/borrar', tags=['Operaciones Crud'])
def eliminar(id:int):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            del usuarios[index]
            return {'Usuario eliminado': usuarios}
    raise HTTPException(status_code=400, detail="El usuario no existe")

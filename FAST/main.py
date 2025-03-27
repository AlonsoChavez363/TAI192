from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
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
@app.get("/todosUsuarios", tags=["Operaciones CRUD"])
def leerUsuarios():
    db= session()
    try:
        consulta= db.query(User).all()
        return JSONResponse(content= jsonable_encoder(consulta))

    except Exception as e:
        return JSONResponse(status_code=500,
                            content={"message":"Error al consultar",
                                     "Exception": str(e)} )
    finally:
        db.close()
    

#Endpoitn para buscar por id
@app.get('/usuario/{id}', tags=["Operaciones CRUD"])
def buscarUno(id:int):
    db = session()
    try: 
        consultauno=db.query(User).filter(User.id == id).first()
        if not consultauno:
            return JSONResponse(status_code=404, content={"Mensaje":"Usuario no encontrado"})
        return JSONResponse(content= jsonable_encoder(consultauno))
    
    except Exception as e:
        return JSONResponse(status_code=500,
                            content={"message":"Error al consultar",
                                     "Exception": str(e)} )
    
    finally:
        db.close()




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
def actualizar(id: int, usuarioActualizado: ModeloUsuario):
    db = session()
    try:
        usuario = db.query(User).filter(User.id == id).first()
        if not usuario:
            return JSONResponse(status_code=404, content={"Mensaje": "Usuario no encontrado"})
        
        db.query(User).filter(User.id == id).update(usuarioActualizado.model_dump())
        db.commit()
        return JSONResponse(status_code=200, content={"Mensaje": "Usuario actualizado"})
    
    except Exception:
        db.rollback()
        return JSONResponse(status_code=500, content={"Mensaje": "Error al actualizar"})
    
    finally:
        db.close()




#Endpont eliminar usuario(del)
@app.delete('/usuarios/borrar/{id}', response_model = ModeloUsuario, tags=['Operaciones CRUD'])
def eliminarUno(id:int):
    db = session()
    try: 
        eliminaruno=db.query(User).filter(User.id == id).first()
        if not eliminaruno:
            return JSONResponse(status_code=404, content={"Mensaje":"Usuario no encontrado"})
        else:
            db.delete(eliminaruno)  
            db.commit()
            return JSONResponse(status_code=200, content={"Mensaje": "Usuario eliminado", "usuario": id})
    
    except Exception as e:
        return JSONResponse(status_code=500,
                            content={"Mensaje": "Error al consultar",
                                    "Exception": str(e)})
    
    finally:
        db.close()


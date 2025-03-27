from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Optional,List
from modelsPydantic import ModeloUsuario, modeloAuth
from genToken import createToken
from middlewares import BearerJWT
from DB.conexion import session, engine,  Base
from models.modelsDB import User
from fastapi import APIRouter

routerUsuario = APIRouter()


# Endpoint CONSULTA TODOS
@routerUsuario.get("/todosUsuarios", tags=["Operaciones CRUD"])
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
@routerUsuario.get('/usuario/{id}', tags=["Operaciones CRUD"])
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
@routerUsuario.post('/usuario/', response_model= ModeloUsuario, tags=['Operaciones CRUD'])
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
@routerUsuario.put('/usuarios/editar/{id}', response_model= ModeloUsuario, tags=['Operaciones CRUD'])
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
@routerUsuario.delete('/usuarios/borrar/{id}', response_model = ModeloUsuario, tags=['Operaciones CRUD'])
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





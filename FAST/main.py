from fastapi import FastAPI, HTTPException
from typing import Optional,List
from models import ModeloUsuario

app = FastAPI(
    title="Mi Primer API 192",
    description="Alonso",
    version="1.0.1",
)




usuarios = [
    {"id": 1, "nombre": "Alonso", "edad": 20, "correo":"example@example.com"},
    {"id": 2, "nombre": "Elvira", "edad": 20,"correo":"example@example.com"},
    {"id": 3, "nombre": "Ana", "edad": 20,"correo":"example@example.com"},
    {"id": 4, "nombre": "Fatima", "edad": 20,"correo":"example@example.com"},
]

# Endpoint CONSULTA TODOS
@app.get("/todosUsuarios",response_model=List[ModeloUsuario], tags=["Operaciones CRUD"])
def leerUsuarios():
    return usuarios



#Endpoint Agregar nuevos
@app.post('/usuario/', response_model= ModeloUsuario, tags=['Operaciones CRUD'])
def agregarUsuario(usuario:ModeloUsuario):
    for usr in usuarios:
        if usr["id"] == usuario.id:
            raise HTTPException(status_code=400, detail="el ID ya esta en uso ")
    usuarios.append(usuario)        
    return usuario

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

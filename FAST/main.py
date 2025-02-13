from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI(
    title="Mi Primer API 192",
    description="Alonso",
    version="1.0.1",
)

usuarios = [
    {"id": 1, "nombre": "Alonso", "edad": 20},
    {"id": 2, "nombre": "Elvira", "edad": 20},
    {"id": 3, "nombre": "Fernanda", "edad": 20},
    {"id": 4, "nombre": "Alma", "edad": 20},
]

# Endpoint CONSULTA TODOS
@app.get("/todosUsuarios", tags=["Operaciones CRUD"])
def leerUsuarios():
    return{"Los usuarios registrados son":   usuarios}


#Endpoint Agregar nuevos
@app.post('/usuario/', tags=['Operaciones CRUD'])
def agregarUsuario(usuario:dict):
    for usr in usuarios:
        if usr["id"] == usuario.get("id"):
            raise HTTPException(status_code=400, detail="el ID ya esta en uso ")
    usuarios.append(usuario)        
    return usuario

#Endpoint actualizar usuraios(put)
@app.put('/usuarios/{id}', tags=['Operaciones CRUD'])
def actualizar(id:int, usuarioActualizado:dict):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index].update(usuarioActualizado)
            return usuarios[index]
    raise HTTPException(status_code=400, detail="El usuario no existe") 


@app.delete('/usuarios/borrar', tags=['Operaciones Crud'])
def eliminar(id:int):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            del usuarios[index]
            return {'Usuario eliminado': usuarios}
    raise HTTPException(status_code=400, detail="El usuario no existe")

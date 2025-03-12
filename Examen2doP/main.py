from fastapi import FastAPI
from fastapi import FastAPI, HTTPException
from typing import Optional,List
from models import ModeloConductor


app = FastAPI()

#Inicio de fastAPI
app = FastAPI(
    title = 'Mi primera API S192' ,
    description = 'Alonso Chávez' ,
    version = '1.0.1'
)

#Mini base estatica
conductores= [
    {"nl": "123456789121","nombre": "Ivan", "tipo": "A"},
    {"nl": "123456789122", "nombre": "Carlos","tipo": "A"},
    {"nl": "123456789123", "nombre": "María", "tipo": "A"},
    {"nl": "123456789124", "nombre": "Lucía", "tipo": "A"},
]

##EndPoint para agregar conductor
@app.post('/agregar/conductor', response_model=ModeloConductor, tags=['Operaciones CRUD'])
def agregarUsuario(conductor:ModeloConductor):
    for usr in conductores:
        if usr["nl"] == conductor.nl:
            raise HTTPException(status_code=400, detail="el numero de licencia ya esta en uso ")
    conductores.append(conductor)        
    return conductor

##EndPont para editar un conductor
@app.put('/conductores/editar/{nl}', response_model= ModeloConductor,tags=['Editar conductor'])
def actualizar(nl:str, conductorActualizado:ModeloConductor):
    for index, usr in enumerate(conductores):
        if usr["nl"] == nl:
            conductores[index].update(conductorActualizado)
            return conductores[index]
    raise HTTPException(status_code=400, detail="El usuario no existe") 
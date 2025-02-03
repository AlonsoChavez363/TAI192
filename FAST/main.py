from fastapi import FastAPI
from typing import Optional

app = FastAPI(
    title="Mi Primer API 192",
    description="Alonso",
    version="1.0.1",
)

usuarios = [
    {"id": 1, "nombre": "Ivan", "edad": 37},
    {"id": 2, "nombre": "Carlos", "edad": 15},
    {"id": 3, "nombre": "María", "edad": 18},
    {"id": 4, "nombre": "Lucía", "edad": 37},
]

# Endpoint home
@app.get("/", tags=["Hola Mundo"])
def home():
    return {"hello": "world FastAPI"}

# Endpoint de promedio
@app.get("/promedio", tags=["Operaciones"])
def promedio():
    return {"promedio": 8.2}

# Endpoint con parámetro obligatorio en la URL
@app.get("/usuario/{id}", tags=["Parámetro Obligatorio"])
def consulta_usuario(id: int):
    for usuario in usuarios:
        if usuario["id"] == id:
            return {"mensaje": "Usuario encontrado", "usuario": usuario}
    return {"mensaje": f"Usuario con id {id} no encontrado"}

@app.get("/usuario", tags=["Parámetro Opcional"])
def consulta_usuario2(id: Optional[int] = None):
    if id is not None:
        for usuario in usuarios:
            if usuario["id"] == id:
                return {"mensaje": "Usuario encontrado", "usuario": usuario}
        return {"mensaje": f"Usuario con id {id} no encontrado"}
    return {"mensaje": "No se proporcionó un id"}
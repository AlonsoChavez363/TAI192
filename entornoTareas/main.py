from fastapi import FastAPI

app = FastAPI(
    title="Api para gestionar Tareas",
    description="Alonso Chávez Alegria",
    version="1.0.2",
)
#crear nuestros registros
tareas = [
    {"id": 1, "titulo": "Estudiar para el examen", "descrpcion": "Estudiar los temas: logistica", "Vencimiento": "14-02-2025", "estado": "En proceso" }
]

#endpoint para obtener tareas
@app.get('/ListarTareas', tags=["Gestionar Tareas"])
def listarTareas():
    return{"Las tareas pendientes son": tareas}

#endpoint para obtener tareas especificas por id

#endpoint para crear tarea

#endpoint para actualizar una tarea existente

#endpoint para eliminar una tarea existente
from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="Api para gestionar Tareas",
    description="Alonso Chávez Alegria",
    version="1.0.2",
)
#crear nuestros registros
tareas = [
    {"id": 1, "titulo": "Crear notas de clase", "descrpcion":"Crear notas de la clase con las diapositivas", "Vencimiento": "8-02-2025", "estado": "Finalizado" },
    {"id": 2, "titulo": "Terminar el trabajo en clase de software", "descrpcion": "Terminar las notas de la presentacion", "Vencimiento": "10-02-2025", "estado": "Finalizado" },
    {"id": 3, "titulo": "Crear una presentacion del PI", "descrpcion": "Crear una presentacion con los temas del PI", "Vencimiento": "12-02-2025", "estado": "En proceso" },
    {"id": 4, "titulo": "Mejorar el PI", "descrpcion": "Mejorar las vistas de admin", "Vencimiento": "22-03-2025", "estado": "En proceso" },
    {"id": 5, "titulo": "Comprar pan", "descrpcion": "Comprar pan", "Vencimiento": "16-02-2025", "estado": "En proceso" },
    {"id": 6, "titulo": "Hacer pierna en el gimnasio", "descrpcion": "Toca pierna", "Vencimiento": "14-02-2025", "estado": "Finalizado" },
    {"id": 7, "titulo": "Estudiar para el examen", "descrpcion": "Estudiar los temas: logistica", "Vencimiento": "14-02-2025", "estado": "En proceso" },
    {"id": 8, "titulo": "Estudiar para el examen", "descrpcion": "Estudiar los temas: logistica", "Vencimiento": "14-02-2025", "estado": "En proceso" },
    {"id": 9, "titulo": "Estudiar para el examen", "descrpcion": "Estudiar los temas: logistica", "Vencimiento": "14-02-2025", "estado": "En proceso" },
    {"id": 10, "titulo": "Estudiar para el examen", "descrpcion": "Estudiar los temas: logistica", "Vencimiento": "14-02-2025", "estado": "En proceso" }



]

#endpoint para obtener tareas
@app.get('/ListarTareas', tags=["Gestionar Tareas"])
def listarTareas():
    return{"Las tareas pendientes son": tareas}

#endpoint para obtener tareas especificas por id
@app.get('/ListarTareas/{id}', tags=['Gestionar Tareas'])
def actualizar(id:int):
    for index, usr in enumerate(tareas):
        if usr["id"] == id:
            return tareas[index]
    raise HTTPException(status_code=400, detail="La tarea no existe") 
    

#endpoint para crear tarea
@app.post('/tareas/', tags=['Agregar Tareas'])
def agregarTarea(tarea:dict):
    for usr in tareas:
        if usr["id"] == tarea.get("id"):
            raise HTTPException(status_code=400, detail="el ID ya esta en uso ")
    tareas.append(tarea)        
    return tarea

#endpoint para actualizar una tarea existente

#endpoint para eliminar una tarea existente
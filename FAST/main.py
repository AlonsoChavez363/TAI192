from fastapi import FastAPI

app = FastAPI(
    title = 'Mi primera API S192' ,
    description = 'Alonso Chávez' ,
    version = '1.0.1'
)

#Endpoint home
@app.get('/')
def home():
    return {'hello':'world FastAPI'}

#endpoint promedio
@app.get('/promedio')
def promedio():
    return 8.2

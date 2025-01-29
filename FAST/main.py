from fastapi import FastAPI

app = FastAPI()

#Endpoint home
@app.get('/')
def home():
    return {'hello':'world FastAPI'}
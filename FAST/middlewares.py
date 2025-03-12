from fastapi import HTTPException, Request
from fastapi.security import HTTPBearer
from genToken import validateToken
class BearerJWT(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)

        data = validateToken(auth.credentials)

        if not isinstance(data, dict): #verificar si es un diccionario valido
            raise HTTPException(status_code=401, detail="Token invalido")
        
        if data.get('correo') != 'alonso@example.com':
            raise HTTPException(status_code=403, detail="Credenciales no validas")
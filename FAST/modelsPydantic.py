from pydantic import BaseModel, Field, EmailStr

#clase
class ModeloUsuario(BaseModel):
    id: int = Field(..., gt=0, description="Id unico y solo numeros positivos")
    nombre :str = Field(..., min_lenght=3, max_lenght=85, description="Solo caracters min:3 y max:85")
    edad:int = Field(..., gt=18, max_lenght=2, description="Nadie tiene mas de 100 años y tienes que tener mas de 18 años")
    correo: EmailStr = Field(..., description="Debe ser un correo electrónico válido")



class modeloAuth(BaseModel):
    correo: EmailStr = Field(..., description="Debe ser un correo electrónico válido", example="example@gmail.com")
    passw: str = Field(..., min_lenght=8,strip_whitespace=True, description= "contraseña minima de 8 caracteres")
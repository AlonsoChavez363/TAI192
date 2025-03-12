from pydantic import BaseModel, Field

#clase
class ModeloConductor(BaseModel):
    nl: str = Field(..., max_lenght=12, description="El numero de licencia debe de tener solo 12 caracteres")
    nombre:str = Field(..., max_lenght=3, description="El nombre debe de tener al menos 3 caracteres")
    tipo:str = Field(..., max_lenght=1, description="El tipo de licencia debe de ser A, B o C")

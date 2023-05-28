from pydantic import BaseModel

class Router(BaseModel):
    id: int
    brand: str
    capacity: str
    antenna: str
    cost: float
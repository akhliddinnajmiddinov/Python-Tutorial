from pydantic import BaseModel

class Human(BaseModel):
    id: int
    name: str


a = Human(id = 1, name = False)
print(a)
### Users API ###

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

# Inicia el server: uvicorn users:app --reload

router = APIRouter(prefix="/users",
                   tags=["users"],
                   responses={404: {"message": "No encontrado"}})


# Entidad user
class User(BaseModel):
    id: int    
    name: str
    surname: str
    url: str
    age: int

users_list = [User(id = 1, name = "Unai", surname = "Munoz", url = "https://moure.dev", age=23),
                User(id = 2, name = "Manolo", surname = "Munfdsafoz", url = "https://moureff.dev", age=13),
                User(id = 3, name = "Alfredo", surname = "GPmaz;p", url = "https://mouraaae.dev", age=21)]

@router.get("/json") 
async def usersjson():
    return [{"name": "Unai", "surname": "Munoz", "url": "https://unaimunoz.dev", "age":23},
            {"name": "Munoz", "surname": "Unai", "url": "https://munozunai.dev", "age":21},
            {"name": "Pascual", "surname": "Unai", "url": "https://pascualunai.dev", "age":34}]


@router.get("/")
async def users():
    return users_list


# Path

@router.get("/{id}")
async def user(id: int):
    return search_user(id)

# Query 

@router.get("/user/")
async def user(id: int): #Es posible llamar también por otro parametro, como nombre. 
    return search_user(id)

@router.post("/user/", response_model=User, status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail= "El usuario ya existe")

    else: 
        users_list.append(user)
        return user

@router.put("/user")
async def user(user: User):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    if not found:
        raise HTTPException(status_code=404, detail= "No se ha actualizado el usuario")
    
    return user

@router.delete("/user/{id}")
async def user(id: int):
    
    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index] 
            found = True
            return{"El usuario ha sido:" "Eliminado."}
    if not found:
        raise HTTPException(status_code=404, detail= "No se ha encontrado el usuario")
    

def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try: 
        return list(users)[0]
    except: 
        raise HTTPException(status_code=304, detail= "No se ha encontrado el usuario")
    


    
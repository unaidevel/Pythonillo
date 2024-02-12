### Users API ###

from fastapi import APIRouter, HTTPException, status
from db.models.user import User
from db.schemas.user import user_schema, users_schema
from db.client import db_client
from bson import ObjectId
# Inicia el server: uvicorn users:app --reload

router = APIRouter(prefix="/userdb",
                   tags=["userdb"],
                   responses={
                       status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})


# Entidad user

users_list = []


@router.get("/", response_model=list[User])
async def users():
    return users_schema[db_client.local.users.find()]

# Path
 
@router.get("/{id}")
async def user(id: str):
    return search_user("_id", ObjectId(id))

# Query 

@router.get("/")
async def user(id: str): #Es posible llamar también por otro parametro, como nombre. 
    return search_user("_id", ObjectId(id))

@router.post("/", response_model=User, status_code=201)
async def user(user: User):
    if type(search_user("email", user.email)) == User:
       raise HTTPException(
           status.HTTP_404_NOT_FOUND, detail= "El usuario ya existe")

    user_dict = dict(user)
    del user_dict["id"]


    id = db_client.local.users.insert_one(user_dict).inserted_id

    new_user = user_schema(db_client.local.users.find_one({"_id":id}))

    return User(**new_user)

@router.put("/")
async def user(user: User):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    if not found:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail= "No se ha actualizado el usuario")
    
    return user

@router.delete("/{id}")
async def user(id: int):
    
    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index] 
            found = True
            return{"El usuario ha sido:" "Eliminado."}
    if not found:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail= "No se ha encontrado el usuario")
    

#Helper

def search_user(field: str, key: str):
    users = filter(lambda user: user.id == id, users_list)
    try: 
        user = user_schema(db_client.local.users.find_one({"_id":id}))
        return User(**user_schema(user))
    except: 
       return {"error": "No se ha encontrado el usuario"}
    


    
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta
ALGORITHM = "HS256"
ACCES_TOKEN_DURATION = 1
SECRET = "0378071d42472b255e9a73186e2ff7457c1aa495b1848fe00f71d7fbad4ada71"

router = APIRouter()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt = CryptContext(schemes=["bcrypt"])

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool

class UserDB(User):
    password: str

users_db = {
    "unaimunoz": {
        "username": "unaimunoz",
        "full_name": "Unai Munoz",
        "email": "unaimunozpascual@gmail.com",
        "disabled": False,
        "password": "$2a$12$wzDxjAiP9XdFqKYmMOnCieG3Hu9I42xHZSmALzUBMKJYB58vOggA6"
    },
    "unaimunoz2": {
        "username": "unaimunoz2",
        "full_name": "Unai Munoz2",
        "email": "unaimunozpascual2@gmail.com",
        "disabled": True,
        "password": "$2a$12$5Wxk2Iz8PCazaMajRqsyu.MYKR5Fl.vrUQaXo1gmVFeHA5wDuyiZq"
    }
}

def search_user_db(username:str):
    if username in users_db:
        return UserDB(**users_db[username])

async def auth_user(token: str = Depends(oauth2)):
    exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail= "Credenciales de autenticación inválidas",
            headers={"WWW-Authenticate": "Bearer"})
    
    try: 
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise exception
    except JWTError:
        raise exception
    

async def current_user(user: User = Depends(auth_user)):     
    if user.disabled: 
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail= "Usuario inactivo")
    
    return user

def search_user(username:str):
    if username in users_db:
        return User(**users_db[username])


@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail= "El usuario no es correcto")
    
    user = search_user_db(form.username)

    if not crypt.verify(form.password, user.password): 
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail= "La contrasena no es correcta")
    
    access_token = {"sub": user.username, 
                    "exp": datetime.utc() + timedelta(minutes = ACCES_TOKEN_DURATION)}

    return {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM), "token_type": "bearer"}


@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user
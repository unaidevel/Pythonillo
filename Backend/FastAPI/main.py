### Hola mundo ###

# Docuemntación oficial: https://fastapi.tiangolo.com/es/

# Instala FastAPI: pip install "fastapi[all]"

from fastapi import FastAPI
from routers import products, users, basic_auth_users, jwt_auth_users, users_db
from fastapi.staticfiles import StaticFiles
app = FastAPI()


# Routers

app.include_router(products.router)
app.include_router(users.router)
app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)
app.include_router(users_db)


app.mount("/static", StaticFiles(directory="static"), name = "static")

# Url local: http://127.0.0.1:8000

@app.get("/") #la barra es la raiz de la ip donde se está desplegando la api
async def root():
    return {"message": "Hola FastAPI!"} 

# Url local: http://127.0.0.1:8000/url

@app.get("/url") #la barra es la raiz de la ip donde se está desplegando la api
async def url():
    return {"url_curso": "https://mourdev.com/python"} 


# Inicia el server: uvicorn main:app --reload
# Detener el server: CTRL+C

# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc
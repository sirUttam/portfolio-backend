from fastapi import FastAPI
from app.routes import hero, auth

app = FastAPI()

app.include_router(router=hero.router)
app.include_router(router=auth.router)

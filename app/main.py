from fastapi import FastAPI
from app.routes import hero, auth, about, skills

app = FastAPI()

app.include_router(router=hero.router)
app.include_router(router=auth.router)
app.include_router(router=about.router)
app.include_router(router=skills.router)

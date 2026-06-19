from fastapi import FastAPI
from app.routes import hero, auth, about
from app.routes.skills import categories, items

app = FastAPI()

app.include_router(router=hero.router)
app.include_router(router=auth.router)
app.include_router(router=about.router)
app.include_router(router=categories.router)
app.include_router(router=items.router)


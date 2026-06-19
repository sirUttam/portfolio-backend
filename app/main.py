from fastapi import FastAPI
from app.routes import hero, auth, about
from app.routes.skills import categories, items
from app.routes.projects import project, project_links, project_tools
import app.models

app = FastAPI()

app.include_router(router=hero.router)
app.include_router(router=auth.router)
app.include_router(router=about.router)
app.include_router(router=categories.router)
app.include_router(router=items.router)
app.include_router(router=project.router)
app.include_router(router=project_links.router)
app.include_router(router=project_tools.router)



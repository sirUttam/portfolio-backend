from fastapi import FastAPI
from app.routes import hero, auth, about
from app.routes.skills import categories, items
from app.routes.projects import project, project_links, project_tools
import app.models
from app.routes import journey
from app.routes.contact import contact_form
from app.routes.contact import contact_links
from app.routes import footer
from app.routes import navbar

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.include_router(router=hero.router)
app.include_router(router=auth.router)
app.include_router(router=about.router)
app.include_router(router=categories.router)
app.include_router(router=items.router)
app.include_router(router=project.router)
app.include_router(router=project_links.router)
app.include_router(router=project_tools.router)
app.include_router(router=journey.router)
app.include_router(router=contact_links.router)
app.include_router(router=contact_form.router)
app.include_router(router=footer.router)
app.include_router(router=navbar.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)






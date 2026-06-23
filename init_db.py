from app.models.admin import Admin
from app.models.hero import Hero
from app.database import Base, engine
from app.models.about import About, AboutCard
from app.models.skills.categories import SkillsCategory
from app.models.skills.items import SkillsItems
from app.models.projects.project import Project
from app.models.projects.project_links import ProjectLinks
from app.models.projects.project_tools import ProjectTools
from app.models.journey import Journey
from app.models.contact.contact_form import ContactForm
from app.models.contact.contact_links import ContactLinks


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)
# Base.metadata.create_all(bind=engine)
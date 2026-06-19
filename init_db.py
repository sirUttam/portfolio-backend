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




Base.metadata.create_all(bind=engine)
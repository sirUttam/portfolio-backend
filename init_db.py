from app.models.admin import Admin
from app.models.hero import Hero
from app.database import Base, engine
from app.models.about import About, AboutCard
from app.models.skills.categories import SkillsCategory
from app.models.skills.items import SkillsItems




Base.metadata.create_all(bind=engine)
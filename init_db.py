from app.models.admin import Admin
from app.models.hero import Hero
from app.database import Base, engine
from app.models.about import About, AboutCard



Base.metadata.create_all(bind=engine)
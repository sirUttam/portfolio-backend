from app.models.admin import Admin
from app.models.hero import Hero
from app.database import Base, engine



Base.metadata.create_all(bind=engine)
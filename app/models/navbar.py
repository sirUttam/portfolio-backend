from sqlalchemy import Column, String, Integer
from app.database import Base


class SiteSettings(Base):
    __tablename__ = "site_settings"

    id = Column(Integer, primary_key=True)

    logo_url = Column(String, nullable=True)
    site_name = Column(String, nullable=False)
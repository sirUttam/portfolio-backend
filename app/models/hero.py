from sqlalchemy import Column, String, Integer
from app.database import Base


class Hero(Base):
    __tablename__ = "hero_table"
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    subtitle = Column(String)
    description = Column(String)
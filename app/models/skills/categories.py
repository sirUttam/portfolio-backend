from app.database import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

class SkillsCategory(Base):
    __tablename__ = "skills_category"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    
    items = relationship("SkillsItems", back_populates="category")
    
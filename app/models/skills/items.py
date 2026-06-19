from app.database import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

    
class SkillsItems(Base):
    __tablename__ = "skills_items"

    id = Column(Integer, primary_key=True)
    icon = Column(String)
    title = Column(String)
    category_id = Column(Integer, ForeignKey("skills_category.id"))  # foreign key
    
    category = relationship("SkillsCategory", back_populates="items")
    
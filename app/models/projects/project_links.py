from sqlalchemy import Column, String, Integer, ForeignKey
from app.database import Base
from sqlalchemy.orm import relationship
from app.models.base import TimeStampMixin



class ProjectLinks(Base, TimeStampMixin):
    __tablename__ = "project_links"
    
    id = Column(Integer, primary_key=True)
    type = Column(String, nullable=False)
    url = Column(String, nullable=False)
    
    project_id = Column(Integer, ForeignKey("project.id"))

    project = relationship("Project", back_populates="links", lazy="selectin")

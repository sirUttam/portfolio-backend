from sqlalchemy import Column, String, Integer, ForeignKey
from app.database import Base
from sqlalchemy.orm import relationship
from app.models.base import TimeStampMixin


class ProjectTools(Base, TimeStampMixin):
    __tablename__ = "project_tools"
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    
    project_id = Column(Integer, ForeignKey("project.id"))

    project = relationship("Project", back_populates="tools", lazy="selectin")

    
    
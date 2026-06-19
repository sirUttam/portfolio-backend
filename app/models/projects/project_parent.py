from sqlalchemy import Column, String, Integer, Text
from app.database import Base
from sqlalchemy.orm import relationship


class Project(Base):
    __tablename__ = "project"
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    
    tools = relationship("ProjectTools", back_populates="project")
    links = relationship("ProjectLinks", back_populates="project")

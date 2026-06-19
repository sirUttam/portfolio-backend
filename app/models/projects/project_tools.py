from sqlalchemy import Column, String, Integer, ForeignKey
from app.database import Base
from sqlalchemy.orm import relationship


class ProjectTools(Base):
    __tablename__ = "project_tools"
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    
    project_id = Column(Integer, ForeignKey("project.id"))

    project = relationship("Project", back_populates="tools", cascade="all, delete")

    
    
    
#     created_at = Column(DateTime, default=datetime.utcnow)
# updated_at = Column(DateTime, onupdate=datetime.utcnow)

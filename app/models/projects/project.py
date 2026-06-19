from sqlalchemy import Column, String, Integer, Text, DateTime
from app.database import Base
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.models.base import TimeStampMixin


class Project(Base, TimeStampMixin):
    __tablename__ = "project"
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    
    # created_at = Column(DateTime, default= lambda: datetime.now(timezone.utc))
    # updated_at = Column(DateTime, onupdate=lambda: datetime.now(timezone.utc))
    
    tools = relationship("ProjectTools", back_populates="project", cascade="all, delete")
    links = relationship("ProjectLinks", back_populates="project", cascade="all, delete")

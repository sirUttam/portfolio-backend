from sqlalchemy import Column, String, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Journey(Base):
    __tablename__ = "journey"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    subtitle = Column(String, nullable=False)
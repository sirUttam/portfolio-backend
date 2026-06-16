from app.database import Base
from sqlalchemy import Column, String, Integer

class Admin(Base):
    __tablename__ = "admin"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String, nullable=False)
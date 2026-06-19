from sqlalchemy import Column, String, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from app.models.base import TimeStampMixin


class ContactLinks(Base, TimeStampMixin):
    __tablename__ = "contact_links"

    id = Column(Integer, primary_key=True)
    icon = Column(String, nullable=False)
    title = Column(String, nullable=False)
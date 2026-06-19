from sqlalchemy import Column, String, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from app.models.base import TimeStampMixin


class ContactForm(Base, TimeStampMixin):
    __tablename__ = "contact_form"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    message = Column(Text)
from sqlalchemy import Column, String, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class About(Base):
    __tablename__ = 'about_table'

    id = Column(Integer, primary_key=True)

    # left side
    about_title = Column(Text, nullable=False)
    subtitle = Column(String, nullable=True)

    # right side
    image_url = Column(String, nullable=False)
    right_text = Column(String, nullable=True)
    
    cards = relationship("AboutCard", back_populates='about')


class AboutCard(Base):
    __tablename__ = "about_cards"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)

    about_id = Column(Integer, ForeignKey("about_table.id"))   # Foreign Key
    
    about = relationship("About", back_populates="cards")

    
    
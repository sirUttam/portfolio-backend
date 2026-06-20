from sqlalchemy import Column, String, Integer, Text
from app.database import Base


class Footer(Base):
    __tablename__ = "footer"

    id = Column(Integer, primary_key=True)

    title = Column(String, nullable=False)
    subtitle = Column(String, nullable=False)
    copyright_text = Column(Text, nullable=False)
    url = Column(String, nullable=False)
from sqlalchemy import Column, Integer, String, Text
from db.db import Base

class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)

    image_url = Column(String(500), nullable=False)

    width = Column(Integer, nullable=True)
    height = Column(Integer, nullable=True)
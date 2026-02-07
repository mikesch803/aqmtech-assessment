from sqlalchemy import Column, Integer, String, Text
from db import Base

class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    file_path = Column(String(255), nullable=False)
    width = Column(Integer)
    height = Column(Integer)
    image_url = Column(String(500)) 

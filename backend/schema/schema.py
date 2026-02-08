from pydantic import BaseModel, HttpUrl
from typing import Optional

class ImageCreate(BaseModel):
    title: str
    description: Optional[str] = None
    image_url: HttpUrl

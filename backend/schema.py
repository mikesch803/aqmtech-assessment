from pydantic import BaseModel

class ImageSchema(BaseModel):
    id: int
    title: str
    description: str | None
    file_path: str
    width: int | None
    height: int | None

    class Config:
        orm_mode = True

import os
from fastapi import Depends, FastAPI, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from fastapi.staticfiles import StaticFiles
from sqlalchemy import text
from dotenv import load_dotenv
load_dotenv()
from util import upload_image_to_s3
from model import Image


from db import SessionLocal, engine

app = FastAPI()

app.mount("/images", StaticFiles(directory="images"), name="images")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/db_check")
def db_check():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            return {"db_status": "connected", "result": result.scalar()}
    except Exception as e:
        return {"db_status": "failed", "error": str(e)}

@app.get("/")
def health_check():
    return {"status": "ok"}

@app.post("/api/images/upload")
def upload_image(
    title: str,
    description: str | None = None,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    image_url = upload_image_to_s3(file)

    new_image = Image(
        title=title,
        description=description,
        file_path=file.filename,
        width=None,
        height=None,
        image_url=image_url,
    )

    db.add(new_image)
    db.commit()
    db.refresh(new_image)

    return {
        "id": new_image.id,
        "title": new_image.title,
        "image_url": new_image.image_url,
    }


@app.get("/api/images")
def get_images(db: Session = Depends(get_db)):
    return db.query(Image).all()

@app.get("/api/images/{image_id}")
def get_image(image_id: int, db: Session = Depends(get_db)):
    image = db.query(Image).filter(Image.id == image_id).first()
    if not image:
        raise HTTPException(status_code=404, detail="Image not found")
    return image




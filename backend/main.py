from schema.schema import ImageCreate
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from dotenv import load_dotenv
load_dotenv()
from model.model import Image
from db.db import Base, SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)
# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (for development only)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

@app.post("/api/images")
def create_image(
    payload: ImageCreate,
    db: Session = Depends(get_db),
):
    new_image = Image(
        title=payload.title,
        description=payload.description,
        image_url=str(payload.image_url),
        width=None,
        height=None,
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




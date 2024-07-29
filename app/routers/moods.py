from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud, models, schemas
from ..database import get_db
from ..auth import get_current_user

router = APIRouter()

@router.post("/moods/", response_model=schemas.Mood)
def create_mood(mood: schemas.MoodCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return crud.create_mood(db=db, mood=mood, user_id=current_user.id)

@router.get("/moods/", response_model=List[schemas.Mood])
def read_moods(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    moods = crud.get_moods(db, user_id=current_user.id, skip=skip, limit=limit)
    return moods

@router.get("/moods/{mood_id}", response_model=schemas.Mood)
def read_mood(mood_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    db_mood = crud.get_mood(db, mood_id=mood_id)
    if db_mood is None or db_mood.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Mood not found")
    return db_mood
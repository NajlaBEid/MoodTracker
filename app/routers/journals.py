from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud, models, schemas
from ..database import get_db
from ..auth import get_current_user

router = APIRouter()

@router.post("/journals/", response_model=schemas.Journal)
def create_journal(journal: schemas.JournalCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return crud.create_journal(db=db, journal=journal, user_id=current_user.id)

@router.get("/journals/", response_model=List[schemas.Journal])
def read_journals(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    journals = crud.get_journals(db, user_id=current_user.id, skip=skip, limit=limit)
    return journals

@router.get("/journals/{journal_id}", response_model=schemas.Journal)
def read_journal(journal_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    db_journal = crud.get_journal(db, journal_id=journal_id)
    if db_journal is None or db_journal.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Journal not found")
    return db_journal
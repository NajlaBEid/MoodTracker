from sqlalchemy.orm import Session
from . import models, schemas
from .auth import get_password_hash


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def create_mood(db: Session, mood: schemas.MoodCreate, user_id: int):
    db_mood = models.Mood(**mood.dict(), user_id=user_id)
    db.add(db_mood)
    db.commit()
    db.refresh(db_mood)
    return db_mood


def get_moods(db: Session, user_id: int, skip: int = 0, limit: int = 10):
    return db.query(models.Mood).filter(models.Mood.user_id == user_id).offset(skip).limit(limit).all()


def get_mood(db: Session, mood_id: int):
    return db.query(models.Mood).filter(models.Mood.id == mood_id).first()


def create_journal(db: Session, journal: schemas.JournalCreate, user_id: int):
    db_journal = models.Journal(**journal.dict(), user_id=user_id)
    db.add(db_journal)
    db.commit()
    db.refresh(db_journal)
    return db_journal


def get_journals(db: Session, user_id: int, skip: int = 0, limit: int = 10):
    return db.query(models.Journal).filter(models.Journal.user_id == user_id).offset(skip).limit(limit).all()


def get_journal(db: Session, journal_id: int):
    return db.query(models.Journal).filter(models.Journal.id == journal_id).first()
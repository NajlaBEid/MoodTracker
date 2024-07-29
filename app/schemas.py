
from typing import List, Optional
from pydantic import BaseModel

# User schemas
class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True


# Mood schemas
class MoodBase(BaseModel):
    mood: str
    description: Optional[str] = None

class MoodCreate(MoodBase):
    pass

class Mood(MoodBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


# Journal schemas
class JournalBase(BaseModel):
    title: str
    content: str

class JournalCreate(JournalBase):
    pass

class Journal(JournalBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


# Token schemas
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
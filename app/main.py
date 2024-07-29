from fastapi import FastAPI
from .database import engine, Base
from .routers import moods, journals, auth
import schedule
import time
import threading

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(moods.router)
app.include_router(journals.router)



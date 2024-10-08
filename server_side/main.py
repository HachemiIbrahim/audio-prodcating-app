from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from auth import authentication
from database import Base, engine
from routers import song, user

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(song.router)

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

from fastapi import FastAPI
from router.movie import movie_router
from app.database import create_table

app = FastAPI()

app.include_router(movie_router)

create_table()
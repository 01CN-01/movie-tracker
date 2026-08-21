from pydantic import BaseModel

class MovieCreate(BaseModel):
    movie_name: str
    genre: str

class MovieDelete(BaseModel):
    movie_name: str
    genre: str | None = None
    
class MovieResponse(BaseModel):
    movie_id: int
    movie_name: str
    genre: str

class MovieUpdate(BaseModel):
    movie_name: str
    new_movie_name: str | None = None
    genre: str | None = None
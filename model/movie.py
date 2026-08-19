from pydantic import BaseModel

class MovieCreate(BaseModel):
    movie: str
    genre: str
    
class MovieResponse(BaseModel):
    movie_id: int
    movie_name: str
    genre: str
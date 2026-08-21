from fastapi import APIRouter, HTTPException
from model.movie import MovieCreate, MovieDelete, MovieResponse, MovieUpdate
from app.database import add_movie, count_movie, view_all, filtered_movie, find_to_update_movie, update_movie, delete_specific_movie

movie_router = APIRouter(prefix = "/movie")
# Add Movie ...........
# View All ...........
# Search / Filter ......    
# Update .......
# Delete
@movie_router.post("/add-movie")
def create_movie(movie: MovieCreate):
    count = count_movie(movie.movie_name) # Does movie exits in database?
    
    if count > 0:
        return {"message": "Movie already exists"}
    else:
        add_movie(movie.movie_name, movie.genre)
        return {"message": "Movie added successfully"}


@movie_router.get("/view-all-movies", response_model=list[MovieResponse])
def view_movie():
    all_movies = view_all()
    
    results = []
    
    for movie in all_movies:
        results.append(dict(movie))
    
    return results

@movie_router.post("/filter-movie", response_model=list[MovieResponse])
def filter_movies(movie: MovieCreate):
    filtered_data = filtered_movie(movie.movie_name, movie.genre)

    results = []
    
    for movie in filtered_data:
        results.append(dict(movie))
    
    return results

@movie_router.post("/update-movie")
def updated_movie(movie: MovieUpdate):
    movie_id = find_to_update_movie(movie.movie_name) # Finds ID for movie
    
    if not movie_id:
        return {"message": "Unable to find movie"}
    else:
        update_movie(movie.new_movie_name, movie.genre, movie_id) #Updates movie once given the movie_ID
        return {"message": "Successfully updated movie"}

@movie_router.post("/delete-movie")
def delete_movie(movie: MovieDelete):
    movie_id = find_to_update_movie(movie.movie_name)
    
    if not movie_id:
        return {"message": "Unable to find movie"}
    else:
        delete_specific_movie(movie_id)
        return {"message": "Successfully deleted movie"}
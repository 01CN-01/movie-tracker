import sqlite3

def get_connection():
    conn = sqlite3.connect("data/movies.db")
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS movies(
            movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
            movie_name TEXT NOT NULL,
            genre TEXT NOT NULL
        )
        """)
    
    conn.commit()
    conn.close()

def add_movie(movie_name, genre):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        """
        INSERT INTO movies (movie_name, genre)
        VALUES(?, ?)
        """,
        (movie_name, genre) 
    )
    
    conn.commit()
    conn.close()
    
def count_movie(movie_name):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        """
        SELECT COUNT(*) FROM movies
        WHERE movie_name LIKE ?
        """,
        (movie_name,)
        )
    
    count = cursor.fetchone()[0]
    conn.close()
    
    return count

def view_all():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        """
        SELECT * FROM movies
        """)
    movies = cursor.fetchall()
    conn.close()
    
    return movies

def filtered_movie(movie_name, genre):
    conn = get_connection()
    cursor = conn.cursor()
    
    query = "SELECT * FROM movies WHERE 1=1"
    params = []
    
    if movie_name:
        query += " AND movie_name LIKE ?"
        params.append(movie_name)
    
    if genre:
        query += " AND genre LIKE ?"
        params.append(genre)
    
    cursor.execute(query, params)
    
    filtered_data = cursor.fetchall()
    conn.close()
    
    return filtered_data

def find_to_update_movie(movie_name):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        """
        SELECT * FROM movies
        WHERE movie_name = ?
        """,
        (movie_name,))
    movie = cursor.fetchone()
    
    conn.close()
    
    if not movie:
        return False
    
    movie_id = movie[0]
    
    return movie_id

def update_movie(new_movie_name, genre, movie_id):
    conn = get_connection()
    cursor = conn.cursor()
    
    query = "UPDATE movies SET"
    params = []
    
    if new_movie_name:
        query += " movie_name = ?"
        params.append(new_movie_name)
    
    if genre:
        if new_movie_name:
            query += ","
        
        query += " genre = ?"
        params.append(genre)
    
    query += " WHERE movie_id = ?"
    params.append(movie_id)
    
    cursor.execute(query, params)
    conn.commit()
    
    conn.close()
        

    
    
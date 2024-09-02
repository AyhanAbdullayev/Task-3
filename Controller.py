from flask import render_template
from Models import Movie
from Web_app import Web_app



@Web_app.route("/Movies/")

def index():
    movie = Movie.query.all()
    return render_template("index.html",movie=movie)


@Web_app.route('/Movies/<int:movie_id>/')

def get_Movie(movie_id):
    movie = Movie.query.get(movie_id) 
    all_movie = Movie.query.all()
    Message = None
    if movie_id <= 0 or movie_id > len(all_movie) :
        Message = "Movie Not Found "
        return Message
    return render_template("movie.html",movie=movie)

    
    

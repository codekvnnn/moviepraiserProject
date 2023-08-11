# flask_app/views/movie.py
from flask import render_template, request
from flask_app.services.movie_api import get_movie_details_by_title
from flask_app.models.movie import MovieSearchForm

@app.route("/movies/search", methods=['GET', 'POST'])
def search_movies():
    form = MovieSearchForm(request.form)
    if request.method == 'POST' and form.validate():
        movie_title = form.title.data
        movie_data = get_movie_details_by_title(movie_title)
        if movie_data:
            return render_template('movie_search_results.html', movies=movie_data['results'])
        else:
            flash('Error: Unable to fetch movie details from the API.', 'danger')
    return render_template('movie_search.html', form=form)

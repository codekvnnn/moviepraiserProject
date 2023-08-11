# flask_app/controllers/movie.py
from flask_app import app
from flask import render_template, request, redirect, url_for, session
from flask_app.models.movie import Movie, Comment
from flask_app.models.user import User
import requests
from datetime import datetime


# Route to display the search form
@app.route('/search')
def search():
    return render_template('movie_search.html')

# Route to handle the form submission and display search results
@app.route('/movies', methods=['POST'])
def show_movies():
    if "user_id" not in session: 
        return redirect('/login') 
    title = request.form['title']
    api_key = "a12f4bb0fa2da473c2910053c7ae4e5a"
    url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={title}"
    response = requests.get(url)
    data = response.json()

    results = []
    for i in data["results"]:
        movie_data = {
            "title": i.get('original_title', 'Title Not Found'),
            "release_year": i.get('release_date', 'Release Year Not Found'),
            "poster_path": i.get('poster_path', None),
            "genre": i.get('genre_ids', []),
            "rating": i.get('popularity', 0),
            "id": i.get('id', 0),
            "overview": i.get('overview', 'Overview Not Found')
        }
        movie = Movie(movie_data)
        results.append(movie)

    return render_template('movie_search_results.html', movies=results)

# Route to display detailed information about a single movie
@app.route('/movies/<int:id>')
def show_movie(id):
    if "user_id" not in session: 
        return redirect('/login') 
    api_key = "a12f4bb0fa2da473c2910053c7ae4e5a"
    url = f"https://api.themoviedb.org/3/movie/{id}?api_key={api_key}"
    response = requests.get(url)
    data = response.json()

    # Check if the 'original_title' key exists in the API response
    if 'original_title' in data:
        title = data['original_title']
    else:
        # If the key doesn't exist, set the title to a default value or handle the error accordingly
        title = "Title Not Found"

    # Create the movie data dictionary with the correct title
    movie_data = {
        "title": title,
        "release_year": data.get('release_date', 'Release Year Not Found'),
        "poster_path": data.get('poster_path', None),
        "genre": data.get('genre_ids', []),
        "rating": data.get('popularity', 0),
        "id": data.get('id', 0),
        "overview": data.get('overview', 'Overview Not Found')
    }
    movie = Movie(movie_data)

    # Fetch comments for the movie
    comments = Comment.get_comments_by_movie_id(id)
    print(comments)

    return render_template('one_movie.html', movie=movie, user_id = session['user_id'],  comments=comments)

@app.route('/add_comment/<int:movie_id>', methods=['POST'])
def add_comment(movie_id):
    if "user_id" not in session: 
        return redirect('/login') 
    user = User.get_by_id({"id":session["user_id"]})
    Comment.save(request.form, user.first_name, movie_id)

    return redirect(f'/movies/{movie_id}')

@app.route('/edit_comment/<int:comment_id>', methods=['GET', 'POST'])
def edit_comment(comment_id):
    if "user_id" not in session: 
        return redirect('/login') 
    comment = Comment.get_by_id(comment_id)

    if not comment:
        # Handle the case where the comment doesn't exist
        # You can choose to display an error message here if you want
        return redirect(url_for('show_movie', id=comment_id))

    if request.method == 'POST':
        # Get the updated content from the form
        updated_content = request.form['content']

        # Update the comment content in the database
        comment.content = updated_content
        comment.update(request.form)

        # Redirect back to the movie detail page
        return redirect(url_for('show_movie', id=comment.movie_id))

    return render_template('edit_comment.html', comment=comment)

@app.route('/edit_comment/<int:comment_id>', methods=['GET', 'POST'])
def edit_comment_view(comment_id):
    if "user_id" not in session: 
        return redirect('/login') 
    # Fetch the comment by comment_id
    comment = Comment.get_by_id(comment_id)

    if not comment:
        # Handle the case where the comment doesn't exist
        # You can choose to display an error message here if you want
        return redirect(url_for('show_movie', id=comment_id))

    if request.method == 'POST':
        # Get the updated content from the form
        updated_content = request.form['content']

        # Update the comment content in the database
        comment.content = updated_content
        comment.save()

        # Redirect back to the movie detail page
        return redirect(url_for('show_movie', id=comment.movie_id))

    return render_template('edit_comment.html', comment=comment)



@app.route('/delete_comment/<int:comment_id>', methods=['GET', 'POST'])
def delete_comment(comment_id):
    if "user_id" not in session: 
        return redirect('/login') 
    # Fetch the comment by comment_id
    comment = Comment.get_by_id(comment_id)

    if not comment:
        # If the comment doesn't exist, redirect to the movie detail page
        # You can choose to display an error message here if you want
        return redirect(url_for('show_movie', id=comment_id))

    # Delete the comment from the database
    comment.delete()

    # Redirect back to the movie detail page using the movie_id stored in the comment
    return redirect(url_for('show_movie', id=comment.movie_id))
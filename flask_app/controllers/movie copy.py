# # flask_app/controllers/movie.py
# # flask_app/controllers/movie.py
# from flask_app import app
# from flask import render_template, request
# from flask_app.models.movie import Movie  # Update the import statement
# import json
# import requests


# @app.route('/search')
# def search():
#     # Logic to fetch and display movie data from the database
#     # movies = Movie.get_all()  # Use the 'Movie' model to fetch movies from the database
#     return render_template('movie_search.html')


# @app.route('/movies',  methods=['POST'])
# def show_movies(): 
#     data = requests.get(f"https://api.themoviedb.org/3/search/movie?api_key=a12f4bb0fa2da473c2910053c7ae4e5a&query={request.form['title']}")
#     print(data.json())
#     results = []
#     for i in data.json()["results"]:
#         data = {
#             "title": i ['original_title'],
#             "release_year": i ['release_date'],
#             "poster_path": i ['poster_path'],
#             "genre": i ['genre_ids'],
#             "rating": i ['popularity'],
#             "id": i ['id'],  
#             "overview": i ['overview']      
#         }
#         x = Movie(data)
#         print(x.title)
#         results.append(x)
#     # movies = Movie.get_all() 
#     print(results)
#     return render_template('movie_search_results.html', movies=results)

# @app.route('/movies/<id>')
# def show_movie(id): 
#     data = requests.get(f"https://api.themoviedb.org/3/search/movie?api_key=a12f4bb0fa2da473c2910053c7ae4e5a&query={id}")
#     print(data.json())
#     i = data.json()["results"][]
#     data = {
#         "title": i ['original_title'],
#         "release_year": i ['release_date'],
#         "poster_path": i ['poster_path'],
#         "genre": i ['genre_ids'],
#         "rating": i ['popularity'],
#         "id": i ['id'], 
#         "overview": i ['overview']        
#     }
#     x = Movie(data)
#     print(x.title)
    
#     return render_template('one_movie.html', movie=x)


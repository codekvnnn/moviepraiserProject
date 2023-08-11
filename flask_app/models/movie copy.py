# # flask_app/models/movie.py
# from flask_app.config.mysqlconnection import connectToMySQL

# class Movie:
#     def __init__(self, data):
#         self.id = data['id']
#         self.title = data['title']
#         self.poster_path = data['poster_path']
#         self.release_year = data['release_year']
#         self.genre = data['genre']
#         self.rating = data['rating']
#         self.overview = data['overview']
        
        
#     @classmethod
#     def get_all(cls):
#         query = """
#             SELECT * FROM movies;
#         """
#         results = connectToMySQL('movie').query_db(query)
#         movies = []
#         for movie in results:
#             movies.append(cls(movie))
#         return movies

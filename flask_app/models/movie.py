# # flask_app/models/movie.py
# from flask_app.config.mysqlconnection import connectToMySQL
# from datetime import datetime

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

# class Comment:
#     def __init__(self, data, comment_id=None):
#         self.id = comment_id    
#         self.content = data['content']
#         self.author = data['author']
#         self.timestamp = data['timestamp']
#         self.movie_id = data['movie_id']
        
#     @classmethod
#     def get_comments_by_movie_id(cls, movie_id):
#         query = """
#             SELECT * FROM comments
#             WHERE movie_id = %(movie_id)s;
#         """
#         data = {
#             'movie_id': movie_id
#         }
#         results = connectToMySQL('movie').query_db(query, data)
#         comments = []
#         for comment in results:
#             comments.append(cls(comment))
#         return comments

#     def save(self):
#         query = """
#             INSERT INTO comments (content, author, timestamp, movie_id)
#             VALUES (%(content)s, %(author)s, %(timestamp)s, %(movie_id)s);
#         """
#         data = {
#             'content': self.content,
#             'author': self.author,
#             'timestamp': self.timestamp.strftime('%Y-%m-%d %H:%M:%S'), 
#             'movie_id': self.movie_id
#         }
#         self.id = connectToMySQL('movie').query_db(query, data)

# flask_app/models/movie.py
from flask_app.config.mysqlconnection import connectToMySQL
from datetime import datetime
from flask import session

class Movie:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.poster_path = data['poster_path']
        self.release_year = data['release_year']
        self.genre = data['genre']
        self.rating = data['rating']
        self.overview = data['overview']
        
    @classmethod
    def get_all(cls):
        query = """
            SELECT * FROM movies;
        """
        results = connectToMySQL('movie').query_db(query)
        movies = []
        for movie in results:
            movies.append(cls(movie))
        return movies

class Comment:
    def __init__(self, data):
        self.id = data['id']  # Use comment_id if provided, otherwise it will be None for new comments
        self.content = data['content']
        self.author = data['author']
        self.user_id = data['user_id']
        self.movie_id = data['movie_id']
        
    @classmethod
    def get_comments_by_movie_id(cls, movie_id):
        query = """
            SELECT * FROM comments
            WHERE movie_id = %(movie_id)s;
        """
        data = {
            'movie_id': movie_id
        }
        results = connectToMySQL('movie').query_db(query, data)
        print(results)
        comments = []
        for comment in results:
            print(comment)
            comments.append(cls(comment))
        return comments

    @classmethod
    def save(cls, data, author,movie_id):
        query = """
                INSERT INTO comments (content, author, user_id, movie_id)
                VALUES (%(content)s, %(author)s, %(user_id)s, %(movie_id)s);
            """
        data = {
            'content': data['content'],
            'author': author,
            'movie_id': movie_id,
            'user_id': session['user_id']
        }
        return connectToMySQL('movie').query_db(query, data)

    @classmethod
    def update(cls, data):
        query = """
                UPDATE comments 
                SET content = %(content)s
                WHERE id = %(id)s;
            """
    
        return connectToMySQL('movie').query_db(query, data)

    def delete(self):
        query = """
            DELETE FROM comments
            WHERE id = %(comment_id)s;
        """
        data = {
            'comment_id': self.id
        }
        connectToMySQL('movie').query_db(query, data)

    @classmethod
    def get_by_id(cls, comment_id):
        query = """
            SELECT * FROM comments
            WHERE id = %(comment_id)s;
        """
        data = {
            'comment_id': comment_id
        }
        result = connectToMySQL('movie').query_db(query, data)
        if result:
            return cls(result[0])
        return None

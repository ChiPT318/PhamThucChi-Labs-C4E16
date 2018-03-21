from pymongo import MongoClient

mongo_URI = "mongodb://Admin:phamthucchi318@ds215759.mlab.com:15759/c4e16"

# 1. connect to database
client = MongoClient(mongo_URI)

# 2. Get database
db = client.get_default_database()

#3. Create collection
# games = db["games"]
movies = db["movies"]

# # 4. Create a new document
#
# movie_list = ["Up", "Time's up", "Call me by your name", "Love actually"]
# movie_description = ["Pixar", "Timberlake", "Gay rom", "Romcom"]
#
# for i in range(len(movie_list)):
#     new_movie = {"name": movie_list[i], "description": movie_description[i]}
# # 5. Insert documentinto collection

    # movies.insert_one(new_movie)

all_movies = movies.find()
for movie in all_movies:
    print(movie)

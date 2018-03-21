from pymongo import MongoClient

mongo_URI = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(mongo_URI)

db = client.get_default_database()

posts = db["posts"]

blog_post = {"title":"Blog post", "author" : "Worst student eva", "content": "Please work, please work, please work"}
posts.insert_one(blog_post)

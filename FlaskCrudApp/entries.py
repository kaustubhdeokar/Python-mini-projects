from pymongo import MongoClient


def establish_connection():
    cluster = MongoClient(
        "mongodb+srv://kaustubh:kaustubh@cluster0.axdxy.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = cluster["nursery"]
    return db["seeds"]


def fetch_entries():
    collection = establish_connection()
    return collection.find()


def insert_into_collection(username, password):
    collection = establish_connection()
    collection.insert_one({"_id": username, "password": password})
    print(collection.count())


def delete_all_having(username, password):
    collection = establish_connection()
    collection.delete_many({"one": 1, "two": 2})


def drop_table():
    collections = establish_connection()
    collections.drop()
    return None


def update_user(user):
    collections = establish_connection()
    collections.update_one({"_id": user}, { "$set": {"password": "newpassword"}})


def delete_user(user):
    collections = establish_connection()
    collections.delete_one({"_id": user})

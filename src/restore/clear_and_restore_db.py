import pymongo
from pymongo.collection import Collection
import subprocess


def clear_and_restore() :
    collection = _create_connection()
    collection.drop()
    subprocess.run(["./mongoimport", "--db", "axxes", "--collection", "indomoBusinesses", "--file", "data.json"])


def _create_connection() -> Collection:
    client = pymongo.MongoClient("localhost", 27017)
    db = client["axxes"]
    return db["indomoBusinesses"]

clear_and_restore()
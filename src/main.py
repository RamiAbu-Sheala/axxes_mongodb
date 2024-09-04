import pymongo
import json

from pymongo.collection import Collection


def find_one(query: str) -> str:
    print(f"Running find_one : {query}")
    collection = _create_connection()
    json_query = _map_to_json(query)
    result = collection.find_one(json_query)
    assert result is not None
    print(f"Result find one businessId : {result.get('businessId')}")
    return result


def find_one_date(query: str) -> str:
    print(f"Running find_one_date : {query}")
    collection = _create_connection()
    result = collection.find_one(query)
    assert result is not None
    print(f"Result find one raw businessId : {result.get('businessId')}")
    return result



def find_one_project(query: str, projection) -> str:
    print(f"Running find_one_project : {query}")
    collection = _create_connection()
    json_query = _map_to_json(query)
    json_projection = _map_to_json(projection)

    result = collection.find_one(json_query, projection=json_projection)
    assert result is not None
    print(f"Result find one project : {result.get('projects')[0].get('mediaLibContainerId')}")
    return result


def find_many(query: str) -> list[str]:
    print(f"Running find_many : {query}")
    collection = _create_connection()
    json_query = _map_to_json(query)

    results = list(collection.find(json_query))
    assert result is not None
    number_of_results = len(results)
    print(f"Number of results : {number_of_results}")
    for result in results:
        print(f"Result find many businessId : {result.get('businessId')}")
    return results


def count(query: str) -> int:
    print(f"Running count : {query}")
    collection = _create_connection()
    json_query = _map_to_json(query)
    count = collection.count_documents(json_query)
    assert count is not None
    print(f"Number of documents counted : {count}")
    return count


def update(query: str, update: str) -> str:
    print(f"Running query : {query}, update : {update}")
    collection = _create_connection()
    json_query = _map_to_json(query)
    json_update = _map_to_json(update)

    return collection.update_one(json_query, json_update)


def aggregate(pipeline: [str]) -> list[str]:
    pipeline_json = list(map(lambda section: _map_to_json(section), pipeline))
    collection = _create_connection()
    print(f"Pipeline : {pipeline_json}")
    return list(collection.aggregate(pipeline_json))


def _create_connection() -> Collection:
    client = pymongo.MongoClient("localhost", 27017)
    db = client["axxes"]
    return db["indomoBusinesses"]


def _map_to_json(value: str):
    try:
        return json.loads(value)
    except json.decoder.JSONDecodeError:
        print(f"Provided json is invalid : {value}")
        raise json.decoder.JSONDecodeError

import pymongo
import json

def load_data_to_mongodb():
    # Connect to MongoDB
    client = pymongo.MongoClient("<your_connection_string>")
    db = client["your_database_name"]  # Replace with your actual database name

    # Load data from JSON file (adjust the path accordingly)
    with open("path/to/your/data.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    # Insert data into MongoDB collections
    # Example: Insert users
    users_collection = db["users"]
    users_collection.insert_many(data["users"])

    # Example: Insert channels
    channels_collection = db["channels"]
    channels_collection.insert_many(data["channels"])

    # Example: Insert messages
    messages_collection = db["messages"]
    messages_collection.insert_many(data["messages"])

    print("Data loaded successfully.")

if __name__ == "__main__":
    load_data_to_mongodb()

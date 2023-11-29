import json
import pymongo
import asyncio
from bson.json_util import dumps

# Define your MongoDB connection string
MONGODB_URI = ""

# Once we connect to the database once, we'll store that connection and reuse it so that we don't have to connect to the database on every request.
cached_db = None

async def connect_to_database():
    global cached_db
    if cached_db:
        return cached_db

    # Connect to our MongoDB database hosted on MongoDB Atlas
    client = pymongo.MongoClient(MONGODB_URI)

    # Specify which database we want to use
    db = client.sample_mflix

    cached_db = db
    return db

async def get_user_settings(user_id):
    # Get an instance of our database
    db = await connect_to_database()

    # Make a MongoDB MQL Query to get user settings based on the unique user ID
    user_settings = db.users.find_one({"user_id": user_id})

    return user_settings

def lambda_handler(event, context):
    # By default, AWS Lambda waits until the runtime event loop is empty before freezing the process and returning the results to the caller.
    # Setting this property to False requests that AWS Lambda freeze the process soon after the callback is invoked.
    context.callbackWaitsForEmptyEventLoop = False

    # Extract the unique user ID from the API request
    user_id = event.get("queryStringParameters", {}).get("user_id")

    if not user_id:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Missing user_id parameter"}),
        }

    # Run the asynchronous function using asyncio.run
    user_settings = asyncio.run(get_user_settings(user_id))

    if not user_settings:
        return {
            "statusCode": 404,
            "body": json.dumps({"error": "User not found"}),
        }

    response = {
        "statusCode": 200,
        "body": json.dumps(user_settings, default=str),
    }

    return response

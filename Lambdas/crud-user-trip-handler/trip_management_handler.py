from datetime import datetime
from bson import ObjectId
from pymongo import MongoClient
from jwt_utils import validate_jwt_token  # Assuming you have a JWT validation function

# Connect to MongoDB
client = MongoClient("your_mongodb_uri")
db = client["your_database"]
trips_collection = db["trips"]

# CRUD operations for Trip Management

def create_trip(event):
    try:
        token = event['headers'].get('Authorization', '').split('Bearer ')[-1]
        decoded_token = validate_jwt_token(token)

        if decoded_token:
            # User is authenticated, proceed with creating a trip
            body = json.loads(event['body'])
            trip_details = {
                'creator_id': decoded_token['sub'],
                'date': body['date'],
                'time': body['time'],
                'location': body['location'],
                'description': body['description'],
                'participants': [decoded_token['sub']]
            }
            result = trips_collection.insert_one(trip_details)
            return {'statusCode': 200, 'body': json.dumps({'message': 'Trip created successfully', 'trip_id': str(result.inserted_id)})}
        else:
            return {'statusCode': 401, 'body': json.dumps({'message': 'Invalid or expired token'})}
    except Exception as e:
        return {'statusCode': 500, 'body': json.dumps({'message': 'Internal Server Error'})}

def join_trip(event):
    try:
        token = event['headers'].get('Authorization', '').split('Bearer ')[-1]
        decoded_token = validate_jwt_token(token)

        if decoded_token:
            trip_id = event['pathParameters']['id']
            result = trips_collection.update_one(
                {'_id': ObjectId(trip_id)},
                {'$addToSet': {'participants': decoded_token['sub']}}
            )

            if result.matched_count > 0 and result.modified_count > 0:
                return {'statusCode': 200, 'body': json.dumps({'message': 'Joined trip successfully'})}
            else:
                return {'statusCode': 404, 'body': json.dumps({'message': 'Trip not found'})}
        else:
            return {'statusCode': 401, 'body': json.dumps({'message': 'Invalid or expired token'})}
    except Exception as e:
        return {'statusCode': 500, 'body': json.dumps({'message': 'Internal Server Error'})}

# Implement similar handlers for leaving trips, sending trip invitations, and filtering/sorting trips

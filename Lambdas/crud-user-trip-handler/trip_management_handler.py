from datetime import datetime
from bson import ObjectId
from auth_utils import db
from Utils.auth_utils import validate_jwt_token
import json

# Connect to MongoDB collections
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
            return {'statusCode': 200,
                    'body': json.dumps({'message': 'Trip created successfully', 'trip_id': str(result.inserted_id)})}
        else:
            return {'statusCode': 401, 'body': json.dumps({'message': 'Invalid or expired token'})}
    except Exception as e:
        return {'statusCode': 500, 'body': json.dumps({'message': 'Internal Server Error'})}


def join_trip(event):
    try:
        # Extract trip ID and user ID from the request
        body = json.loads(event['body'])
        trip_id = body.get('trip_id')
        user_id = body.get('user_id')

        # Validate the presence of required parameters
        if not trip_id or not user_id:
            return {'statusCode': 400, 'body': json.dumps({'message': 'Missing required parameters'})}

        # Check if the trip exists
        trip = trips_collection.find_one({'_id': ObjectId(trip_id)})
        if not trip:
            return {'statusCode': 404, 'body': json.dumps({'message': 'Trip not found'})}

        # Add the user to the list of participants
        trips_collection.update_one({'_id': ObjectId(trip_id)}, {'$addToSet': {'participants': user_id}})

        return {'statusCode': 200, 'body': json.dumps({'message': 'Joined trip successfully'})}
    except Exception as e:
        return {'statusCode': 500, 'body': json.dumps({'message': 'Internal Server Error'})}


def leave_trip(event):
    try:
        # Extract trip ID and user ID from the request
        body = json.loads(event['body'])
        trip_id = body.get('trip_id')
        user_id = body.get('user_id')

        # Validate the presence of required parameters
        if not trip_id or not user_id:
            return {'statusCode': 400, 'body': json.dumps({'message': 'Missing required parameters'})}

        # Check if the trip exists
        trip = trips_collection.find_one({'_id': ObjectId(trip_id)})
        if not trip:
            return {'statusCode': 404, 'body': json.dumps({'message': 'Trip not found'})}

        # Remove the user from the list of participants
        trips_collection.update_one({'_id': ObjectId(trip_id)}, {'$pull': {'participants': user_id}})

        return {'statusCode': 200, 'body': json.dumps({'message': 'Left trip successfully'})}
    except Exception as e:
        return {'statusCode': 500, 'body': json.dumps({'message': 'Internal Server Error'})}


def send_trip_invitation(event):
    try:
        token = event['headers'].get('Authorization', '').split('Bearer ')[-1]
        decoded_token = validate_jwt_token(token)

        if decoded_token:
            trip_id = event['pathParameters']['id']
            body = json.loads(event['body'])
            invited_user_id = body['invited_user_id']

            result = trips_collection.update_one(
                {'_id': ObjectId(trip_id)},
                {'$addToSet': {'invitations': {'user_id': invited_user_id, 'status': 'pending'}}}
            )

            if result.matched_count > 0 and result.modified_count > 0:
                return {'statusCode': 200, 'body': json.dumps({'message': 'Invitation sent successfully'})}
            else:
                return {'statusCode': 404, 'body': json.dumps({'message': 'Trip not found'})}
        else:
            return {'statusCode': 401, 'body': json.dumps({'message': 'Invalid or expired token'})}
    except Exception as e:
        return {'statusCode': 500, 'body': json.dumps({'message': 'Internal Server Error'})}


def filter_and_sort_trips(event):
    try:
        # Get query parameters from the URL
        location = event['queryStringParameters'].get('location')
        date = event['queryStringParameters'].get('date')

        # Define a base query
        query = {}

        # Add filters based on user preferences
        if location:
            query['location'] = location

        if date:
            query['date'] = date

        # Fetch trips from the database based on the query
        trips = trips_collection.find(query)

        # Sort trips based on a specific criterion (e.g., date)
        sorted_trips = sorted(trips, key=lambda x: x.get('date', ''))

        # Return the filtered and sorted trips
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Trips filtered and sorted successfully', 'trips': sorted_trips})
        }
    except Exception as e:
        return {'statusCode': 500, 'body': json.dumps({'message': 'Internal Server Error'})}

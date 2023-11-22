import json
from auth_utils import validate_jwt_token, db
from bson import ObjectId


def create_trip(event, context):
    try:
        # Validate JWT token
        token = event['headers'].get('Authorization', '').split('Bearer ')[-1]
        decoded_token = validate_jwt_token(token)
        if not decoded_token:
            return {'statusCode': 401, 'body': json.dumps({'message': 'Invalid or expired token'})}

        # Create a new trip
        body = json.loads(event['body'])
        trip = {
            'user_id': decoded_token['sub'],
            'destination': body.get('destination'),
            'date': body.get('date'),
            'description': body.get('description')
        }
        result = db.trips.insert_one(trip)

        return {'statusCode': 200, 'body': json.dumps({'message': 'Trip created', 'trip_id': str(result.inserted_id)})}
    except Exception as e:
        return {'statusCode': 500, 'body': json.dumps({'message': 'Internal Server Error'})}

def get_trip(event, context):
    try:
        # Validate JWT token
        token = event['headers'].get('Authorization', '').split('Bearer ')[-1]
        decoded_token = validate_jwt_token(token)
        if not decoded_token:
            return {'statusCode': 401, 'body': json.dumps({'message': 'Invalid or expired token'})}

        # Get user's trips
        user_id = decoded_token['sub']
        trips = list(db.trips.find({'user_id': user_id}))

        return {'statusCode': 200, 'body': json.dumps({'trips': trips})}
    except Exception as e:
        return {'statusCode': 500, 'body': json.dumps({'message': 'Internal Server Error'})}

def update_trip(event, context):
    try:
        # Validate JWT token
        token = event['headers'].get('Authorization', '').split('Bearer ')[-1]
        decoded_token = validate_jwt_token(token)
        if not decoded_token:
            return {'statusCode': 401, 'body': json.dumps({'message': 'Invalid or expired token'})}

        # Update a trip
        body = json.loads(event['body'])
        trip_id = body.get('trip_id')
        updated_trip = {
            'destination': body.get('destination'),
            'date': body.get('date'),
            'description': body.get('description')
        }
        db.trips.update_one({'_id': ObjectId(trip_id), 'user_id': decoded_token['sub']}, {'$set': updated_trip})

        return {'statusCode': 200, 'body': json.dumps({'message': 'Trip updated'})}
    except Exception as e:
        return {'statusCode': 500, 'body': json.dumps({'message': 'Internal Server Error'})}

def delete_trip(event, context):
    try:
        # Validate JWT token
        token = event['headers'].get('Authorization', '').split('Bearer ')[-1]
        decoded_token = validate_jwt_token(token)
        if not decoded_token:
            return {'statusCode': 401, 'body': json.dumps({'message': 'Invalid or expired token'})}

        # Delete a trip
        body = json.loads(event['body'])
        trip_id = body.get('trip_id')
        db.trips.delete_one({'_id': ObjectId(trip_id), 'user_id': decoded_token['sub']})

        return {'statusCode': 200, 'body': json.dumps({'message': 'Trip deleted'})}
    except Exception as e:
        return {'statusCode': 500, 'body': json.dumps({'message': 'Internal Server Error'})}

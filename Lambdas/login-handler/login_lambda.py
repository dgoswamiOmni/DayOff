import json
from cassandra_utils import session
from auth_utils import generate_jwt_token, log_login
from passlib.hash import pbkdf2_sha256


def authenticate_user(username, password):
   
    # Check if the user exists
    user_query = session.prepare('SELECT * FROM users.account WHERE username = ?')
    user_result = session.execute(user_query, [username])

    if not user_result:
        return {'statusCode': 401, 'body': json.dumps({'message': 'Invalid credentials'})}

    user = user_result[0]
    hashed_password = user['password']

    # Verify the password
    if not pbkdf2_sha256.verify(password, hashed_password):
        return {'statusCode': 401, 'body': json.dumps({'message': 'Invalid credentials'})}

    # Generate a JWT token
    session_token = generate_jwt_token(username)

    # Log the login time
    log_login(username)

    return {'statusCode': 200,
            'body': json.dumps({'message': 'Login successful', 'session_token': session_token.decode('utf-8')})}

def login_user(event):
    try:
        # Handle login
        body = json.loads(event['body'])
        username = body['username']
        password = body['password']

        response = authenticate_user(username, password)
        return response

    except Exception as e:
        return {'statusCode': 500, 'body': json.dumps({'message': 'Internal Server Error'})}

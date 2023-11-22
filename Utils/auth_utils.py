import uuid
from datetime import datetime, timedelta
import jwt
from Utils.cassandra_utils import session
from secret_utils import secrets


SECRET_KEY = secrets['jwt_secret_key']
ALGORITHM = 'HS256'


def validate_jwt_token(token):
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return decoded_token
    except jwt.ExpiredSignatureError:
        return None  # Token has expired
    except jwt.InvalidTokenError:
        return None  # Invalid token


def generate_jwt_token(username):
    expiration_time = datetime.utcnow() + timedelta(hours=24)  # You may adjust the expiration time
    payload = {
        'sub': username,
        'exp': expiration_time,
        'iat': datetime.utcnow(),
        'jti': str(uuid.uuid4())  # Unique identifier for the token
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    
    # Store the token in the user_tokens table
    insert_token_query = session.prepare('INSERT INTO users.user_tokens (username, token) VALUES (?, ?)')
    session.execute(insert_token_query, [username, token])

    return token


def log_login(username):
    login_timestamp = datetime.utcnow()
    insert_login_history_query = session.prepare('INSERT INTO users.login_history (username, login_time) VALUES (?, ?)')
    session.execute(insert_login_history_query, [username, login_timestamp])


def log_logout(username):
    logout_timestamp = datetime.utcnow()
    update_logout_query = session.prepare(
        'UPDATE users.login_history SET logout_time = ? WHERE username = ? AND logout_time IS NULL')
    session.execute(update_logout_query, [logout_timestamp, username])

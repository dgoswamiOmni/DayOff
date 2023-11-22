import json
from Utils.auth_utils import validate_jwt_token, log_logout

def logout_user(event):
    token = event['headers'].get('Authorization', '').split('Bearer ')[-1]

    # Validate the JWT token
    decoded_token = validate_jwt_token(token)

    if decoded_token:
        # Log the logout time
        log_logout(decoded_token['sub'])
        return {'statusCode': 200, 'body': json.dumps({'message': 'Logout successful'})}
    else:
        return {'statusCode': 401, 'body': json.dumps({'message': 'Invalid or expired token'})}

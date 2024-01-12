# import json
# import random
# import boto3
#
#
# def lambda_handler(event, context):
#     try:
#         print("Received event:", json.dumps(event))
#         # Extract user email from the request
#         user_email = event.get('email')
#         # Log the extracted email for debugging
#         print("Extracted email:", user_email)
#         # Check if user_email is None or an empty string
#         if user_email is None or not user_email.strip():
#             raise ValueError("Invalid or missing email in the event payload")
#             # Generate a random 6-digit OTP
#         otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
#
#         # Replace 'YOUR_SNS_TOPIC_ARN' with the ARN of your SNS topic
#         sns_topic_arn = 'YOUR_SNS_TOPIC_ARN'
#
#         # Replace 'YOUR_AWS_REGION' with your AWS region
#         aws_region = 'YOUR_AWS_REGION'
#
#         # Send OTP to the user via SNS
#         sns = boto3.client('sns', region_name=aws_region)
#         message = f'Your OTP for email verification is: {otp}'
#         # Log the message and email attributes for debugging
#         print("Message:", message)
#         print("MessageAttributes:", {'email': {'DataType': 'String', 'StringValue': user_email}})
#
#         sns.publish(
#             TopicArn=sns_topic_arn,
#             Message=message,
#             Subject='Email Verification OTP',
#             MessageAttributes={
#                 'email': {
#                     'DataType': 'String',
#                     'StringValue': user_email
#                 }
#             }
#         )
#
#         return {
#             'statusCode': 200,
#             'body': json.dumps('OTP sent successfully')
#         }
#     except Exception as e:
#         # Log the exception for debugging
#         print("Exception:", str(e))
#
#         return {
#             'statusCode': 400,
#             'body': json.dumps(f'Error: {str(e)}')
#    }

import json
import os
import time
import random
from pymongo import MongoClient
import boto3

# Initialize MongoDB client
mongo_client = MongoClient('your_mongodb_connection_string')
db = mongo_client['your_database_name']
otp_collection = db['your_collection_name']

# Initialize SNS client
sns_client = boto3.client('sns', region_name='your_region')


def send_otp_sms(phone_number, otp):
    message = f'Your OTP is: {otp}'

    sns_client.publish(
        PhoneNumber=phone_number,
        Message=message
    )


def lambda_handler(event, context):
    # TODO implement

    if 'queryStringParameters' in event and 'otp' not in event['queryStringParameters']:
        # Triggered to send OTP
        phone_number = event['queryStringParameters']['phone_number']
        print(f"Sending OTP to: {phone_number}")

        # Generate a random 6-digit OTP
        generated_otp = str(random.randint(100000, 999999))
        print("Generated OTP : {}".format(generated_otp))

        # Store OTP and expiration time in MongoDB
        expiration_time = int(time.time()) + 300  # OTP expires in 5 minutes
        otp_collection.update_one(
            {'phone_number': phone_number},
            {'$set': {'otp': generated_otp, 'expiration_time': expiration_time}},
            upsert=True
        )

        # Send OTP via SNS
        send_otp_sms(phone_number, generated_otp)

        return {
            'statusCode': 200,
            'body': json.dumps('OTP sent successfully!')
        }

    elif 'queryStringParameters' in event and 'otp' in event['queryStringParameters']:
        # Triggered to verify OTP
        phone_number = event['queryStringParameters'].get('phone_number')
        print(f"Verifying OTP for: {phone_number}")

        # Retrieve the OTP entered by the user
        otp_from_user = event['queryStringParameters']['otp']
        print("The received otp : {}".format(otp_from_user))

        # Retrieve the stored OTP and expiration time from MongoDB
        stored_data = otp_collection.find_one({'phone_number': phone_number})

        if not stored_data:
            return {
                'statusCode': 400,
                'body': json.dumps('No OTP found for the provided phone number')
            }

        stored_otp_value = stored_data['otp']
        stored_expiration_time = stored_data['expiration_time']

        print(f"Stored OTP: {stored_otp_value}")

        if int(stored_expiration_time) < int(time.time()):
            return {
                'statusCode': 400,
                'body': json.dumps('Time Over. OTP has expired.')
            }
        else:
            if stored_otp_value == otp_from_user:
                return {
                    'statusCode': 200,
                    'body': json.dumps('OTP Verified!')
                }
            else:
                return {
                    'statusCode': 400,
                    'body': json.dumps(f'Wrong OTP! Expected: {stored_otp_value}, Received: {otp_from_user}')
                }

    return {
        'statusCode': 400,
        'body': json.dumps('Invalid request. Provide either phone_number or otp in queryStringParameters.')}

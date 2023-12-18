import json
import random
import boto3


def lambda_handler(event, context):
    try:
        print("Received event:", json.dumps(event))
        # Extract user email from the request
        user_email = event.get('email')
        # Log the extracted email for debugging
        print("Extracted email:", user_email)
        # Check if user_email is None or an empty string
        if user_email is None or not user_email.strip():
            raise ValueError("Invalid or missing email in the event payload")
            # Generate a random 6-digit OTP
        otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])

        # Replace 'YOUR_SNS_TOPIC_ARN' with the ARN of your SNS topic
        sns_topic_arn = 'YOUR_SNS_TOPIC_ARN'

        # Replace 'YOUR_AWS_REGION' with your AWS region
        aws_region = 'YOUR_AWS_REGION'

        # Send OTP to the user via SNS
        sns = boto3.client('sns', region_name=aws_region)
        message = f'Your OTP for email verification is: {otp}'
        # Log the message and email attributes for debugging
        print("Message:", message)
        print("MessageAttributes:", {'email': {'DataType': 'String', 'StringValue': user_email}})

        sns.publish(
            TopicArn=sns_topic_arn,
            Message=message,
            Subject='Email Verification OTP',
            MessageAttributes={
                'email': {
                    'DataType': 'String',
                    'StringValue': user_email
                }
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps('OTP sent successfully')
        }
    except Exception as e:
        # Log the exception for debugging
        print("Exception:", str(e))

        return {
            'statusCode': 400,
            'body': json.dumps(f'Error: {str(e)}')
        }
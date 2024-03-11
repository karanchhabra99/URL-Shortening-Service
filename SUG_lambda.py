import boto3
import random

def base58_encode():
    # Define the base-58 characters (excluding look-alike characters)
    base58_chars = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    number = random.randint(2**63, 2**64 - 1)
    # Initialize an empty result string
    result = ""

    # Convert the number to base-58
    while number > 0:
        digit = number % 58
        result = base58_chars[digit] + result
        number //= 58
    result = result[:6]
    return result

def lambda_handler(event, context):
    try:
        url =  event[0]
        # Retrieve a list of objects from the bucket
        bucket_name = 'redirect-sug'
        s3_client = boto3.client('s3')
        objects = s3_client.list_objects(Bucket=bucket_name)
        SOG = base58_encode()

        while SOG in objects:
            SOG = base58_encode()

        # HTML content for the redirecting website
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta http-equiv="refresh" content="0;url={url}">
        </head>
        <body>
            Redirecting to <a href="{url}">Website</a>...
        </body>
        </html>
        """

        # Specify your S3 bucket and object key
        object_key = f'{SOG}.html'  # Customize the object key as needed

        # Upload HTML content to S3
        s3_client.put_object(Bucket=bucket_name, Key=object_key, Body=html_content, ContentType='text/html', ACL='public-read')

        return {
            'statusCode': 200,
            'body': SOG
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }

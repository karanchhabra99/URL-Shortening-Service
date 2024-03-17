import boto3
from datetime import datetime
import random

def base58_encode():
    # Define the base-58 characters (excluding look-alike characters)
    base58_chars = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    number = random.randint(10**9, 2**64 - 1)
    # Initialize an empty result string
    result = ""

    # Convert the number to base-58
    while number > 0:
        digit = number % 58
        result = base58_chars[digit] + result
        number //= 58

    return result

def lambda_handler(event, context):
    try:
        url = event["URL"]
        email = event["email"]
        
        # Initialize a DynamoDB client
        dynamodb = boto3.resource('dynamodb')
        
        # # Specify the table
        table = dynamodb.Table('TinyURL-Table')
        items ='0'
        
        while items:
            SOG = base58_encode()
            
            # Check if the new key already exists in the table
            response = table.query(
                KeyConditionExpression=boto3.dynamodb.conditions.Key('key').eq(SOG)
            )
            items = response['Items']

        item = {
            'time': datetime.now().isoformat(),
            'email': email,
            'key': SOG,
            'url': url
        }
    
        # Insert the item
        response = table.put_item(Item=item)
            
        return {
        'statusCode': 200,
        'body': f"{SOG}"
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }

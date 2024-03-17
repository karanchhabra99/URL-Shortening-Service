import boto3

def lambda_handler(event, context):
    try:
        # Extract the UserString and email from the event
        user_string = event["UserString"]
        email = event["email"]
        
        # Initialize a DynamoDB client
        dynamodb = boto3.resource('dynamodb')
        
        # Specify the table
        table = dynamodb.Table('TinyURL-Table')
        
        # Get the item
        response = table.get_item(
            Key={
                'key': user_string
            }
        )
        
        # Check if the email matches
        if 'Item' in response and response['Item']['email'] == email:
            # Delete the item
            response = table.delete_item(
                Key={
                    'key': user_string
                }
            )
            
            return {
                'statusCode': 200,
                'body': f"Record with key {user_string} deleted successfully."
            }
        else:
            return {
                'statusCode': 403,
                'body': f"Some issue occured."
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': "Error"
        }

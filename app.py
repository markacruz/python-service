import boto3
import json

def handler(event, context):
    try:
        client = boto3.resource('dynamodb')
        table = client.Table('python-service-db')
        
        print(event)
        
        if event['httpMethod'] == "GET" and event['path'] == "/items":
            res = table.get_item(
                Key = {
                    'firstName': event['pathParameters']['firstName'],
                    'lastName': event['pathParameters']['lastName']
                    }
                )
            body = res
        elif event['httpMethod'] == "POST" and event['path'] == "/items":
            describeTable = table.describe_table(TableName='python-service-db')
            table.put_item(
                Item = {
                    'id': describeTable['Table']['ItemCount'],
                    'firstName': event['body']['firstName'],
                    'lastName': event['body']['lastName']
                    }
                )
            body = {
                'message': 'Successfully added!'
                }
        return {
            'statusCode': 200,
            'body': body
        }
        
    except Exception as e:
        return {
            'statusCode': 400,
            'body': e['message']
        }
        


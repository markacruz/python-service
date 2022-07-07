import boto3
import json

def handler(event, context):
    body = ""
    client = boto3.resource('dynamodb')
    table = client.Table('python-service-db')
    
    print(event)
    
    if event['routeKey'] == "GET /items":
        res = table.get_item(
            Key = {
                'id': event['queryStringParameters']['id']
                }
            )
        body = res
    elif event['routeKey'] == "POST /items":
        describeTable = table.describe_table(TableName='python-service-db')
        table.put_item(
            Item = {
                'id': describeTable['Table']['ItemCount'],
                'firstName': event['queryStringParameters']['firstName'],
                'lastName': event['queryStringParameters']['lastName']
                }
            )
        body = {
            'message': 'Successfully added!'
            }
    
    if body == "":
        return {
            'statusCode': 400,
        }
    else:
        return {
            'statusCode': 200,
            'body': body
        }
import boto3
import json

def handler(event, context):
    try:
        body = ""
        client = boto3.resource('dynamodb')
        table = client.Table('python-service-db')
        
        if event['routeKey'] == "GET /items":
            res = table.get_item(
                Key = {
                    'id': event['queryStringParameters']['id']
                    }
                )
            body = res['Item']
        
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
            return json.dumps({
                'statusCode': 400,
            })
        else:
            return json.dumps({
                'statusCode': 200,
                'body': body
            })
    except:
        return json.dumps({
                'statusCode': 200,
                'body': body
        })
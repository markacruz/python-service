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
        
        if event['routeKey'] == "POST /items":
            print({"message": "here"})
            describeTable1 = client.describe_table(TableName='python-service-db')
            describeTable2 = table.describe_table(TableName='python-service-db')
            print(describeTable1)
            print(describeTable2)
            table.put_item(
                Item = {
                    'id': describeTable1['Table']['ItemCount'],
                    'firstName': event['body']['firstName'],
                    'lastName': event['body']['lastName']
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
    except Exception as e:
        return json.dumps({
                'statusCode': 400,
                'body': e
        })
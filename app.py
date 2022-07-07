import boto3
import json

def handler(event, context):
    
    eventJson = json.loads(event)
    
    try:
        client = boto3.resource('dynamodb')
        table = client.Table('python-service-db')
        
        table.put_item(Item= {
            'id': '0',
            'name': 'Mark'
        })
        
        # if eventJson['routeKey'] is "GET /items/{id}":
        #     table.get_item({
        #     "Key": {
        #       'id': event.pathParameters.id
        #         }
        #     })
        #     body = {
        #         'message': 'Item added!'
        #     }
        # elif eventJson['routeKey'] is "POST /items":
        #     table.put_item(
                
        #     )
            
        # return {
        #     'statusCode': 200,
        #     'body': body
        # }
        return {
            'status': 200,
            'message': 'Successfully added!'
        }
        
    except Exception as e:
        return {
            'statusCode': 400,
            'body': e['message']
        }
        


import json

def handler(event, context):
    path = event['path']
    body = json.loads(event['body'])
    fruit = body['fruit']
    
    if fruit == 'cherry':
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'text/plain'
            },
            'body': f'Good Morning, CDK! I love {fruit} {path}'
        }

    elif fruit == 'durian':
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'text/plain'
            },
            'body': f'Good Morning, CDK! I do not like {fruit} {path}'
        }
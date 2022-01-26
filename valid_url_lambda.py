import urllib3
import json


def lambda_handler(event, context):
    http = urllib3.PoolManager()
    url = event['queryStringParameters'] ['url']


    try:
        response = http.request('GET', url)
        response_message = "Site reached: " + str(response.status)
 
    except:
        response_message = 'Site could not be reached.'
    
    
    transactionResponse = {}
    transactionResponse['url'] = url
    transactionResponse['response_message'] = response_message
    
    response_object = {}
    response_object['statusCode'] = 200
    response_object['headers'] = {}
    response_object['headers']['Content-Type'] = 'application/json'
    response_object['body'] = json.dumps(transactionResponse)
        
    return response_object
    
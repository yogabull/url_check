import urllib3

def lambda_handler(event, context):
    url = event['url']
    
    http = urllib3.PoolManager()
    
    try:
        response = http.request('GET', url)
        print(f'STATUS CODE: {r.status}.')
        return r.status
    except:
        response = 'NOT VALID'
        return response
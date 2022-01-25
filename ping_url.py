import os

def lambda_handler(event, context):
    
    url = event['url']
    
    def ping_that(url):
        response = os.system('ping -c 2 ' + url)
        if response == 0:
            return True
        else:
            return False
    
    ping_that(url)
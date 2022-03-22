# AWS Lambda Script to ping a url.

### Description
The goal is verify a url is active using AWS EventBridge and the AWS lambda service.

### Progress
Created a script to ping a url using python, but was not successful using it with AWS Lambda.
Discoverd that AWS lambda does not support ICMP protocol, so I opted to try using the Python _requests_ module. Turns out, AWS has depricated _requests_ and replaced the library _urllib3_.

### Technologies
Python

### Scripts

| Name | Description                     |
| --------------- | -------------------- |  
| ping_url.py     | Python script that failed to run in Lambda. 
| valid_url.py    | Python script that uses __requests__ to verify if a url is active. 
| valid_url_lambda.py | Python script that works in AWS lambda to verify if a url is active. 

### References
https://forums.aws.amazon.com/thread.jspa?threadID=263968

https://aws.amazon.com/blogs/compute/upcoming-changes-to-the-python-sdk-in-aws-lambda/

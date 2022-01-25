#Script to verify if a url is valid.

import requests

def main():
    url = ask_for_url()
    answer = is_valid(url)
    report(answer)

    
def ask_for_url():
    print('Which URL do we test: ')
    answer = input('(a)  https://www.google.com \n(b)  www.badurl.com\n  : ')
    if answer == 'a':
        answer = 'https://www.google.com'
    else:
        answer = 'www.badurl.com'
    return answer


def is_valid(url):
    try:
        response = requests.head(url)
    except requests.exceptions.MissingSchema:
        response = 'not valid'
    return response


def report(answer):
    if answer == 'not valid':
        print('The URL is NOT VALID')
    else:
        print('That is a VALID URL')

if __name__ == '__main__':
    main()
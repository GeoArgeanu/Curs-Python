from pprint import pprint

import requests

URL = 'https://jsonplaceholder.typicode.com'
payload = {
    'title': 'New Title'
}

response = requests.patch(f'{URL}/posts/1', json=payload)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('request failed with sataus code: ', response.status_code)

'''
Patch modifica doar campurile specificate in payload
'''

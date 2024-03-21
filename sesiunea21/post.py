from pprint import pprint

import requests

URL = 'https://jsonplaceholder.typicode.com'
payload = {
    'body': 'Postare noua',
    'title': 'Titlu nou',
    'userId': 2
}

response = requests.post(f'{URL}/posts', json=payload)
if response.status_code == 201:
    data = response.json()
    pprint(data)
else:
    print('request failed with status code: ', response.status_code)
from pprint import pprint

import requests

URL = 'https://jsonplaceholder.typicode.com'
response = requests.get(f'{URL}/posts')

if response.status_code == 200:  # daca requestul a avut succes
    data = response.json()  # transformam continutul din corpul raspunsului din string in format json intr-un dictionar
    pprint(data)
else:
    print('Request failed with status code: ', response.status_code)

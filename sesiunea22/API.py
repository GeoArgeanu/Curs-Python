from pprint import pprint

import requests


class BooksAPIClient:
    URL = 'https://simple-books-api.glitch.me'

    def __init__(self, client_name, client_email):
        self.client_name = client_name
        self.client_email = client_email
        self._token = self.__generate_token()

    def __generate_token(self):
        response = requests.post(f'{self.URL}/api-client',
                                 json={'clientName': self.client_name, 'clientEmail': self.client_email})
        data = response.json()
        print(data)
        return data.get('accesToken')

    def __get_headers(self):
        return {
            'Authorization': f'Bearer {self._token}'
        }

    # ex nr 4
    def add_order(self, bookId):
        response = requests.post(f'{self.URL}/orders', json={'bookId': bookId, 'customerName': self.client_name},
                                 headers=self.__get_headers())
        return response.json()

    # ex nr 2
    def get_all_orders(self):
        response = requests.get(f'{self.URL}/orders', headers=self.__get_headers())
        return response.json()

    # ex nr 5
    def delete_order(self, orderId):
        requests.delete(f'{self.URL}/orders/{orderId}', headers=self.__get_headers())


b = BooksAPIClient('Geo', 'argeanu_g@yahoo.com')
print(b.add_order(1))
pprint(b.get_all_orders())
print(20 * '*')
b.delete_order('ACawbuW6CO-wlNTVqdn9q')
print(20 * '*')
pprint(b.get_all_orders())

'''
Folosim https://jsonplaceholder.typicode.com/guide/ Toate requesturile se
vor face prima data in Postman (pentru verificare),
iar apoi folosind libraria requests din Python.

Structura datelor este următoarea:
- fiecare post este deținut de un user, și poate avea mai multe comments
- fiecare album este deținut de un user, și poate avea mai multe photos
- fiecare todo este detinut de un user.
1. Alege un user din lista de useri predefiniti. Pentru acesta,
fa requesturile necesare pentru a afișa următoarele informații:
	-> lista de posts
Pentru a menține output-ul la un nivel acceptabil, afișează la
fiecare dintre aceste liste doar informații despre primele 3 obiecte,
iar apoi afiseaza "+x more posts/", unde x este numărul de obiecte rămase.
'''

import requests
from pprint import pprint


class PostAPIClient:
    URL = 'https://jsonplaceholder.typicode.com'


    # rezolvare nr 1
    def get_post_by_user(self, userId):
        response = requests.get(f'{self.URL}/posts?userId={userId}')
        posts = response.json()
        first_3 = posts[:3]
        return first_3, len(posts) - 3



    # rezolvare nr 2
    def get_comments_by_post(self, postId):
        response = requests.get(f'{self.URL}/comments?postId={postId}')
        return response.json()



    # rezolvare nr 3
    def create_post(self, new_post):
        response = requests.post(f'{self.URL}/posts', json=new_post)
        return response.json()


    # rezolvare nr 5
    def get_todo_by_user(self, userId):
        response = requests.get(f'{self.URL}/todos?userId={userId}&completed=false')
        return response.json()



client = PostAPIClient()
posts, left = client.get_post_by_user(3)
pprint(posts)
print(f'{left} more posts')

'''
2. Alege un post, și afișează lista de comentarii. 
Alege un album, si afiseaza lista de photos.
'''
pprint(client.get_comments_by_post(100))



'''
3. Creeaza un post nou (atentie, acesta NU va fi salvat, dar putem analiza răspunsul 
pentru a vedea cum ar arata în viitor dacă ar fi fost salvat). 
Încearcă să-l creezi cu si fără id. Ce observi?
'''
payload = {
    'title': 'New Title',
    'body': 'new body',
    'userId': 1,
}

pprint(client.create_post(payload))



'''
5. Folosind query parameters, filtrează lista de todos pentru 
userul ales astfel incat sa afisezi doar todos care nu sunt 
completed.
'''

pprint(client.get_todo_by_user(1))
'''
Iterators

Implementati un iterator numit ReverseIterator, care parcurge o
colectie in sens opus. Exemplu de folosire:

note = [3, 7, 5, 8, 10]
rev_it = ReverseIterator(note)
print(next(rev_it))  # printeaza 10
print(next(rev_it))  # printeaza 8
print(next(rev_it))  # printeaza 5
s.a.m.d
'''


class ReverseIterator():
    def __init__(self, collection):
        self.collection = collection
        self.start = len(collection) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < 0:
            raise StopIteration

        current_index = self.start
        self.start -= 1
        return self.collection[current_index]


note = [3, 7, 5, 8, 10]
rev_it = ReverseIterator(note)
print(next(rev_it))  # printeaza 10
print(next(rev_it))  # printeaza 8
print(next(rev_it))  # printeaza 5

rev_it = ReverseIterator(note)
for elem in rev_it:
    print(elem)

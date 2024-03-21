# 1. printare

# string = "Hello"
# print(string)

# 2. for

# for elem in [1,2,3,4]:
#     print(elem)

# 3. clasa

# class Student:
#     def __init__(self, name):
#         self.name = name
#
# s = Student('Geo')
# print(s.name)


# 4. open

# with open("file.txt", 'w') as f:
#     f.write("hello")

# 5. indexing

# l = [1, 2, 3, 4, 5]
# print(l[-1])
# print(l[4])

# 6. slicing

# string = "Hello"
# print(string[5:6])
# print(string[2:4])
# print(string[-2:-4:-1])
# print(string[-1:-3:-1])
# print(string[4:2:-1])
# print(string[:3])
# print(string[1:])
# print(string[::-1])
#  H  e  l  l  o
#  0  1  2  3  4
# -5 -4 -3 -2 -1

# 7. inheritance
# from abc import ABC, abstractmethod
# class Animal(ABC):
#     @abstractmethod
#
#     def growl(self):
#         pass
#
#
# class Lion(Animal):
#     def growl(self):
#         print('Rawrr')

# 8. Collections

# l = [1, 2, 3]
# t = ("a", "b", "c")
# s = {2, 3, 4}
# print(type(l), type(t), type(s))

# 9. Generators

# def gen(n):
#     for i in range(n):
#         if i % 2 == 0:
#             yield i
#
#
# for even in gen(10):
#     print(even)

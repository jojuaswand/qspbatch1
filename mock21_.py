# count the number of lines in a file
# path = r"C:\Users\jojua\PycharmProjects\qspb1\names.txt"
# with open(path) as file_:
#     a = file_.readlines()
#     print(len(a))

# print the even numbered lines
# path = r"C:\Users\jojua\PycharmProjects\qspb1\names.txt"
# with open(path) as file_:
#     a = file_.readlines()
#     for i in range(len(a)):
#         if i % 2 == 0:
#             print(a[i])
#

# dictionary with words and its count pair
# s = "she sells sea shells on the sea shore"
# d = {}
# for i in s.split():
#     d[i] = s.count(i)
#
# print(d)

# number of elements present in the list without using inbuilt functions and methods
# l = [1, 2, "hello", 5]
# count = 0
# for i in l:
#     count += 1
# print(count)

# reverse a string without using inbuilt functions and slicing
# a = "hello"
# s = ""
# for i in a:
#     s = i + s
# print(s)

# string as input and returns first middle and last word
# s1 = "sea shells on the sea shore"
# s = s1.split()
# print(s[0], s[int(len(s)//2)], s[-1])

# decorator for time delay and total time

# import time
#
# def deco(func):
#     def wrap(*args, **kwargs):
#         start = time.time()
#         time.sleep(5)
#         print(func(*args, **kwargs))
#         end = time.time()
#         print(f"{end - start} seconds")
#     return wrap
#
# @deco
# def add(a, b):
#     return (a + b)
#
#
# add(4, 5)

# dictionary with index n value if numeric and if string reverse and element itself

# l = [1, "hello", 2, "hi"]
#
# d = {i:v for i, v in enumerate(l) if isinstance(v, (int, float))}
# d1 = {v[::-1]: v for i, v in enumerate(l) if isinstance(v, str )}
# print(d, d1)

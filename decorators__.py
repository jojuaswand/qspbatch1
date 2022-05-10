# def disp(x):
#     print("anything")
#     return x(4, 5)
#
#
# # disp()
#
#
# def add_(a, b):
#     # print(a + b)
#     return a + b
#
# print(disp(add_))
# add_(4, 5)
# print(add_)
# a = add_(4, 5) # here we are creating a first class object
# print(a)
# a = add_ # here we stored address of add_()
# print(a(4, 5)) # we used a to call add_()
# calling a function using another name is called monkey patching

# def disp(func):
#     print("execution")
#     return func
#
# @disp # add- = disp(add_)
# def add_(a,b):
#     return a + b
#
#
# # add_ = disp(add_)
# print(add_(4, 5))

""" here we are adding a new functionality to the original function
without modifying the original functionality.
so disp is the decorator function which decorates the original function"""


# def disp(func):
#     def wrapper(*args, **kwargs):
#         print("execution")
#         return func(*args, **kwargs)
#     return wrapper
#
#
# @disp
# def add_(*args, **kwargs):
#     sum_ = 0
#     for i in args:
#         sum_ += i
#     for j in kwargs:
#         sum_ += kwargs[j]
#
#     return sum_
#
#
# # print(add_(4, 6, 7, 8, a=10, b=20))
# @disp
# def sub_(*args, **kwargs):
#     diff = 0
#     for i in args:
#         diff = i
#         if diff == i:
#             diff = 0 - i
#         else:
#             diff -= i
#     for j in kwargs:
#         diff -= kwargs[j]
#     return diff
#
#
# print(sub_(5, 5, 5, a=10, b=20))
#

import time


# def spam(func):
#     def wrapper(*args, **kwargs):
#         time.sleep(5)
#         print("reversed")
#         func(*args, **kwargs)
#     return wrapper

# def spam(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         time.sleep(5)
#         print("reversed")
#         func(*args, **kwargs)
#         end = time.time()
#         print(f"the program took {end - start} seconds to run")
#     return wrapper
#
# def spam(n):
#     def spam1(func):
#         def wrapper(*args, **kwargs):
#             time.sleep(n)
#             print("reversed")
#             func(*args, **kwargs)
#         return wrapper
#     return spam1

# using parameterized decorator to repeat the original function n times
# def rep_(n):
#     def spam(func):
#         def wrapper(*args, **kwargs):
#             time.sleep(5)
#             print("reversed")
#             for i in range(n):
#                 func(*args, **kwargs)
#         return wrapper
#     return spam
#
#
# @rep_(5)
# def rev_(*args, **kwargs):
#     for i in args:
#         if isinstance(i, str):
#             print(i[::-1])
#     for j in kwargs:
#         if isinstance(kwargs[j], str):
#             print(kwargs[j][::-1])
#
#
# rev_("hello", strings="bye")


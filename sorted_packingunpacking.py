# l = [12, 1, 112, 5, 14, 6, 0]
# l.sort()
# print(l)
#
# s = "hello"
# l = list(s)
# l.sort()
# print(l)
# print(sorted(s))
# d = {"name": "j", "age": 2, "rno": 1}
# print(sorted(d))
# print(sorted(d.items()))

# s = {465, 12, 48, 2, 1, 0}
# print(sorted(s))
# l = [1, 1+2j, 12.1, "hello"]
# # l.sort()
# # print(l)
# print(sorted(l))
# def ll(a):
#     if len(a) > 1:
#         return a[1]
#     else:
#         return a[0]
# l = ["hello", "hi", "by", "i"]
# # l.sort(key=len)
# print(sorted(l,key=ll))
# # print(l)
#
# # print(sorted)

l = list(range(1, 30))
def prime(a):
    f = []
    h = []
    for i in a:
        for j in range(2, i):
            if i % j == 0:
                f.append(i)
                break
            else:
                h.append(i)
                break
    return h

# print(sorted(prime(l)))
# print(sorted(l, key=prime))
# def primes_(a):
#     l = []
#     if a > 3:
#         for i in range(2, a):
#             if i >= 10:
#                 if i % 2 == 0:
#                     pass
#                 elif i % 3 == 0 or i % 5 == 0 or i % 7 == 0 or i % 9 == 0 or i % 11 == 0:
#                     pass
#                 else:
#                     l.append(i)
#             else:
#                 if i > 3 :
#                     if i % 2 == 0 or i % 3 == 0:
#                         pass
#                     else:
#                         l.append(i)
#                 else:
#                     l.append(i)
#         return l
#     return a
#
# print(sorted(l, key=primes_))

# class A:
#     def disp(self):
#         print("hi")
#
#
# A.disp(A)

# l = [1, 6, 3, "b", "a"]
# l1 = []
# l2 = []
# for i in l:
#     if isinstance(i, str):
#         l1.append(i)
#     else:
#         l2.append(i)
#
# l1.sort()
# l2.sort()
# l2.extend(l1)
# print(l2)
#
# from copy import deepcopy
# l3 = l.copy()
# l3 = deepcopy(l)
# print(id(l3))


# a, b = 1, (2, 3)
# print(a, b)
# # d = a, b, c
# # print(d)
# a, *_b, c, d = 1, 2, 3, 4, 5, 6
# print(a, _b, c, d)

def fi_(*args, **kwargs):
    a, b, *_c = args
    d = _c[-1]
    x = kwargs.keys()
    return type(x)


print(fi_(1, 2, 3, 4, 5, 6, a={"name": "jake", "age": 1}))
